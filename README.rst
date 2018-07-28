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

The ``subl`` command will by default called with ``-b filename:lineno``,
where ``filename`` and ``lineno`` are replaced accordingly.

You can change the default ``subl`` command by setting the ``command`` keyword option.

You can change the default arguments with the ``command_args`` keyword option.

Example with the defaults::

    import PdbEditorSupport
    PdbEditorSupport.patch(
        editor='sublime',
        command='subl',
        command_args=['-b', '{filename}:{lineno}'])

TextMate
--------

For Sublime Text support add this to ``.pdbrc``::

    import PdbEditorSupport
    PdbEditorSupport.patch(editor='textmate')

You can change the default ``TextMate`` application name with the ``application`` keyword option.

You can change the default url used via Apple Script with the ``url`` keyword option.

Example with the defaults::

    import PdbEditorSupport
    PdbEditorSupport.patch(
        editor='textmate',
        application='TextMate',
        url='txmt://open?url=file://{filename}&line={lineno}&column=2')


Other editors
-------------

Other editors which allow opening files via the command line can be used as well.

You can use arbitrary shell commands like this::

    import PdbEditorSupport
    PdbEditorSupport.patch(
        func='shell',
        command='mycommand',
        command_args=['{filename}:{lineno}'])


Acknowledgments
===============

This module is based on ``PdbSublimeTextSupport`` by Martin Aspeli, which in
turn is based on ``PdbTextMateSupport`` by Andi Zeidler and others.
