from typing import TypeVar, Dict, Generic, overload

from attrdict.mixins import MutableAttr

KT = TypeVar('KT')
VT = TypeVar('VT')


class AttrDict(Dict[KT, VT], MutableAttr[KT, VT], Generic[KT, VT]):
    @overload
    def __init__(self, mapping: Dict[KT, VT]) -> None: ...

    @overload
    def __init__(self, *args: KT, **kwargs: VT) -> None: ...

    def __init__(self, *args: KT, **kwargs: VT) -> None: ...
