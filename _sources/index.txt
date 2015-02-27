.. _index:

The Jam Programming Language
############################

**An open source programming language that combines the expressiveness of
dynamic languages with the power of modern type systems and native efficiency.**

Expressive
==========

Jam supports many of the concepts found in modern interpreted languages. It's
syntax aims to be easy to read and easy to write and completely unambiguous.

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

Jam is being developed under the GNU General Public License Version 3

.. toctree::
    :hidden:

    about
    jam/index
