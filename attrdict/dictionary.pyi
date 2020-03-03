from typing import TypeVar, Dict, Generic

from attrdict.mixins import MutableAttr

KT = TypeVar('KT')
VT = TypeVar('VT')


class AttrDict(Dict[KT, VT], MutableAttr[KT, VT], Generic[KT, VT]):
    def __init__(self, *args: KT, **kwargs: VT) -> None: ...
