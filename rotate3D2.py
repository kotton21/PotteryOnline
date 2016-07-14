import numpy as np
import json

def shift_x( SHAPE, SHIFT ):
    """
    Shifts the shape over by the specified SHIFT. 
    Returns the two shapes separately so they can
    be properly dealt with when building the final shape.
    
    """
    NUM_POINTS = len(SHAPE)

    #make nparray
    shape = np.array(SHAPE)
    shape = shape - np.array([SHIFT, 0])
    
    return shape

def rotate_3d( SHAPE, NUM_ROTATIONS ):
    """
    
    Rotates the given shape around the y axis.
    Expects SHAPE to be an n x 2 nested list
    
    """

    NUM_POINTS = len(SHAPE)
    NUM_VERTS = NUM_POINTS * NUM_ROTATIONS

    #translate to 3d
    shape = np.array(SHAPE)
    zers = np.zeros((NUM_POINTS,1))
    shape2d = np.hstack((shape, zers))

    shape3d = np.zeros(( NUM_ROTATIONS, NUM_POINTS, 3 ))

    rm = np.zeros((3,3))
    for i in range(NUM_ROTATIONS):
        theta = i*2.0*np.pi/NUM_ROTATIONS
        rm = np.array([[np.cos(theta), 0., np.sin(theta)],
                    [0., 1., 0.],
                    [-np.sin(theta), 0., np.cos(theta)]])

        shape3drot = np.dot(shape2d, rm)
        shape3d[i,:,:] = shape3drot

    #shape3d = np.round(shape3d,4)
    #print shape3d
    #print shape3d[0,:,:]
    return shape3d


def build_quad_indices( shape3d, NUM_ROTATIONS, base ):
    """

    Builds quad indexes, normals, and faces from the shape vertices
    Shape3d is a NUM_VERTICES x 3 array
    Do I want a normal for each face and for each vertice? or do I 
    want them just on the faces?
    Should be able to do this with a numpy dot product if i keep the
    num-verts constant and use the same tranformation matrix..
    
    base is the 1x5 array representing the order in which the points
    are sampled into 'faces'

    """
    NUM_POINTS = shape3d.shape[1]
    NUM_VERTS = NUM_POINTS * NUM_ROTATIONS

    faces = np.zeros(( NUM_VERTS - NUM_ROTATIONS, 5 ))
    vertices = np.zeros(( NUM_VERTS, 3 ))
    #uvs = np.zeros(( NUM_VERTS, 2 ))
    #normals = np.zeros(( NUM_VERTS * 2, 3 ))
    # powarr = np.array([2,2])
    # powind = np.array([0,2])

    base_add = np.array([0, 1, 1, 1, 1 ])

    j = 0
    for i in range(NUM_VERTS):
        #prevent wrap-around in the model:
        if (i % NUM_POINTS) != (NUM_POINTS - 1):
            #faces for each quad
            faces[j,:] = (base + (base_add * i))%NUM_VERTS
            j = j + 1
        
        #vertices for each quad
        p = i % NUM_POINTS
        r = i / NUM_POINTS

        vertices[i,:] = shape3d[r, p, :]
    return (faces, vertices)


