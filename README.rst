This module is used to hook up``pdb``, the python debugger, with
Sublime Text, enabling it to display the debugged source code during
a``pdb``session.

You can install with ``pip``::

  $ pip install PdbSublimeTextSupport

Or download, unpack the package and install with::

  $ python setup.py install

Next you need to hook up ``pdb`` with this module by adding the
following to your ``.pdbrc`` file, which you can create in your home
directory if it's not there already::

  import PdbSublimeTextSupport
  PdbSublimeTextSupport.patch()

Finally, ensure that the ``subl`` command line tool has
been installed as per `these instructions
<http://www.sublimetext.com/docs/3/osx_command_line.html>`_.

Afterwards Sublime Text should get started automatically whenever
you enter a debug session.  The current source line will be
displayed simultaneously while stepping through the code.

This module is based on ``PdbTextMateSupport`` by Andi Zeidler
and others.
