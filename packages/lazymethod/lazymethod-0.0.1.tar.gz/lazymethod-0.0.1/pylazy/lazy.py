from typing import Callable, TypeVar, Type

T = TypeVar('T')


class lazy:
    """ 实现赖加载属性的装饰器 """
    __slots__ = ['func', 'name', 'is_class_var']

    def __init__(self, func: Callable):
        self.func = func
        self.name = ''
        self.is_class_var = False

    def __get__(self, instance, owner):
        fn_name = self.func.__name__
        own = owner if self.is_class_var else instance
        args = () if fn_name == '<lambda>' else (own,)
        v = self.func(*args)
        setattr(own, self.name, v)
        return v

    def __set_name__(self, owner, name):
        self.name = name
        if fields := getattr(owner, '__annotations__', None):
            type_ = fields.get(name)
            if str(type_).startswith('typing.ClassVar'):
                self.is_class_var = True


def lazymethod(ret: Type[T]):
    def decorate(func):
        def wrapper(*args, **kwargs) -> T:
            lazy_ = lazy(func)
            lazy_.is_class_var = True
            return lazy_
        return wrapper()
    return decorate
