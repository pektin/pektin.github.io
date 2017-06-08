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
    The above example is not yet fully supported by the language

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
* Powerful meta-programming concepts (
  :doc:`Compile-time evaluation<docs/jam/modifiers/pragma>`,
  :doc:`meta-classes<docs/jam/types>`\*)
* First order :doc:`dependent types<docs/jam/dependent-types>`\*
* Efficient C bindings*

\* Some features are yet to be implemented, please see the
:doc:`roadmap<docs/roadmap/index>` for development details.

Open Source
===========

Jam is licensed under MIT, giving everyone the freedom to do what they want to
do with the language. Contributions on Github_ are always welcome.

.. _Github: https://github.com/pektin/jam
