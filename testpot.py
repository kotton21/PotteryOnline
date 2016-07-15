import rotate3D2
import PotGenerator

polyLimits = (-.1,.1,-.03,.03,-.0001,.0001)				
g = PotGenerator.PolyPotGenerator(polyLimits)
print g.numCurves,': ',[round(c,2) for poly in g for c in poly]
g.plot(True)
shape = g.zipPoints()
filename = "./mythree.js/examples/models/json/shape3d.json" 
rotate3D2.build_3d_shape_quads(shape, 20, filename)