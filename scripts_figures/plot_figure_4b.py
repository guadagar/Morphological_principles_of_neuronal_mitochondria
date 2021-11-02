import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import os,glob
import csv
from sklearn.cluster import KMeans
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
from matplotlib import ticker

''''
This script was used to plot figure 4c of the paper.
GCG
30.07.21
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 5,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.8)}

mpl.rcParams.update(params)
name = []
v_om = []
s_om = []
sf = []
v_ibmc = []
s_ibmc = []
v_cm = []
s_cm =[]
cjs = []
loc = []
v_im = []
s_im = []
c_k1_150 = []
c_k1_100 = []
l =[]
r = []
loc =[]
cluster =[]

with open('data_last.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        name.append(row[0])
        loc.append(row[11])
        v_om.append(np.float(row[1]))
        s_om.append(np.float(row[2]))
        sf.append(np.float(row[14]))
        cjs.append(np.float(row[10]))
        v_im.append(np.float(row[3]))
        s_im.append(np.float(row[4]))
        v_ibmc.append(np.float(row[6]))
        s_ibmc.append(np.float(row[7]))
        v_cm.append(np.float(row[9]))
        s_cm.append(np.float(row[8]))
        l.append(np.float(row[12]))
        r.append(np.float(row[13]))
        cluster.append(np.float(row[24]))

f = open('om_k1_mean.txt','w')

m =[]
sfm = []
vomm = []
std = []
som = []
r_om = []
l_om = []
lin = []
lin1 = []
locl = []
nameo = []
cl = []
cjsf = []
folder_path = './curvature_om'

for filename in glob.glob(os.path.join(folder_path,'smooth_k1_*')):
    k1 = pickle.load(open(filename,'rb'))

    x = filename.split('/')
    #print(x)
    namec = x[2].split('_')[3]
    f.write(namec)
    f.write('\t')
    f.write(str(np.mean(k1)))
    f.write('\t')
    f.write(str(np.std(k1)))
    f.write('\t')
    f.write(str(np.median(k1)))
    f.write('\t')
    f.write(str(sf[name.index(namec)]))
    f.write('\n')

    if namec in lin:
        continue
    else:
        nameo.append(namec)
        m.append(float(np.mean(k1)))
        std.append(np.std(k1)/np.mean(k1))
        sfm.append(np.round(float(sf[name.index(namec)]),decimals=2))
        vomm.append(np.round(float(v_om[name.index(namec)]),decimals=4))
        som.append(np.round(float(s_om[name.index(namec)]),decimals=4))
        r_om.append(np.round(float(r[name.index(namec)]),decimals=4))
        l_om.append(np.round(float(l[name.index(namec)]),decimals=4))
        locl.append(loc[name.index(namec)])
        cl.append(cluster[name.index(namec)])
        cjsf.append(float(cjs[name.index(namec)]))

asfm = np.array(sfm)
am = np.array(m)
avomm = np.array(vomm)
asomm = np.array(som)
aromm = np.array(r_om)
alomm = np.array(l_om)
acl = np.array(cl)

fig, ax = plt.subplots(1,1)

for i,j in enumerate(avomm):
    if locl[i] == 'Axonal':
        ax.scatter(asfm[i],alomm[i], s=10, color = 'b', marker = 's')
    else:
        ax.scatter(asfm[i],alomm[i], s=10, color = 'r', marker = 'o')

class ScalarFormatterClass(ScalarFormatter):
   def _set_format(self):
      self.format = "%1.2f"
ax = plt.gca()
yScalarFormatter = ScalarFormatterClass(useMathText=True)
yScalarFormatter.set_powerlimits((0,0))
ax.yaxis.set_major_formatter(yScalarFormatter)


circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="r",mec='r')
circ1 = Line2D([0], [0], linestyle="none", marker="s",  markersize=3, markerfacecolor="b",mec='b')
plt.legend((circ1, circ2), ("Axonal","Presynaptic"), numpoints=1, loc="upper left", frameon = True)
#plt.ylim(0,0.2)
plt.xlim(1,4.5)
ax.set_xticks([1,2,3,4])

plt.xlabel(r'Aspect ratio (L/D)')
#plt.ylabel(r'Radius ($\mu$m)')
plt.ylabel(r'Length ($\mu$m)')

#plt.savefig('ar_vs_length.png',bbox_inches='tight',dpi = 600)
plt.show()
