The Jam Programming Language
############################

.. rubric:: An open source programming language that combines the expressiveness
    of dynamic languages with a powerful static type system for native
    efficiency.

::

    # Compute the average line length from stdin
    lines = io.stdin.lines()

    if lines.length > 0
      average = lines.map($length).sum() / lines.length
    else
      average = 0
    end

    puts("Average line length: #{average}")

.. note::
    The above example is not yet entirely supported by the language

.. toctree::
    :hidden:

    docs/index

Features
========

* Strong, static duck-typing, with
  :doc:`optional type annotations<docs/jam/methods>`
* Common value semantics between :doc:`values<docs/jam/values>` and
  :doc:`types<docs/jam/types>`
* Fast compiling* to efficient native code
* Non-restrictive towards programming paradigms
* Powerful meta-programming (:doc:`dependent types<docs/jam/dependent-types>`\*,
  :doc:`meta-classes<docs/jam/types>`\*)
* :doc:`Compile-time evaluation<docs/jam/modifiers/pragma>`
* Efficient C bindings*

\* Some features are yet to be implemented

Open Source
===========

Jam is licensed under MIT, giving everyone the freedom to do what they want to
do with the language. Contributions on Github_ are always welcome.

.. _Github: https://github.com/pektin/jam
