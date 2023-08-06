:py:mod:`example`
=================

.. py:module:: example

.. autoapi-nested-parse::

   Example module

   This is a description



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   example.Foo
   example.Bar
   example.ClassWithNoInit
   example.One
   example.MultilineOne
   example.Two



Functions
~~~~~~~~~

.. autoapisummary::

   example.decorator_okay
   example.fn_with_long_sig



.. py:class:: Foo(attr)

   Bases: :py:obj:`object`

   This is using custom filters.
   .. py:class:: Meta

      Bases: :py:obj:`object`

      This is using custom filters.
      .. py:method:: foo()
         :classmethod:

         The foo class method



   .. py:property:: property_simple
      :type: int

      This property should parse okay.


   .. py:attribute:: class_var
      :annotation: = 42

      

   .. py:attribute:: another_class_var
      :annotation: = 42

      Another class var docstring


   .. py:attribute:: attr2
      

      This is the docstring of an instance attribute.

      :type: str


   .. py:method:: method_okay(foo=None, bar=None)

      This method should parse okay


   .. py:method:: method_multiline(foo=None, bar=None, baz=None)

      This is on multiple lines, but should parse okay too

      pydocstyle gives us lines of source. Test if this means that multiline
      definitions are covered in the way we're anticipating here


   .. py:method:: method_tricky(foo=None, bar=dict(foo=1, bar=2))

      This will likely fail our argument testing

      We parse naively on commas, so the nested dictionary will throw this off


   .. py:method:: method_sphinx_docs(foo, bar=0)

      This method is documented with sphinx style docstrings.

      :param foo: The first argument.
      :type foo: int

      :param int bar: The second argument.

      :returns: The sum of foo and bar.
      :rtype: int


   .. py:method:: method_google_docs(foo, bar=0)

      This method is documented with google style docstrings.

      Args:
          foo (int): The first argument.
          bar (int): The second argument.

      Returns:
          int: The sum of foo and bar.


   .. py:method:: method_sphinx_unicode()

      This docstring uses unicodé.

      :returns: A string.
      :rtype: str


   .. py:method:: method_google_unicode()

      This docstring uses unicodé.

      Returns:
          str: A string.



.. py:function:: decorator_okay(func)

   This decorator should parse okay.


.. py:class:: Bar(attr)

   Bases: :py:obj:`Foo`

   This is using custom filters.
   .. py:method:: method_okay(foo=None, bar=None)

      This method should parse okay



.. py:class:: ClassWithNoInit

   This is using custom filters.

.. py:class:: One

   This is using custom filters.

.. py:class:: MultilineOne

   Bases: :py:obj:`One`

   This is using custom filters.

.. py:class:: Two

   Bases: :py:obj:`One`

   This is using custom filters.

.. py:function:: fn_with_long_sig(this, *, function=None, has=True, quite=True, a, long, signature, many, keyword, arguments)

   A function with a long signature.


