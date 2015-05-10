.. _index:

The Jam Programming Language
############################

.. rubric:: An open source programming language that combines the expressiveness of
    dynamic languages with the power of modern type systems and native efficiency.

::

    import sys

    sum_length = length = 0

    for line in sys.stdin
      length += 1
      sum_length += line.length
    end

    average = sum_length / length if length > 0 else 0
    print("Average line length: #{average}")

.. note::
    The above example is not yet supported by the language

Expressive
==========

Jam supports many of the concepts found in modern interpreted languages. It's
syntax aims to be easy to read, easy to write and completely unambiguous.

Powerful
========

Jam's type system supports a mix of static and dynamic typing. The programmer is
given the option of declaring a type or keeping it generic. The compiler
intuitively infers static types that fit to the situation, rather than impose
unnecessary restrictions.

Jam's type system does however have specific restrictions on concepts such as
the ``null`` value, that ensure that common mistakes are caught before they
cause a problem.

Fast
====

Jam boasts native efficiency. Using the static type system, the compiler is able
to convert your high level code into native executables that run on a minimal
runtime to ensure maximum performance.

Open Source
===========

Jam is being developed under the MIT License, giving everyone the freedom to do
what they want to do with the language.

.. toctree::
    :hidden:

    about
    jam/index
