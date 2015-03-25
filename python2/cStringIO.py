"""Stub file for the 'cStringIO' module."""
# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, Undefined, GenericType

InputType = Undefined(StringI)
OutputType = Undefined(StringO)
cStringIO_CAPI = Undefined(object)

def StringIO(*args, **kwargs) -> object: pass


class StringI(object):
    def close() -> None: pass
    def flush() -> None: pass
    def getvalue(*args, **kwargs) -> str: pass
    def isatty() -> bool: pass
    def read(*args, **kwargs) -> str: pass
    def readline(*args, **kwargs) -> str: pass
    def readlines(*args, **kwargs) -> List[str]: pass
    def reset() -> None: pass
    def seek(a: int, *args, **kwargs) -> None: pass
    def tell() -> int: pass
    def truncate(*args, **kwargs) -> None:
        raise IOError()

class StringO(object):
    def close() -> None: pass
    def flush() -> None: pass
    def getvalue(*args, **kwargs) -> str: pass
    def isatty() -> bool: pass
    def read(*args, **kwargs) -> str: pass
    def readline(*args, **kwargs) -> str: pass
    def readlines(*args, **kwargs) -> List[str]: pass
    def reset() -> None: pass
    def seek(a: int, *args, **kwargs) -> None: pass
    def tell() -> int: pass
    def truncate(*args, **kwargs) -> None:
        raise IOError()
    def write(a) -> None: pass
    def writelines(*args, **kwargs) -> None: pass