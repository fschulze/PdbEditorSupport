================
PdbEditorSupport
================


This module is used to hook up ``pdb``, the python debugger, with your editor.
This enables it to display the debugged source code during a ``pdb`` session.

You can install with ``pip``::

  $ pip install PdbEditorSupport

Or download, unpack the package and install with::

  $ python setup.py install

Next you need to hook up ``pdb`` with this module.
See the next sections to see how.

Afterwards your editor should get started automatically whenever you enter a debug session.
The current source line will be displayed simultaneously while stepping through the code.


Editors
=======

Sublime Text
------------

For Sublime Text support add this to ``.pdbrc``::

  import PdbEditorSupport
  PdbEditorSupport.patch(editor='sublime')

Ensure that the ``subl`` command line tool has been installed as per
`these instructions
<http://www.sublimetext.com/docs/3/osx_command_line.html>`_.


Acknowledgments
===============

This module is based on ``PdbSublimeTextSupport`` by Martin Aspeli, which in
turn is based on ``PdbTextMateSupport`` by Andi Zeidler and others.
