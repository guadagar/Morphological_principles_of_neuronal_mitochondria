import bpy
import blendgamer, numpy
import pickle

'''This script was used to select vertices with specific curvature.
CTL & GCG
07.09.21
'''

class Curvature:
    def __init__(self, algorithm, curvatureType, curveIter):
        self.algorithm = algorithm
        self.curvatureType = curvatureType
        self.curveIter = curveIter

# outside of class scope
crv1 = Curvature('MDSB', 'K1', 1)
crv2 = Curvature('MDSB', 'K2', 1)
crvg = Curvature('MDSB', 'KG', 1)
crvh = Curvature('MDSB', 'KH', 1)

smoothData1 = blendgamer.colormap.curveToData(crv1, bpy.context)
smoothData2 = blendgamer.colormap.curveToData(crv2, bpy.context)
smoothDatag = blendgamer.colormap.curveToData(crvg, bpy.context)
smoothDatah = blendgamer.colormap.curveToData(crvh, bpy.context)

npkg = smoothDatag
npkh = smoothDatah
npk1 = smoothData1

#th = np.percentile(npk1,thpercentile) #positive curvature
#th = np.percentile(npk1,thpercentile)

thg = 300
thh = 10
thk1 = 80

#k1 >150
#indices = (((thk1 < npk1))).nonzero()[0] #positive curvature

#flat-sheets J = 0 & K = 0
#indices = (((thg > abs(npkg)) & (abs(npkh) < thh))).nonzero()[0] #positive curvature

#saddles J = 0 & K ne 0
#indices = (((thh > abs(npkh)) & (abs(npkg) > thg))).nonzero()[0] #positive curvature

#cylindrical J ne 0 & K = 0
#indices = (((thg > abs(npkg)) & ((npkh) > thh))).nonzero()[0] #positive curvature

#spheres J, K ne 0
indices = (((thg <(npkg)) & ((npkh) > thh))).nonzero()[0] #positive curvature


#select the vertices with positive values
for i in indices:
   bpy.context.object.data.vertices[i].select = True