def build_triangle_indices( shape3d, NUM_ROTATIONS ):
    """

    Builds the indexes, normals, and faces from the shape vertices
    Also, why? just provide the qNUM_VERTSuads

    """

    #print SHAPE.shape
    NUM_POINTS = shape3d.shape[1]
    NUM_VERTS = NUM_POINTS * NUM_ROTATIONS
    
    indices = np.zeros(( NUM_VERTS, 8 ))
    vertices = np.zeros(( NUM_VERTS, 3 ))
    uvs = np.zeros(( NUM_VERTS, 2 ))
    normals = np.zeros(( NUM_VERTS * 2, 3 ))
    powarr = np.array([2,2])
    powind = np.array([0,2])
    # print normals.shape
    # print uvs.shape
    for i in range( 0, NUM_VERTS):
        p = i % NUM_POINTS
        pp = (p+1)%NUM_POINTS
        r = i / NUM_POINTS
        rr = (r+1)%NUM_ROTATIONS
    
        #Triangle 1
        #print "\n\n",r,p
        T1 = np.array([ shape3d[r, p, :], shape3d[r, pp, :], shape3d[rr, p, :] ])
        nT1 = np.cross(T1[1,:]-T1[0,:], T1[2,:]-T1[0,:])

        #Triangle 2
        T2 = np.array([ shape3d[rr, p, :], shape3d[rr ,pp ,:], shape3d[r ,pp ,:] ])
        nT2 = np.cross(T2[1,:]-T2[0,:], T2[2,:]-T2[0,:])

        #apparently these don't matter anyway... why?
        normals[i*2, :] = nT1/np.linalg.norm(nT1)
        normals[i*2+1, :] = -nT2/np.linalg.norm(nT2)

        #indices and point value calculations
        tp = shape3d[r, p, :] #this point
        vertices[i,:] = tp
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

        # print indices[i,:]
        # print vertices[i,:]


    # print np.around(vertices, 4)
    # print np.around(uvs, 4)
    # print indices

    return ( indices, vertices, uvs, normals )



