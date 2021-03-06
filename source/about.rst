:orphan:

About Jam
#########

Concept
=======

Jam is an attempt to bridge the gap between dynamic, interpreted languages and
static, compiles ones.

Effectively most useful language constructs from languages such as Ruby_ and
Python_ can be statically verified and compiled to something as natively
efficient as if the equivalent were written in languages such as C++ or D_.

Because of this, it is possible to combine a lot of the type safety and other
neat features from static compiled languages with the dynamic nature common to
interpreted ones. This includes types as values, monkey-patching and effective
duck-typing.

Design Goals
============

* Easy to read, understand and reason about.
* A tight set of complimentary language features that expand to more powerful concepts.
* Good, large set of standardised tools/libraries.
* Efficiently compile-able to fast native code.

Syntax
======

Jam syntax is inspired by Ruby_ with a hint of Python_ and D_, designed with
readability and writeability in mind.

.. _D: http://dlang.org
.. _Ruby: http://ruby-lang.org
.. _Python: http://python.org
