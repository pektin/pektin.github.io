The Jam Programming Language
############################

.. rubric:: An open source programming language that combines the expressiveness
    of dynamic languages with a powerful static type system for native
    efficiency.

::

    # Compute the average line length from stdin
    lines = io.stdin.lines()
    length_sum = lines.sum()

    if lines.length > 0
      average = length_sum / lines.length
      print("Average line length: #{average}")
    end

.. note::
    The above example is not yet entirely supported by the language

.. toctree::
    :hidden:

    about
    docs/index

Features
========

* Strong, static duck-typing, with optional type annotations
* Common value semantics between values and types*
* Fast compiling*
* Compiles to efficient native code
* Non-restrictive towards programming paradigms
* Powerful meta-programming* (dependent types, meta-classes)
* Efficient C bindings*

\* Some features are yet to be implemented

Open Source
===========

Jam is licensed under MIT, giving everyone the freedom to do what they want to
do with the language. Contributions on Github_ are always welcome.

.. _Github: https://github.com/pektin/jam
