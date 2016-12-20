Cython Library Wrapper Examples
===============================

Examples of wrapping external libraries with Cython.

Please feel free to fork and send pull requests, or otherwise contribute.

Python has a number of tools for integrating with external code. Sadly, many 
of these tools lack desirable features and/or the available documentation is 
limiting. This repository aims to collect working examples for wrapping
external libaries for use in Python. The primary tool will be Cython however,
other methods may be integrated as there are many situations were multiple tools
can improve the process.

Of special interest is wrapping Fortran libraries. Fortran was and still is 
the goto (pun intended) language for scientific computing in many fields. 
Consequently there is a wealth of relevant and stable code written in Fortran. 
Often this is Fortran 77, but the trend is toward mixing F77 with modern 
Fortran, F90, F2003, etc. The tools developed for wrapping one version of 
Fortran may not understand the features of the other versions.

Contents
--------

Fortran
+++++++

Unless otherwise noted these examples assume the use of GNU compilers.  They 
should work on Windows, Linux, and likely OSX. Testing is primarily on Windows.

1. Common Blocks (common_blocks)

    Demonstrate how to reference Fortran common blocks from Cython.
    This is a verbatim implementation of the solution originally posted [here][1]
  
TODO
----

1. Basic Usage (f77_basic)

    Demonstrate wrapping a F77 subroutine.

Useful Links
------------

 - [Using Python as glue](https://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html)
 - [Interoperable Subroutines and Functions](https://gcc.gnu.org/onlinedocs/gfortran/Interoperable-Subroutines-and-Functions.html)
 - [Setup a MinGW build environment](http://ascend4.org/Setting_up_a_MinGW-w64_build_environment)


[1]: http://stackoverflow.com/a/41192647/673590

