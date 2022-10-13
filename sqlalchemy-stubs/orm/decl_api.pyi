from .decl_base import _declarative_constructor

class DeclarativeMeta:
    def __init__(self, classname, bases, dict_, **kw) -> None: ...

def declarative_base(
    bind=None,
    metadata=None,
    mapper=None,
    cls=object,
    name="Base",
    constructor=_declarative_constructor,
    class_registry=None,
    metaclass=DeclarativeMeta
): ...