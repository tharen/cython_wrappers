"""
Demonstrate how to reference common block data from Cython.
"""

# NOTE: cdef extern usually refers to a header file, but it's not strictly necessary
#       It would probably be wise however if multiple libraries were being called
cdef extern:
    void init_com()
    
    cdef struct foo_com:
        double a[2]
        float b[5]
        int c[5]

    cdef foo_com foo_com_

def test():
    
    # Initially the common block variables are not initialized
    print(foo_com_.a)
    print(foo_com_.b)
    print(foo_com_.c)
    
    # Call the initialization routine
    init_com()
     
    print(foo_com_.a)
    print(foo_com_.b)
    print(foo_com_.c)
 
    # Common block variables can be modified, with some caveats of course
    foo_com_.c[:] = [foo_com_.c[i]*2 for i in range(5)]
    print('c x2:', foo_com_.c)
    
