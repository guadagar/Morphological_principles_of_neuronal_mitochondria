#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import csv
import pandas as pd
from scipy import stats
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
from matplotlib.lines import Line2D
import matplotlib as mpl
from matplotlib import ticker

'''
This script reads the file data_final.cvs and plots the values in Table 3
and generates the figure 10c in the paper.
GCG
07.13.21
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 5,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.8)}

mpl.rcParams.update(params)

name = []
vom = []
flat =[]
cat = []
sp = []
cyl = []
k1_80 = []
tot = []
scm = []
sf = []
cjs = []
s_ibm = []
cluster = []
som = []
sim = []
im_g = []

with open('data_last.csv', 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        name.append(row[0])
        vom.append(np.float(row[1]))
        som.append(np.float(row[2]))
        sim.append(np.float(row[4]))
        flat.append(np.float(row[16]))
        sp.append(np.float(row[17]))
        cat.append(np.float(row[18]))
        cyl.append(np.float(row[19]))
        k1_80.append(np.float(row[20]))
        tot.append(np.float(row[21]))
        #scm.append(np.float(row[21]))
        sf.append(np.float(row[14]))
        cjs.append(np.float(row[10]))
        s_ibm.append(np.float(row[5]))
        cluster.append(np.float(row[24]))
        im_g.append(np.float(row[15])) #genus


af = np.array(flat)
asp = np.array(sp)
acat = np.array(cat)
acyl = np.array(cyl)
ak1 = np.array(k1_80)
atot= np.array(tot)
acjs = np.array(cjs)
asibm = np.array(s_ibm)
avom = np.array(vom)
asf = np.array(sf)
acl = np.array(cluster)
asom = np.array(som)
asim = np.array(sim)
aim_g =np.array(im_g)
namec = np.array(name)

l_indices = (((acl==0) & (af!=0))).nonzero()[0]
g_indices = (((acl==1) & (af!=0))).nonzero()[0]


x1 = (100*af[l_indices])/atot[l_indices]
x1a = (100*af[g_indices])/atot[g_indices]

x2 = (100*asp[l_indices])/atot[l_indices]
x2a = (100*asp[g_indices])/atot[g_indices]

x3 = (100*acat[l_indices])/atot[l_indices]
x3a = (100*acat[g_indices])/atot[g_indices]

x4 = (100*acyl[l_indices])/atot[l_indices]
x4a = (100*acyl[g_indices])/atot[g_indices]

x5 = (100*ak1[l_indices])/asom[l_indices]
x5a = (100*ak1[g_indices])/asom[g_indices]

x7 = (aim_g[l_indices])
x7a = (aim_g[g_indices])
#print('atot',atot[l_indices])
#Table 3 in the paper
print('f',np.round(np.mean(x1),decimals=2), np.round(np.mean(x1a),decimals=2),np.round(np.std(x1),decimals=2), np.round(np.std(x1a),decimals=2),stats.ks_2samp(x1,x1a)[1])
print('cat',np.round(np.mean(x3),decimals=2), np.round(np.mean(x3a),decimals=2),np.round(np.std(x3),decimals=2), np.round(np.std(x3a),decimals=2),stats.ks_2samp(x3,x3a)[1])
print('cyl',np.round(np.mean(x4),decimals=2), np.round(np.mean(x4a),decimals=2),np.round(np.std(x4),decimals=2), np.round(np.std(x4a),decimals=2),stats.ks_2samp(x4,x4a)[1])
print('s',np.round(np.mean(x2),decimals=2), np.round(np.mean(x2a),decimals=2),np.round(np.std(x2),decimals=2), np.round(np.std(x2a),decimals=2),stats.ks_2samp(x2,x2a)[1])
print('k1',np.round(np.mean(x5),decimals=2), np.round(np.mean(x5a),decimals=2),np.round(np.std(x5),decimals=2), np.round(np.std(x5a),decimals=2),stats.ks_2samp(x5,x5a)[1])
#print('k1_sa/omvol',np.round(np.mean(x5),decimals=2), np.round(np.mean(x5a),decimals=2),np.round(np.std(x5),decimals=2), np.round(np.std(x5a),decimals=2),stats.ks_2samp(x5,x5a)[1])

#Figure 7
fig, ax = plt.subplots(1,1)

plt.ylim(0,18)
plt.plot(asf[l_indices],x5, 'o', color='y',markersize='3')
plt.plot(asf[g_indices], x5a, 's', color='k',markersize='3')

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="y",mec='y')
circ2 = Line2D([0], [0], linestyle="none", marker="s",  markersize=3, markerfacecolor="k",mec='k')
plt.legend((circ1, circ2), ("Globular","Elongated"), numpoints=1, loc="upper right", frameon = True)
tick_spacing = 3
ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.ylim(0,18)
plt.xlim(1,4.5)
plt.xlabel('Aspect ratio (L/D)')
plt.ylabel('CM SA with k1 > 80 $\mu m^{-1}$ / OM SA')
#plt.savefig('rat_sa_k1_sa_vs_ar.png',transparent=True,bbox_inches='tight',dpi = 600)
#plt.legend()
plt.show()
