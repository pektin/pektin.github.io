.. _about:

About Jam
#########

Jam is the result of a theory. A theory that most code written in dynamic
languages that follows standard practices contains enough information to compile
that same code to highly efficient native executables.

Jam's Design
============

The goal of Jam is to have as many uses as C++, D_ or Rust_ while making it
"feel" like writing Ruby_ or Python_ code. Jam's type system type system should
be static, but behave as if it were dynamic.

From this a hybrid type system evolved, that allowed for type declarations and
contract based programming while not making it mandatory. An extensive set of
rules built upon expectation dictate how the compiler handles non-specified
types.

Syntax
------

The syntax of Jam is heavily inspired by Ruby_ and Python_, with the occasional
hint of other languages. The syntax was designed after the type system and
builds upon it.

.. _D: http://dlang.org
.. _Rust: http://rust-lang.org
.. _Ruby: http://ruby-lang.org
.. _Python: http://python.org

