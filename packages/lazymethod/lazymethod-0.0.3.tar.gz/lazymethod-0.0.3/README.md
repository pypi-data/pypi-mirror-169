lazymethod 是一个 python 对象的懒加载装饰器，类似于 `@property` 但只会调用一次。

不仅如此，`lazy` 还实现了返回值的静态类型识别。

## 基本使用

只需要将方法加入到懒加载装饰器：`@lazymethod(<return type>)` 。

或使用 `var: [return type] = lazy(lambda: ...)` 。

```python
from pylazy import lazymethod

class Model:
    @lazymethod(list)
    def numbers(self):
        print('get numbers')
        return [1, 2, 3]

m1 = Model()
print(m1.numbers)
print(m1.numbers)

m2 = Model()
print(m2.numbers)
print(m2.numbers)
```

```python
### Print:
get numbers
[1, 2, 3]
[1, 2, 3]
get numbers
[1, 2, 3]
[1, 2, 3]
```

结果上所示。可以看到，每个对象只会调用懒加载方法一次。

也可以将方法声明为静态属性，如此就可以在任何时候都只调用一次：

```python
from typing import ClassVar

@lazymethod(ClassVar[list])
def numbers(self):
    print('get numbers')
    return [1, 2, 3]

m1 = Model()
print(m1.numbers)

m2 = Model()
print(m2.numbers)
print(Model.numbers)
    
""" Print:
get numbers
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
"""
```

### 使用 lambda

lazymethod 支持使用 `lambda` 表达式创建懒加载属性：


```python
from typing import ClassVar
from pylazy import lazy

class Model:
    numbers: list = lazy(lambda: [1, 2, 3])
    ages: ClassVar[list] = lazy(lambda: [10, 20, 30])

m1 = Model()
m2 = Model()

print(m1.numbers)
print(m2.ages)
```

结果如下：

```python
### Print:
[1, 2, 3]
[10, 20, 30]
```

## 静态识别返回值类型

不论你是使用 `@lazymethod` 还是 `lazy` 来创建懒加载属性，它们都会静态识别方法返回值类型：

![](33d61644f2ecc319455f4b1970fa0d0.jpg)

----

![](06201ef2fdbd0db6aa9a7c5d9a633c4.jpg)
