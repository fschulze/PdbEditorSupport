from setuptools import setup


README = open('README.rst', 'rb').read().decode('utf-8')


setup(
    name='PdbEditorSupport',
    version='0.4.0',
    description='Display source code in your editor while debugging with pdb.',
    keywords='editor pdb sublimetext textmate',
    author='Florian Schulze',
    author_email='mail@florian-schulze.net',
    url='https://github.com/fschulze/PdbEditorSupport',
    license='GPL',
    py_modules=['PdbEditorSupport'],
    include_package_data=False,
    platforms='Mac OS X',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Text Editors'],
    long_description=README)
