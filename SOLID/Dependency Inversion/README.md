# Dependency Inversion Principle:

> High level modules should not depend on low level modules and (vice versa)
> instead should depend on abstraction.


**Suppose some Foo class has a dependency on an object of Bar class.
Then the Foo should not depend on a concrete implementation of Bar
But should depend on abstraction offered for implementation of each bar objects
that implements a contract for its implementation.**


**What makes this principle differnt from liskov substitution principle.**

**Liskov substitution principle** talks about relationship between classes in an inheritance
hierarchy. I.e. if i create a two classes subclassing a class Foo with two methods,
then the properties of the class (client) utilizing the two different objects of those two different subclasses
as a dependency should behave same.

**Depdency Inversion** states that the higher level module should not depend on the low level modules
but on an abstract implementation of low level modules
i.e. if i have a some class Foo (higher level module) and he other client ( class Bar) which 
utilizes the object of a class Foo as a depdendency. Then it is a direct violation of depdency management
on Bar class. Bar class should instead depend on a abstract implementation of Foo class or an interface / contract
by which it (Foo class) is implemented.

[...Read More](https://stackoverflow.com/questions/58300258/solid-design-principles-liskov-substitution-principle-and-dependency-inversion)