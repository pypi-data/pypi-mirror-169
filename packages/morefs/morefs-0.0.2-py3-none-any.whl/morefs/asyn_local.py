import asyncio
import datetime
import errno
import functools
import os
import shutil

import aiofile
import aiofiles.os
from aiofiles.os import wrap  # type: ignore[attr-defined]
from fsspec import AbstractFileSystem
from fsspec.asyn import AbstractBufferedFile, AsyncFileSystem
from fsspec.implementations.local import LocalFileSystem

aiofiles.os.chmod = wrap(os.chmod)  # type: ignore[attr-defined]
aiofiles.os.utime = wrap(os.utime)  # type: ignore[attr-defined]
aiofiles.os.path.islink = wrap(os.path.islink)  # type: ignore[attr-defined]
aiofiles.os.path.lexists = wrap(os.path.lexists)  # type: ignore[attr-defined]
async_rmtree = wrap(shutil.rmtree)  # type: ignore[attr-defined]
async_move = wrap(shutil.move)  # type: ignore[attr-defined]
async_copyfile = wrap(shutil.copyfile)  # type: ignore[attr-defined]


def _copy_to_fobj(fs, path1, fdst):
    with fs.open(path1, "rb") as fsrc:
        shutil.copyfileobj(fsrc, fdst)


async_copy_to_fobj = wrap(_copy_to_fobj)


async def copy_asyncfileobj(fsrc, fdst, length=shutil.COPY_BUFSIZE):
    fsrc_read = fsrc.read
    fdst_write = fdst.write
    while buf := await fsrc_read(length):
        await fdst_write(buf)


# pylint: disable=arguments-renamed


def wrapped(func):
    @functools.wraps(func)
    def inner(self, *args, **kwargs):
        return func(self, *args, **kwargs)

    return inner


class AsyncLocalFileSystem(AsyncFileSystem):  # pylint: disable=abstract-method
    find = wrapped(AbstractFileSystem.find)
    walk = wrapped(AbstractFileSystem.walk)
    exists = wrapped(AbstractFileSystem.exists)
    isdir = wrapped(AbstractFileSystem.isdir)
    isfile = wrapped(AbstractFileSystem.isfile)
    lexists = staticmethod(LocalFileSystem.lexists)

    ls = wrapped(LocalFileSystem.ls)
    info = wrapped(LocalFileSystem.info)
    _info = wrap(LocalFileSystem.info)

    async def _ls(self, path, detail=True, **kwargs):
        if detail:
            entries = await aiofiles.os.scandir(path)
            return [await self._info(f) for f in entries]
        return [os.path.join(path, f) for f in await aiofiles.os.listdir(path)]

    async def _rm_file(self, path, **kwargs):
        await aiofiles.os.remove(path)

    async def _rmdir(self, path):
        await aiofiles.os.rmdir(path)

    async def _mkdir(self, path, create_parents=True, **kwargs):
        if create_parents:
            if await self._exists(path):
                raise FileExistsError(
                    errno.EEXIST, os.strerror(errno.EEXIST), path
                )
            return await self._makedirs(path, exist_ok=True)
        await aiofiles.os.mkdir(path)

    async def _makedirs(self, path, exist_ok=False):
        await aiofiles.os.makedirs(path, exist_ok=exist_ok)

    async def _cat_file(self, path, start=None, end=None, **kwargs):
        async with self.open_async(path, "rb") as f:
            if start is not None:
                if start >= 0:
                    f.seek(start)
                else:
                    f.seek(max(0, f.size + start))
            if end is not None:
                if end < 0:
                    end = f.size + end
                return await f.read(end - f.tell())
            return await f.read()

    async def _pipe_file(self, path, value, **kwargs):
        async with self.open_async(path, "wb") as f:
            await f.write(value)

    async def _put_file(self, path1, path2, **kwargs):
        await self._cp_file(path1, path2, **kwargs)

    async def _get_file(self, path1, path2, **kwargs):
        write_method = getattr(path2, "write", None)
        if not write_method:
            return await self._cp_file(path1, path2, **kwargs)
        if isinstance(
            path2, AbstractBufferedFile
        ) or asyncio.iscoroutinefunction(write_method):
            async with self.open_async(path1, "rb") as fsrc:
                return await async_copy_to_fobj(fsrc, path2)
        return await async_copy_to_fobj(path1, path2)

    async def _cp_file(self, path1, path2, **kwargs):
        if await self._isfile(path1):
            return await async_copyfile(path1, path2)
        if await self._isdir(path1):
            return await self._makedirs(path2, exist_ok=True)
        raise FileNotFoundError

    async def _mv_file(self, path1, path2, **kwargs):
        await async_move(path1, path2)

    async def _lexists(self, path, **kwargs):
        return await aiofiles.os.path.lexists(path)

    async def _created(self, path):
        info = await self._info(path=path)
        return datetime.datetime.utcfromtimestamp(info["created"])

    async def _modified(self, path):
        info = await self._info(path=path)
        return datetime.datetime.utcfromtimestamp(info["mtime"])

    async def _rm(
        self, path, recursive=False, maxdepth=None
    ):  # pylint: disable=arguments-differ, unused-argument
        if isinstance(path, str):
            path = [path]

        for p in path:
            if recursive and await self._isdir(p):
                if os.path.abspath(p) == os.getcwd():
                    raise ValueError("Cannot delete current working directory")
                await async_rmtree(p)
            else:
                await aiofiles.os.remove(p)

    async def _chmod(self, path, mode):
        await aiofiles.os.chmod(path, mode)

    async def _link(self, src, dst):
        await aiofiles.os.link(src, dst)

    async def _symlink(self, src, dst):
        await aiofiles.os.symlink(src, dst)

    async def _islink(self, path):
        return await aiofiles.os.path.islink(path)

    async def _touch(self, path, **kwargs):
        if self._exists(path):
            return await aiofiles.os.utime(path, None)
        async with self.open_async(path, "a"):
            pass

    _open = LocalFileSystem._open  # pylint: disable=protected-access

    def open_async(  # pylint: disable=invalid-overridden-method
        self, path, mode="rb", **kwargs
    ):
        return aiofile.async_open(path, mode, **kwargs)
