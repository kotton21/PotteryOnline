
#shape in 2d:
#translate to 3d
#Apply rotation matrix
#result: 3d array nx3xs : n=numpoints and s=rotation slices

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

import json

#SHAPE = [
#	[1,0],
#	[2,1],
#	[2.1,2],
#    [3,3]]
SHAPE = [
	[1,0],
	[1,1]]


NUM_ROTATIONS = 6
NUM_POINTS = len(SHAPE)
NUM_VERTS = NUM_POINTS * NUM_ROTATIONS


#translate to 3d
shape = np.array(SHAPE)
zers = np.zeros((NUM_POINTS,1))
shape2d = np.hstack((shape, zers))
#print shape2d

#shape3d = np.zeros((NUM_POINTS, NUM_ROTATIONS, 3))
shape3d = np.zeros((NUM_ROTATIONS, NUM_POINTS, 3))

rm = np.zeros((3,3))
for i in range(NUM_ROTATIONS):
    theta = i*2.0*np.pi/NUM_ROTATIONS
    rm = np.array([[np.cos(theta), 0., np.sin(theta)],
                   [0., 1., 0.],
                   [-np.sin(theta), 0., np.cos(theta)]])
    # print(shape2d.shape)
    # print(rm.shape)
    # print(shape2d)
    # print(np.dot(shape2d, rm))
    #print np.dot(shape2d, rm)
    # print shape3d
    #print shape3d[i*NUM_POINTS,:]
    shape3drot = np.dot(shape2d, rm)
    shape3d[i,:,:] = shape3drot

#shape3d = np.round(shape3d,4)
#print shape3d
#print shape3d[0,:,:]

indices = np.zeros(( NUM_VERTS, 6 ))
vertices = np.zeros(( NUM_VERTS, 3 ))
uvs = np.zeros(( NUM_VERTS, 2 ))
normals = np.zeros(( NUM_VERTS * 2, 3 ))
powarr = np.array([2,2])
powind = np.array([0,2])
print normals.shape
print uvs.shape
for i in range( 0, NUM_VERTS):
    p = i % NUM_POINTS
    pp = (p+1)%NUM_POINTS
    r = i / NUM_POINTS
    rr = (r+1)%NUM_ROTATIONS
    #Triangle 1
    print r,p
    T1 = np.array([ shape3d[r, p, :], shape3d[r, pp, :], shape3d[rr, p, :] ])
    nT1 = np.cross(T1[1,:]-T1[0,:], T1[2,:]-T1[0,:])

    #Triangle 2
    T2 = np.array([ shape3d[rr, p, :], shape3d[rr ,pp ,:], shape3d[r ,pp ,:] ])
    nT2 = np.cross(T2[1,:]-T2[0,:], T2[2,:]-T2[0,:])
    #print T1,nT1/np.linalg.norm(nT1)
    #print T2,-nT2/np.linalg.norm(nT2)
    normals[i*2, :] = nT1
    normals[i*2+1, :] = nT2

    #indices and point value calculations
    tp = shape3d[r, p, :] #this point
    vertices[i,:] = tp
    #theta = np.sqrt( np.power( tp[powind], powarr ).sum())
    #theta = np.tan(tp[2],
    theta = (np.arctan2(tp[2], tp[0]) / np.pi) / 2 + .5
    uvs[i, :] = np.array([theta, tp[1] ])  # theta, z decomposition, actually theta(xz), y decomp in 
    indices[i,:] = np.array([
        i, 
        (i+1)%NUM_VERTS, 
        (NUM_ROTATIONS+i)%NUM_VERTS, 
        (NUM_ROTATIONS+i)%NUM_VERTS, 
        (NUM_ROTATIONS + i + 1)%NUM_VERTS,
        ( i + 1 ) % NUM_VERTS 
    ])


print np.around(vertices, 4)
print np.around(uvs, 4)


# print np.reshape(shape3d, (NUM_POINTS*NUM_ROTATIONS, 3))

# plt.plot_surface(shape3d[:,0],shape3d[:,1],shape3d[:,2])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(shape3d[:,0],shape3d[:,2],shape3d[:,1], rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)

# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()

# with open("./3dout.csv",'wb+') as csvfile:
#     shape3dlist = shape3d.tolist()
#     csvwriter = csv.writer(csvfile)
#     for item in shape3dlist:
#         csvwriter.writerow(item)

#indices = [] 
#vertices = shape3d
#normals = []
#uvs = [] 

metadata = {
        "version"       : 1,
        "type"          : "Geometry",
        "generatedBy"   : "Karl Bayer's 3d.py",
        "vertices"      : NUM_VERTS,
        "faces"         : NUM_VERTS*6,
        "normals"       : NUM_VERTS*6,
        "colors"        : 0,
        "uvs"           : [NUM_VERTS*6],
        "materials"     : 0,
        "morphTargets"  : 0,
        "bones"         : 0
}
    
obj = {"metadata":metadata, 
       "faces": indices.reshape(NUM_POINTS*NUM_ROTATIONS*3*2, 1).tolist(),
       "vertices": vertices.reshape((NUM_POINTS*NUM_ROTATIONS*3, 1)).tolist(),
       "normals": normals.reshape((NUM_POINTS*NUM_ROTATIONS*2*3, 1)).tolist(),
       "uvs": [uvs.reshape((NUM_POINTS*NUM_ROTATIONS*2, 1)).tolist()]
       }

FILEPATH = "C:/Users/Kbayer/Source/Repos/PotteryOnline/mythree.js/examples/models/json/"
FILENAME = "shape3d.json"
with open(FILEPATH+FILENAME, 'w+') as file:
    json.dump(obj, file)

    

