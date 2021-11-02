import bpy
import blendgamer, numpy
import pickle

'''This script was used to save the smooth curvature of a selected object
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

nr = 7 #mito number

with open('smooth_k1_mito_'+str(nr), 'wb') as f:
    pickle.dump(smoothData1, f)

with open('smooth_k2_mito_'+str(nr), 'wb') as f:
    pickle.dump(smoothData2, f)

with open('smooth_kg_mito_'+str(nr), 'wb') as f:
    pickle.dump(smoothDatag, f)

with open('smooth_kh_mito_'+str(nr), 'wb') as f:
    pickle.dump(smoothDatah, f)
