
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

SHAPE = [
	[1,0],
	[2,1],
	[2.1,2],
    [3,3]]
#SHAPE = [
#	[1,0],
#	[1,1]]


NUM_ROTATIONS = 20
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

indices = np.zeros(( NUM_VERTS, 8 ))
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
    print "\n\n",r,p
    T1 = np.array([ shape3d[r, p, :], shape3d[r, pp, :], shape3d[rr, p, :] ])
    nT1 = np.cross(T1[1,:]-T1[0,:], T1[2,:]-T1[0,:])

    #Triangle 2
    T2 = np.array([ shape3d[rr, p, :], shape3d[rr ,pp ,:], shape3d[r ,pp ,:] ])
    nT2 = np.cross(T2[1,:]-T2[0,:], T2[2,:]-T2[0,:])
    #print T1,nT1/np.linalg.norm(nT1)
    #print T2,-nT2/np.linalg.norm(nT2)

    #apparently these don't matter anyway... why?
    normals[i*2, :] = nT1/np.linalg.norm(nT1)
    normals[i*2+1, :] = -nT2/np.linalg.norm(nT2)

    #indices and point value calculations
    tp = shape3d[r, p, :] #this point
    vertices[i,:] = tp
    #theta = np.sqrt( np.power( tp[powind], powarr ).sum())
    #theta = np.tan(tp[2],
    theta = (np.arctan2(tp[2], tp[0]) / np.pi) / 2 + .5
    uvs[i, :] = np.array([theta, tp[1] ])  # theta, z decomposition, actually theta(xz), y decomp in 
    indices[i,:] = np.array([0,
        i, 
        (i+1)%NUM_VERTS, 
        (NUM_POINTS+i)%NUM_VERTS, 
        0,
        (NUM_POINTS+i)%NUM_VERTS, 
        ( i + 1 ) % NUM_VERTS, 
        (NUM_POINTS + i + 1)%NUM_VERTS
    ])

    print indices[i,:]
    print vertices[i,:]


print np.around(vertices, 4)
print np.around(uvs, 4)
print indices

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

faces = indices.reshape(NUM_POINTS*NUM_ROTATIONS*3*2+(2*NUM_VERTS)).tolist()
print faces
vertices = np.around(vertices, 4).reshape((NUM_POINTS*NUM_ROTATIONS*3)).tolist()
normals = np.around(normals, 4).reshape((NUM_POINTS*NUM_ROTATIONS*2*3)).tolist()
uvs = np.around(uvs, 4).reshape((NUM_POINTS*NUM_ROTATIONS*2)).tolist()

materials = [{u'opacity': 1, u'uuid': u'7AAB18E5-FF88-4A82-8018-4DF34EDB7539', u'color': 16714940, u'wireframe': False, u'emissive': 0, u'shininess': 50, u'specular': 0, u'ambient': 16714940, u'type': u'MeshPhongMaterial', u'transparent': False}]

metadata = {
        u"version"      : 4,
        u"type"         : u"Geometry",
        u"generator"    : u"Karl Bayer's 3d-2.py",
}

data = {
       u"faces": faces,
       u"vertices": vertices,
       #u"normals": normals,
       u"uvs": [uvs]
       }   
geometries = [{u"data":data, u"uuid": u'15930b1c-1b50-4926-a0ac-df433b9c4f96', u"type":u"Geometry"}]
obj = {u'uuid': u'0D4F494E-35AD-4D5B-9696-7DF60B73E7F0', u'geometry': u'15930b1c-1b50-4926-a0ac-df433b9c4f96', u'material': 
       u'7AAB18E5-FF88-4A82-8018-4DF34EDB7539', u'matrix': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], u'castShadow': True,
       u'type': u'Mesh', u'receiveShadow': True, u'name': u'shape3d001'
       }
jobj = {u'object':obj, u'materials':materials, u'geometries':geometries, u'metadata':metadata}

FILEPATH = "C:/Users/Kbayer/Source/Repos/PotteryOnline/mythree.js/examples/models/json/"
FILENAME = "shape3d.json"
with open(FILEPATH+FILENAME, 'w+') as file:
    json.dump(jobj, file)

    

print 'vertices len: ',len(vertices)
print 'faces len: ',len(faces)
print 'normals len: ',len(normals)
print 'uvs len: ',len(uvs)