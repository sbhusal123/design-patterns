class _Foo:
    pass


_instance = None


def Foo():
    global _instance
    if _instance is None:
        # Thread lock if this is to be accessed using concurrency.
        _instance = _Foo()
    return _instance
