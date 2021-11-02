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

'''This script was used to generate figure 6b, and to calculate the values in Table 1
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
v_cm = []
s_cm =[]
cjs = []
loc = []
v_im = []
s_im = []
c_k1_150 = []
c_k1_100 = []
l = []
r = []
loc = []
cluster = []
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

m = []
sfm = []
vomm = []
std = []
som = []
r_om = []
l_om = []
lin = []
lin1 =[]
locl = []
nameo = []
cl = []
cjsf = []
folder_path = './curvature_om'

for filename in glob.glob(os.path.join(folder_path,'smooth_k2_*')):
    k1 = pickle.load(open(filename,'rb'))

    x = filename.split('/')
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
        #print(namec,np.mean(k1))

asfm = np.array(sfm)
am = np.array(m)
avomm = np.array(vomm)
asomm = np.array(som)
aromm = np.array(r_om)
alomm = np.array(l_om)
acl = np.array(cl)

l_indices = np.where(acl==0)
g_indices = np.where(acl==1)

#print(avomm[l_indices])
#print(avomm[g_indices])

print('vo:',np.round(np.mean(avomm[l_indices]),decimals=3), np.round(np.mean(avomm[g_indices]),decimals=3),np.round(np.std(avomm[l_indices]),decimals=3),np.round(np.std(avomm[g_indices]),decimals=3),np.round(stats.ks_2samp(avomm[l_indices],avomm[g_indices])[1],decimals=3))
print('so:',np.round(np.mean(asomm[l_indices]),decimals=3), np.round(np.mean(asomm[g_indices]),decimals=3),np.round(np.std(asomm[l_indices]),decimals=3),np.round(np.std(asomm[g_indices]),decimals=3),np.round(stats.ks_2samp(asomm[l_indices],asomm[g_indices])[1],decimals=3))
print('r:',np.round(np.mean(2*aromm[l_indices]),decimals=3), np.round(np.mean(2*aromm[g_indices]),decimals=3),np.round(np.std(2*aromm[l_indices]),decimals=3),np.round(np.std(2*aromm[g_indices]),decimals=3),np.round(stats.ks_2samp(aromm[l_indices],aromm[g_indices])[1],decimals=3))
print('l:',np.round(np.mean(alomm[l_indices]),decimals=3), np.round(np.mean(alomm[g_indices]),decimals=3),np.round(np.std(alomm[l_indices]),decimals=3),np.round(np.std(alomm[g_indices]),decimals=3),np.round(stats.ks_2samp(alomm[l_indices],alomm[g_indices])[1],decimals=3))
print('ar:',np.round(np.mean(asfm[l_indices]),decimals=3), np.round(np.mean(asfm[g_indices]),decimals=3),np.round(np.std(asfm[l_indices]),decimals=3),np.round(np.std(asfm[g_indices]),decimals=3),np.round(stats.ks_2samp(asfm[l_indices],asfm[g_indices])[1],decimals=3))
print('k1:',np.round(np.mean(am[l_indices]),decimals=3),np.round(np.mean(am[g_indices]),decimals=3),np.round(np.std(am[l_indices]),decimals=3),np.round(np.std(am[g_indices]),decimals=3),np.round(stats.ks_2samp(am[l_indices],am[g_indices])[1],decimals=3))


#fig = plt.figure(2, figsize=(4, 3))
#ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

fig, ax = plt.subplots()

for i in range(0,len(avomm)):
    #print(lab[i])
    if acl[i]==0:
        ax.scatter(asfm[i],m[i],marker='o',color='y')
        print(asfm[i])
    else:
        ax.scatter(asfm[i],m[i],marker='s',color='k')
        print(asfm[i])

plt.errorbar(np.mean(asfm[l_indices]),np.mean(am[l_indices]),xerr=np.std(asfm[l_indices]),yerr=np.std(am[l_indices]) ,color='y',marker='s')
plt.errorbar(np.mean(asfm[g_indices]),np.mean(am[g_indices]),xerr=np.std(asfm[g_indices]),yerr=np.std(am[g_indices]) ,color='k',marker='s')

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="y",mec='y')
circ2 = Line2D([0], [0], linestyle="none", marker="s",  markersize=3, markerfacecolor="k",mec='k')
plt.legend((circ1, circ2), ("Globular","Elongated"), numpoints=1, loc="upper right", frameon = True)

ax.set_yticks([-22,-20,-18,-16,-14,-12,-10,-8,-6,-4])


yText1 = r'px < %.3f' %(np.round(stats.ks_2samp(asfm[l_indices],asfm[g_indices])[1],decimals=3))
plt.text(1.2,-6.3, yText1, fontsize=6,color='k')
yText2 = r'py < %.3f' %(np.round(stats.ks_2samp(am[l_indices],am[g_indices])[1],decimals=3))
plt.text(1.2,-7.5, yText2, fontsize=6,color='k')
plt.ylim(-22,-5)
plt.xlim(1,4.5)
#plt.xlabel('OM volume ($\mu m^3$)')
plt.xlabel('Aspect ratio (L/D)')
#ax.set_ylabel('k1 of the OM (um)')
plt.ylabel('Average curvature (k2) of the OM')
#plt.savefig('k2_vs_ar_cluster.png',transparent=True,bbox_inches='tight',dpi = 600)
plt.show()
