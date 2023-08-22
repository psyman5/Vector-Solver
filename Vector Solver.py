import math
import numpy as np

#TODO: Implement 3D vectors and fix the numpy tangent bug being caused.

class Vector2D: #class for 2D vectors with descriptors magnitude and direction
    def __init__(self, mag, dir):
        self.mag = mag
        self.dir = dir
    
    def get_x_mag(self):
        self.x = self.mag*np.cos(self.dir)
        return self.x
    def get_y_mag(self):
        self.y = self.mag*np.sin(self.dir)
        return self.y

class Vector3D: #WIP class for 3D vectors with descriptors x, y, z, magnitude, direction in all three dimensions (azimuth)
    def __init__(self, x, y, z, mag, xDir, yDir, zDir):
        self.x = x
        self.y = y
        self.z = z
        self.mag = mag
        self.xDir = xDir
        self.yDir = yDir
        self.zDir = zDir


#specifies the number of vectors and initializes list to store the pertinent information. 3D is not added yet.
vectorNumber = 1
vectorMagList = []
vectorDirList = []


for x in range(1, vectorNumber+1): #for loop that continually asks the user for input information about the numbered vectors.
    vectorMagList.append((int((input("Mag of Vector " + str(x) + ": \n")))*np.pi/180))
    vectorDirList.append((int(input("Direction of Vector " + str(x) + ": \n")))*np.pi/180)


vectors = [Vector2D(vectorMagList[s],vectorDirList[s]) for s in range(vectorNumber)] #creates a list storing classed vectors with the descriptors specified.

print(vectors)

#sums x and y vectors for a resultant
resX = sum([v.get_x_mag() for v in vectors])
resY = sum([v.get_y_mag() for v in vectors])


#creates a new Vector2D Classed Vector and outputs the results of the addition.
resVector = Vector2D((math.sqrt(resX**2+resY**2)),
                     math.atan(resY/resX))


print(resVector.mag, resVector.dir)




