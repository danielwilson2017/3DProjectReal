
import math

def enter_point() :
    x = float(input("Enter an x value: "))
    y = float(input("Enter a y value: "))
    z = float(input("Enter a z value: "))
    return (x, y, z)
    
def three_points() :
    '''Returns a list of 3 3d pts'''
    points = []
    for i in range(3):
        points.append(enter_point())
    return points

def two_vectors(points) :
    '''Inputs a list of 2 pts and returns a list of vectors from 1st pt'''
    vectors = []
    for i in range(2) :
        x = points[i+1][0]-points[0][0]
        y = points[i+1][1]-points[0][1]
        z = points[i+1][2]-points[0][2]
        vectors.append((x,y,z))
    return vectors
    
def xprod(vectors) :
    '''Inputs a list of 2 vector and returns A, B, C, of plane equation'''
    A = vectors[0][1]*vectors[1][2]-vectors[0][2]*vectors[1][1]
    B = -1*(vectors[0][0]*vectors[1][2]-vectors[0][2]*vectors[1][0])
    C = vectors[0][0]*vectors[1][1]-vectors[0][1]*vectors[1][0]
    return(A, B, C)
    
def solve_tri(vectors) :
    '''Inputs a list of 2 vectors and returns 2 magnitudes and included angle'''
    dot = vectors[0][0]*vectors[1][0]-vectors[0][1]*vectors[1][1]+vectors[0][2]*vectors[1][2]
    mag1 = math.sqrt(vectors[0][0]**2 + vectors[0][1]**2 + vectors[0][2]**2)
    mag2 = math.sqrt(vectors[1][0]**2 + vectors[1][1]**2 + vectors[1][2]**2)
    return(math.acos(dot/(mag1*mag2)), mag1, mag2)
    
points = three_points()
vectors = two_vectors(points)
xprod = xprod(vectors)
solve_tri = solve_tri(vectors)

'''Now find triangle area 2 different ways'''
tri_area1 = 1/2*math.sqrt(xprod[0]**2+xprod[1]**2+xprod[2]**2)
tri_area2 = 1/2*math.sin(solve_tri[0])*solve_tri[1]*solve_tri[2]
print("Tri Area", tri_area, tri_area2)