def plot_shape(shape3d):
    """

    Almost certainly not working

    """
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    import matplotlib.pyplot as plt

    # plt.plot_surface(shape3d[:,0],shape3d[:,1],shape3d[:,2])
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(shape3d[:,0],shape3d[:,2],shape3d[:,1], rstride=1, 
        cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


def export_json(filename, indices, vertices, uvs, normals):
    """

    Exports the given shape to a json file
    
    """

    NUM_VERTS = len( vertices )

    faces = indices.reshape(NUM_VERTS*3*2+(2*NUM_VERTS)).tolist()
    # print faces
    vertices = np.around(vertices, 4).reshape((NUM_VERTS*3)).tolist()
    normals = np.around(normals, 4).reshape((NUM_VERTS*2*3)).tolist()
    uvs = np.around(uvs, 4).reshape((NUM_VERTS*2)).tolist()

    #import uuid
    #materialID = uuid.uuid4()
    #geometryID = uuid.uuid4()
    #objID = uuid.uuid5(uuid.NAMESPACE_URL, "www.karlsbayer.com")

    #old uuid 

    materials = [{u'opacity': 1, u'uuid': u'7AAB18E5-FF88-4A82-8018-4DF34EDB7539', u'color': 16714940, u'wireframe': False, u'emissive': 0, u'shininess': 50, u'specular': 0, u'ambient': 16714940, u'type': u'MeshPhongMaterial', u'transparent': False}]

    metadata = {
            u"version"      : 4,
            u"type"         : u"Geometry",
            u"generator"    : u"Karl Bayer's 3d.py",
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

    # FILEPATH = "C:/Users/Kbayer/Source/Repos/PotteryOnline/mythree.js/examples/models/json/"
    # FILENAME = "shape3d.json"
    with open(filename, 'w+') as file:
        json.dump(jobj, file)

        

    print 'vertices len: ',len(vertices)
    print 'faces len: ',len(faces)
    print 'normals len: ',len(normals)
    print 'uvs len: ',len(uvs)

def build_3d_shape(SHAPE, NUM_ROTATIONS, FILENAME):
    shape3d = rotate_3d(SHAPE, NUM_ROTATIONS)
    ( indices, vertices, uvs, normals ) = build_triangle_indices( shape3d, NUM_ROTATIONS )
    export_json(FILENAME, indices, vertices, uvs, normals)
    print 'saving to "%s"'%FILENAME

def export_json_simple(filename, faces, vertices):
    """

    Exports the given shape to a json file
    
    """

    NUM_VERTS = len( vertices )

    face_size = np.prod(np.shape(faces))
    vertice_size = np.prod(np.shape(vertices))

    faces = faces.reshape( face_size ).tolist()
    # print faces
    vertices = np.around(vertices, 4).reshape(vertice_size).tolist()
    # normals = np.around(normals, 4).reshape((NUM_VERTS*2*3)).tolist()
    # uvs = np.around(uvs, 4).reshape((NUM_VERTS*2)).tolist()

    #import uuid
    #materialID = uuid.uuid4()
    #geometryID = uuid.uuid4()
    #objID = uuid.uuid5(uuid.NAMESPACE_URL, "www.karlsbayer.com")

    #old uuid 

    materials = [{u'opacity': 1, 
                  u'uuid': u'7AAB18E5-FF88-4A82-8018-4DF34EDB7539', 
                  u'color': 16712000, 
                  u'wireframe': False, 
                  u'emissive': 0, 
                  u'shininess': 50, 
                  u'specular': 0, 
                  u'ambient': 16714940, 
                  u'type': u'MeshPhongMaterial', 
                  #u'wireframe': True,
                  u'transparent': False
                  }]

    metadata = {
            u"version"      : 4,
            u"type"         : u"Geometry",
            u"generator"    : u"Karl Bayer's 3d.py",
    }

    data = {
        u"faces": faces,
        u"vertices": vertices
        }   
    geometries = [{u"data":data, u"uuid": u'15930b1c-1b50-4926-a0ac-df433b9c4f96', u"type":u"Geometry"}]
    obj = {u'uuid': u'0D4F494E-35AD-4D5B-9696-7DF60B73E7F0', u'geometry': u'15930b1c-1b50-4926-a0ac-df433b9c4f96', u'material': 
        u'7AAB18E5-FF88-4A82-8018-4DF34EDB7539', u'matrix': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], u'castShadow': True,
        u'type': u'Mesh', u'receiveShadow': True, u'name': u'shape3d001'
        }
    jobj = {u'object':obj, u'materials':materials, u'geometries':geometries, u'metadata':metadata}

    # FILEPATH = "C:/Users/Kbayer/Source/Repos/PotteryOnline/mythree.js/examples/models/json/"
    # FILENAME = "shape3d.json"
    with open(filename, 'w+') as file:
        json.dump(jobj, file)

    print 'vertices len: ',len(vertices)
    print 'faces len: ',len(faces)

def build_3d_shape_quads(SHAPE, NUM_ROTATIONS, FILENAME):
    NUM_POINTS = len(SHAPE)
    #NUM_VERTS = NUM_POINTS * NUM_ROTATIONS
    baseCW = np.array([1, 0, 1, NUM_POINTS+1, NUM_POINTS ])
    baseCCW = np.array([1, 0, NUM_POINTS, NUM_POINTS+1, 1  ])

    shape3d_out = rotate_3d(SHAPE, NUM_ROTATIONS)
    shape3d_in = rotate_3d(shift_x(SHAPE, .1), NUM_ROTATIONS)

    ( faces_out, vertices_out ) = build_quad_indices( shape3d_out, NUM_ROTATIONS, baseCW)
    ( faces_in, vertices_in ) = build_quad_indices( shape3d_in, NUM_ROTATIONS, baseCCW )

    off = np.shape(faces_out)[0]
    faces_in_offset =  np.array([0,off,off,off,off])#np.prod(np.shape(faces_out))

    #print vertices_out.shape
    #print faces_out.shape
    #print faces_in_offset
    #print (faces_in + faces_in_offset)[0,0]
    faces = np.vstack((faces_out, faces_in + faces_in_offset ))
    vertices = np.vstack((vertices_out, vertices_in))
    export_json_simple(FILENAME, faces, vertices )
    #print faces, vertices
    print 'saving to "%s"'%FILENAME


if __name__ == "__main__":
    SHAPE = [
        [1,0],
        [2,1],
        [2.1,2],
        [3,3]]
    #SHAPE = [
    #	[3, 3],
    #	[2.1, 2],
    #	[2, 2],
    #	[1, 0]]



    NUM_ROTATIONS = 20
    
    filename = "./mythree.js/examples/models/json/shape3d3.json"
    print 'saving to %s'%filename
    build_3d_shape_quads(SHAPE, NUM_ROTATIONS, filename)