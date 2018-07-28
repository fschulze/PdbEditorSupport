from setuptools import setup, find_packages

README = open('README.rst', 'rb').read().decode('utf-8')


setup(name = 'PdbSublimeTextSupport',
      version = '0.2',
      description = 'Display source code in Sublime Text 2 while debugging with pdb.',
      keywords = 'sublimetext pdb',
      author = 'Martin Aspeli',
      author_email = 'optilude@gmail.com',
      url = 'http://pypi.python.org/pypi/PdbSublimeTextSupport',
      license = 'GPL',
      py_modules = ['PdbSublimeTextSupport'],
      include_package_data = False,
      platforms = 'Mac OS X',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: MacOS X',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Text Editors',
      ],
      long_description = README,
)
