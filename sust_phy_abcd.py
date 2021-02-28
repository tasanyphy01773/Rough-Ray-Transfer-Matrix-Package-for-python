# Python Package abcd
# Author: Tahmidul Azom Sany 
# Created for Computational Physics course of SUST Physics 
# Under the supervision of Dr. Md Enamul Hoque(Assistant Professor, SUST)


from numpy import *
from math import *

def distance(d):
    """
    This function creates an ray transfer matrix for d distance
    input:
    distance(50)
    output:
    The ray transfer matrix for your setup at d distance is
    [[ 1. 50.]
     [ 0.  1.]]
    """
    arr01 = array([
                    [1, d],
                    [0, 1] 
                                ], float)
    print("The ray transfer matrix for your setup at d distance is", )
    print(arr01)

#---------------------------------------------------------------------------------------------
def thinlens(f):
    """
    This function creates an ray transfer matrix for a lens with f focal length
    input:
    thinlens(50)
    output:
    The ray transfer matrix for your thin lens of focal lenth f is
    [[ 1.    0.  ]
     [-0.02  1.  ]]
    """
    arr02 = array([
                    [1, 0],
                    [-1/f, 1]                    
                            ])
    print("The ray transfer matrix for your thin lens of focal lenth f is", )
    print(arr02)


#---------------------------------------------------------------------------------------------

def refraflat(n1 ,n2):
    """
    This function creates an ray transfer matrix for refraction in a flat interface
    n1 = initial refractive index 
    n2 = final refractive index

    Example:
    source code is -> refraflat(n1, n2)
    Input:
    refraflat(4,2)
    Output:
    The ray transfer matrix for refraction in a flat interface is 
    [[1. 0.]
     [0. 2.]]
    """
    arr03 = array([
                    [1, 0],
                    [0, n1/n2]
                                ], float)
    print("The ray transfer matrix for refraction in a flat interface is ")
    print(arr03)

#----------------------------------------------------------------------------------------------

def refracurve(n1, n2, R):
    """
    This function creates an ray transfer matrix for a refraction at a curved interface
    Example:
    n1 = initial refractive index
    n2 = final refractive index
    R  = radius of curvature

    source code is -> refracurve(n1, n2, R)
    Input:
    refracurve(4,2,3)
    Output:
    The ray transfer matrix for refraction at a curved interface is 
    [[1.         0.        ]
     [0.33333333 2.        ]]

    """
    arr04 = array([
                    [1, 0],
                    [(n1-n2)/(R*n2), n1/n2]
                                ], float)
    print("The ray transfer matrix for refraction at a curved interface is ")
    print(arr04)
    
    
#----------------------------------------------------------------------------------------------    
    
def refflatmirror():
    """
    This function creates an ray transfer matrix for reflection from a flat mirror.
    You don't need to create any input here.
    input:
    refflatmirror()
    output:
    The ray transfer matrix for reflaction in a flat interface is 
    [[1. 0.]
     [0. 1.]]

    """
    arr05 = array([
                    [1, 0],
                    [0, 1]
                                ], float)
    print("The ray transfer matrix for reflaction in a flat interface is ")
    print(arr05)

#----------------------------------------------------------------------------------------------      

def refracurvemirror(Re):
    """
    This function creates an ray transfer matrix for refraction in a curved mirror. 
    You just need to enter effective radius of curvature, Re in the bracket. 
    Example:
    source code is -> refracurvemirror(Re):
    
    input:
    refracurvemirror(4)
    
    output:
    The ray transfer matrix for refraction at a curved mirror is 
    [[ 1.   0. ]
     [-0.5  1. ]]

    
    and it will provide a ray transfer matrix for refraction in a curved mirror. 
    """
    arr06 = array([
                    [1, 0],
                    [-2/Re, 1]
                                ], float)
    print("The ray transfer matrix for refraction at a curved mirror is ")
    print(arr06)
#----------------------------------------------------------------------------------------------      

def sinpri(k, d, n):
    """
    This function creates an ray transfer matrix for single prism. You just need to enter k,d,n
    here,
    
    k = cos(a)/cos(b) --> You have to calculate this. 
    a = the angle of refraction(in radian)
    b = the angle of incidence(in radian)
    
    d = Prism path length
    n = Refractive index of the prism material
    Example: 
    Source code-->sinpri(k,d,n)
    This matrix applies for orthogonal beam exit
    
    input:
    sinpri(2,4,3)
    
    output:
    The ray transfer matrix for a single prism is: 
    [[2.         0.66666667]
     [0.         0.5       ]]
   
    
    """
    arr07 = array([
                    [k, d/(n*k)],
                    [0, 1/k]
                                ], float)
    print("The ray transfer matrix for a single prism is: ")
    print(arr07)

#----------------------------------------------------------------------------------------------   

def mulpri(n, B, *k):
    """
    This function creates an ray transfer matrix for multiple prism. You just need to enter n, B in the bracket.
    here,
    n = the number of prism you are using 
    B = the total optical propagation distance of the multiple prism expander
    After inputing the first two argument in the code, the program will ask you to put the value of k.
    
    Example:
    input:
    mulpri(3, 2)
    
    output:
    Enter the beam expansion factor, k=2
    Enter the beam expansion factor, k=3
    Enter the beam expansion factor, k=4
    The ray transfer matrix for a multiple prism is: 
    [[24.          2.        ]
     [ 0.          0.04166667]]
    >
    """
    M = 1
    for i in range(n):
        k = float(input("Enter the beam expansion factor, k=", ))
        M = k*M

    arr08 = array([
                    [M, B],
                    [0, 1/M]
                                ], float)
    
    print("The ray transfer matrix for a multiple prism is: ")
    print(arr08)
