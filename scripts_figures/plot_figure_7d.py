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
This script was used to plot figure 7d and generate table 2
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
k80 = []
l = []
r = []
cluster = []
nc = []

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
        cjs.append(np.float(row[10])) #nr of cjs
        v_im.append(np.float(row[3]))
        s_im.append(np.float(row[4]))
        v_ibmc.append(np.float(row[6]))
        s_ibmc.append(np.float(row[7]))
        v_cm.append(np.float(row[9]))
        s_cm.append(np.float(row[8]))
        k80.append(np.float(row[18]))
        s_ibm.append(np.float(row[5]))
        cluster.append(np.float(row[24])) #cluster nr
        nc.append(np.float(row[25])) #cristae components

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
        ncf.append(nc[name.index(namec)])


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
anc = np.array(ncf) #crista components


l_indices = np.where(acl==0)
g_indices = np.where(acl==1)

x1 = avim[l_indices[:]]/avom[l_indices]
x1a = avim[g_indices]/avom[g_indices]

x2 = avcm[l_indices]/avom[l_indices]
x2a = avcm[g_indices]/avom[g_indices]

x3 = (avom[l_indices] - avibmc[l_indices])/avom[l_indices]
x3a = (avom[g_indices] - avibmc[g_indices])/avom[g_indices]

x4 = (ascm[l_indices] )/asom[l_indices]
x4a = (ascm[g_indices])/asom[g_indices]

x5 = (asibm[l_indices])/asom[l_indices]
x5a = (asibm[g_indices])/asom[g_indices]

x6 = ancjs[l_indices]
x6a = ancjs[g_indices]

x7 = (ancjs[l_indices])/asom[l_indices]
x7a = (ancjs[g_indices])/asom[g_indices]

x8 =  np.sqrt((asibmc[l_indices] - asibm[l_indices])/(ancjs[l_indices]*np.pi))
x8a = np.sqrt((asibmc[g_indices] - asibm[g_indices])/(ancjs[g_indices]*np.pi))

x9 = (ascm[l_indices])/avcm[l_indices]
x9a = (ascm[g_indices])/avcm[g_indices]

x10 = (ascm[l_indices])/avom[l_indices]
x10a = (ascm[g_indices])/avom[g_indices]


# Table 2 in the paper
print('cjs/som',np.round(np.mean(x7),decimals=3),np.round(np.mean(x7a),decimals=3),np.round(np.std(x7),decimals=3),np.round(np.std(x7a),decimals=3),np.round(stats.ks_2samp(x7,x7a)[1],decimals=3))
print('Shape factor',np.round(np.mean(x9),decimals=3), np.round(np.mean(x9a),decimals=3),np.round(np.std(x9),decimals=3),np.round(np.std(x9a),decimals=3), np.round(stats.ks_2samp(x9,x9a)[1],decimals=3))
print('den cm',np.round(np.mean(x10),decimals=3), np.round(np.mean(x10a),decimals=3),np.round(np.std(x10),decimals=3),np.round(np.std(x10a),decimals=3), np.round(stats.ks_2samp(x10,x10a)[1],decimals=3))
print('vim/vom',np.round(np.mean(x1),decimals=3), np.round(np.mean(x1a),decimals=3),np.round(np.std(x1),decimals=3),np.round(np.std(x1a),decimals=3),np.round(stats.ks_2samp(x1,x1a)[1],decimals=3))
print('vims/vom',np.round(np.mean(x3),decimals=3), np.round(np.mean(x3a),decimals=3),np.round(np.std(x3),decimals=3),np.round(np.std(x3a),decimals=3),np.round(stats.ks_2samp(x3,x3a)[1],decimals=3))
print('vcm/vom',np.round(np.mean(x2),decimals=3), np.round(np.mean(x2a),decimals=3),np.round(np.std(x2),decimals=3),np.round(np.std(x2a),decimals=3),np.round(stats.ks_2samp(x2,x2a)[1],decimals=3))
print('sibm/som',np.round(np.mean(x5),decimals=3), np.round(np.mean(x5a),decimals=3),np.round(np.std(x5),decimals=3),np.round(np.std(x5a),decimals=3),np.round(stats.ks_2samp(x5,x5a)[1],decimals=3))
print('scm/som',np.round(np.mean(x4),decimals=3), np.round(np.mean(x4a),decimals=3),np.round(np.std(x4),decimals=3),np.round(np.std(x4a),decimals=3),np.round(stats.ks_2samp(x4,x4a)[1],decimals=3))
print('rad_cjs',np.round(np.mean(x8),decimals=5), np.round(np.mean(x8a),decimals=5),np.round(np.std(x8),decimals=5),np.round(np.std(x8a),decimals=5), np.round(stats.ks_2samp(x8,x8a)[1],decimals=5))
print('nr cjs',np.round(np.mean(x6),decimals=3), np.round(np.mean(x6a),decimals=3),np.round(np.std(x6),decimals=3),np.round(np.std(x6a),decimals=3),np.round(stats.ks_2samp(x6,x6a)[1],decimals=3))



plt.plot(asfm[l_indices],x9,'o', color='y',markersize='3')
plt.plot(asfm[g_indices],x9a,'s',color='k',markersize='3')


circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="y",mec='y')
circ2 = Line2D([0], [0], linestyle="none", marker="s",  markersize=3, markerfacecolor="k",mec='k')
#circ3 = Line2D([0], [0], linestyle="none", marker="h",  markersize=3, markerfacecolor="k",mec='k')
plt.legend((circ1, circ2), ("Globular","Elongated"), numpoints=1, loc="upper right", frameon = True)

plt.errorbar(np.mean(asfm[l_indices]),np.mean(x9),xerr=np.std(asfm[l_indices]),yerr=np.std(x9) ,color='y',marker='s')
plt.errorbar(np.mean(asfm[g_indices]),np.mean(x9a),xerr=np.std(asfm[g_indices]),yerr=np.std(x9a) ,color='k',marker='s')

plt.xlim(1,4.5)
plt.xlabel('Aspect ratio (L/D)')
plt.ylabel(r'Crista shape factor ($\mu m^{-1}$)')
#plt.ylabel(r'# of CJs / OM surface area ($\mu m^2$)')
#plt.ylabel(r'Compartment SA / OM area ($\mu m^2$) ')

#plt.ylabel('Mean first principal curvature (k1) of the IM')
#plt.savefig('mk1_im_cjs.png')
#plt.savefig('csf_vs_ar_cl.png',transparent=True,bbox_inches='tight',dpi = 600)
plt.show()
