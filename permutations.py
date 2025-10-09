# The objective is to generate all possible integer coordinates in a 3D grid, [i,j,k], 
# within a specific boundary defined by x,y, and z, and then remove any coordinate where the
# sum of its elements (i+j+k) equals a forbidden value, n.

# Coordinate	Constraint	Sum Check
# i	             0≤i≤x	
# j	             0≤j≤y	
# k	             0≤k≤z	    i+j+k !=n



# METHOD 1: Using itertools.product
from itertools import permutations
from itertools import product


def set_permutations(x,y,z,n):
    
    p = [x,y,z]
    
    var1 = [list(p) for p in product(range(x+1), range(y+1), range(z+1)) if sum(p) != n ]
    
    print(var1)
    

x = int(input())
y = int(input())
z = int(input())
n = int(input())

set_permutations(x,y,z,n)


# METHOD 2: 
x = int(input())
y = int(input())
z = int(input())
n = int(input())


result = [
    [i,j,k]
    for i in range (x+1)
    for j in range (y+1)
    for k in range (z+1)
    if i+j+k != n 
]

print (result)