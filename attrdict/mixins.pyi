from abc import ABCMeta
from collections import Mapping, MutableMapping
from typing import Any, TypeVar, Generic

KT = TypeVar('KT')
VT = TypeVar('VT')


class Attr(Mapping[KT, VT], Generic[KT, VT], metaclass=ABCMeta):
    def __call__(self, key: KT) -> Any: ...

    def __getattr__(self, key: KT) -> VT: ...

    def __add__(self, other: Any) -> Any: ...

    def __radd__(self, other: Any) -> Any: ...


class MutableAttr(Attr[KT, VT], MutableMapping[KT, VT], Generic[KT, VT], metaclass=ABCMeta):
    def __setattr__(self, key: KT, value: VT) -> None: ...

    def __delattr__(self, key: KT, force: bool = ...) -> None: ...
