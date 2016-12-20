"""
Demonstrate wrapping and using Fortran common block data.

Example assumes GNU compilers, e.g. MinGW w64 on Windows
"""

import os
import sys
import subprocess
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

fflags = []
cflags = []
link_args = []
define_macros = []
libraries = ['gfortran',]

# Determine OS and bitness
_is_windows = sys.platform=='win32'
_is_64bit = (getattr(sys, 'maxsize', None) or getattr(sys, 'maxint')) > 2 ** 32

if not _is_windows:
    fflags.append('-fPIC')
    cflags.append('-fPIC')

if _is_windows and _is_64bit:
    # MinGW-w64 does not include this definition, resulting in a crash on exit.
    define_macros.append(('MS_WIN64', None))
    
# Compile the fortran library sources
fsources = ['fort_mod.f90',]
fobjs = []
fmacros = ['-D{}'.format(m[0]) for m in define_macros if m[1] is None]
fmacros += ['-D{}'.format('='.join(m)) for m in define_macros if not m[1] is None]
for src in fsources:
    obj = os.path.splitext(src)[0] + '.o'
    args = ['gfortran', '-c', src, '-o', obj] + fflags + fmacros
    try:
        print(' '.join(args))
        subprocess.check_call(args)
    except:
        print('Error compiling {}'.format(src))
        print(' '.join(args))
        raise
    
    fobjs.append(obj)

ext_modules = [Extension(
    name = 'fort_test'
    , sources = ['fort_test.pyx']
    , extra_compile_args = cflags
    , extra_link_args = link_args
    , extra_objects = fobjs
    , libraries = libraries
    , define_macros=define_macros
    )]

setup(
    name = 'fort_test'
    , cmdclass = {'build_ext': build_ext}
    , ext_modules = ext_modules
    )

# Build with `python setup.py build_ext --inplace`
