
# import json 
# with open('tree.json', 'r') as f
#     j = json.load(f)

def recurs(obj, depth):
    for key,value in obj.iteritems():
        print "\t"*depth+key,
        if type(value) == dict:
            print 'recursing'
            recurs(value,depth+1)
        else:
            if type(value) == list:
                print len(value)
            else:
                print value

recurs(j,0)
            

# morphColors 0
# scale 1.0
# morphTargets 0
# uvs 1
# vertices 1245
# colors 0
# materials 1
# faces 8360
# normals 4908
# metadata 	recursing
#   uvs 1498
# 	colors 0
# 	generatedBy OBJConverter
# 	sourceFile tree_triangles.obj
# 	vertices 415
# 	formatVersion 3
# 	materials 0
# 	normals 1636
# 	faces 760 

# faces/11 = numfaces
# normals/3 = numnormas
# vertices/2 = numvertices
# uvs/2 = numuvs

# should be 4 normals per face