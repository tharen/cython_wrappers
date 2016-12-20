! Demonstrate access to common block data from Cython.
!

module fort_mod
    use iso_c_binding
    implicit none
contains

subroutine init_com() bind(C)
    ! Initialize the common block data
    real(c_double) :: a(2)
    real(c_float) :: b(5)
    integer(c_int) :: c(5)

    common /foo_com/ a, b, c

    a = (/3.14159265359,2.71828182846/)
    b = (/0,1,2,3,4/)
    c = (/0,1,2,3,4/)

end subroutine

end module
