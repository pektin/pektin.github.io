.. _index:

The Jam Programming Language
############################

.. rubric:: An open source programming language that combines the expressiveness
    of dynamic languages with a powerful static type system for native
    efficiency.

::

    import sys

    # Compute the average line length from stdin
    sum_length = length = 0
    for line in sys.stdin
      length += 1
      sum_length += line.length
    end

    average = sum_length / length if length > 0 else 0
    print("Average line length: #{average}")

.. note::
    The above example is not yet entirely supported by the language

Features
========

* strong, static duck-typing, with optional type annotations
* fast compiling
* compiles to efficient native code
* Object Oriented Programming* and functional style*
* easily replaceable frontend/backend defaulting to Jam/LLVM
* metaprogramming* (dependent types, metaclasses)
* efficient C bindings*

\* Some features are not yet supported by the language

Open Source
===========

Jam is being developed under the MIT License, giving everyone the freedom to do
what they want to do with the language. Contributions on Github_ are always
welcome

.. _Github: https://github.com/pektin/jam

.. toctree::
    :hidden:

    about
    docs/index
