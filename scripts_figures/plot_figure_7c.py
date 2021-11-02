import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import os,glob
import csv
from matplotlib.lines import Line2D
from sklearn.cluster import KMeans


''''
This script was used to plot figure 7c of the paper
GCG
07.30.21
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
s_ibm = []
v_cm = []
s_cm =[]
cjs = []
loc = []
v_im = []
s_im = []
l = []
r = []
cluster = []
nc = []
k80 = []

with open('data_last.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        name.append(row[0])
        v_om.append(np.float(row[1]))
        s_om.append(np.float(row[2]))
        sf.append(np.float(row[14]))
        l.append(np.float(row[12]))
        r.append(np.float(row[13]))
        cjs.append(np.float(row[10]))
        v_im.append(np.float(row[3]))
        s_im.append(np.float(row[4]))
        v_ibmc.append(np.float(row[6]))
        s_ibmc.append(np.float(row[7]))
        v_cm.append(np.float(row[9]))
        s_cm.append(np.float(row[8]))
        s_ibm.append(np.float(row[5]))
        cluster.append(np.float(row[24]))
        #nc.append(np.float(row[25]))
        #nc.append(np.float(row[25]))
        k80.append(np.float(row[20]))

f = open('im_k1_mean.txt','w')

m = []
sfm = []
vomm = []
std = []
som = []
r_om = []
l_om = []
vim = []
vcm = []
vibmc = []
sim = []
sibmc = []
scm = []
nrcjs = []
sibm =[]
gc = []
nameo = []
cl = []
ncf = []
lna_o = ['6','3','7']

folder_path = './curvature_im'
plt.figure(1)
bins = np.arange(-5e2, 5e2,1)
for filename in glob.glob(os.path.join(folder_path,'smooth_k1_*')):
    k1 = pickle.load(open(filename,'rb'))

    x = filename.split('/')
    namec = x[2].split('_')[3]
    #print(namec)
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
    if namec in lna_o:
        continue
    else:
        #print(namec)
        nameo.append(namec)
        m.append(float(np.mean(k1)))
        std.append(float(np.std(k1)/np.mean(k1)))
        sfm.append(np.round(float(sf[name.index(namec)]),decimals=2))
        vomm.append(np.round(float(v_om[name.index(namec)]),decimals=4))
        som.append(np.round(float(s_om[name.index(namec)]),decimals=4))
        r_om.append(np.round(float(r[name.index(namec)]),decimals=4))
        l_om.append(np.round(float(l[name.index(namec)]),decimals=4))
        vim.append(np.round(float(v_im[name.index(namec)]),decimals=4))
        vcm.append(np.round(float(v_cm[name.index(namec)]),decimals=4))
        vibmc.append(np.round(float(v_ibmc[name.index(namec)]),decimals=4))
        sim.append(np.round(float(s_im[name.index(namec)]),decimals=4))
        scm.append(np.round(float(s_cm[name.index(namec)]),decimals=4))
        sibmc.append(np.round(float(s_ibmc[name.index(namec)]),decimals=4))
        nrcjs.append(np.round(float(cjs[name.index(namec)]),decimals=4))
        sibm.append(np.round(float(s_ibm[name.index(namec)]),decimals=4))
        gc.append(np.round(float(k80[name.index(namec)]),decimals=4))
        cl.append(cluster[name.index(namec)])


asfm = np.array(sfm)
am = np.array(m)
astd = np.array(std)
avim = np.array(vim)
asim = np.array(sim)
avcm = np.array(vcm)
ascm = np.array(scm)
avibmc = np.array(vibmc)
asibmc = np.array(sibmc)
asibm = np.array(sibm)
avom = np.array(vomm)
asom = np.array(som)
ancjs = np.array(nrcjs)
agc = np.array(gc)
acl = np.array(cl)
anc = np.array(ncf)

l_indices = np.where(acl==0)
g_indices = np.where(acl==1)

x7 = (ancjs[l_indices])/asom[l_indices]
x7a = (ancjs[g_indices])/asom[g_indices]


plt.plot(asfm[l_indices],x7,'o', color='y',markersize='3')
plt.plot(asfm[g_indices],x7a,'s',color='k',markersize='3')


circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="y",mec='y')
circ2 = Line2D([0], [0], linestyle="none", marker="s",  markersize=3, markerfacecolor="k",mec='k')
#circ3 = Line2D([0], [0], linestyle="none", marker="h",  markersize=3, markerfacecolor="k",mec='k')
plt.legend((circ1, circ2), ("Globular","Elongated"), numpoints=1, loc="lower left", frameon = True)

plt.ylim(10,75)

plt.errorbar(np.mean(asfm[l_indices]),np.mean(x7),xerr=np.std(asfm[l_indices]),yerr=np.std(x7) ,color='y',marker='s')
plt.errorbar(np.mean(asfm[g_indices]),np.mean(x7a),xerr=np.std(asfm[g_indices]),yerr=np.std(x7a) ,color='k',marker='s')
plt.xlim(1,4.5)

plt.xlabel('Aspect ratio (L/D)')
plt.ylabel(r'# of CJs per OM surface area ($\mu m^{-2}$)')

#plt.savefig('cjs_per_om_vs_ar_cl.png',transparent=True,bbox_inches='tight',dpi = 600)
plt.show()
