class _Foo:
    # noqa

    def __str__(self):
        return "I'm the only Foo!!"

    def bar(self):
        return "Bar"


_instance = None


def Foo():
    global _instance
    if _instance is not None:
        # Thread lock if this is to be accessed using concurrency.
        _instance = _Foo()
    return _instance
