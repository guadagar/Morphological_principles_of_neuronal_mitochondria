import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import os,glob
import csv
from sklearn.cluster import KMeans
from matplotlib.lines import Line2D


'''
This script was used to separate the mitos with protrusions from those without
GCG
08.05.21
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
k80 = []
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
        k80.append(np.float(row[18]))
        l.append(np.float(row[12]))
        r.append(np.float(row[13]))
        cluster.append(np.float(row[24])) #cluster nr

f = open('om_k1_mean.txt','w')

m = []
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
folder_path = './curvature_om/'
plt.figure(1)
bins = np.arange(-5e2, 5e2,1)
for filename in glob.glob(os.path.join(folder_path,'smooth_k1_*')):
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

asfm = np.array(sfm)
am = np.array(m)
avomm = np.array(vomm)
asomm = np.array(som)
aromm = np.array(r_om)
alomm = np.array(l_om)
acl = np.array(cl)

lin1 = ['9','6','5','11']

indx = np.zeros((len(acl)))
for i,j in enumerate(asfm):
    if nameo[i] in lin1:
        indx[i] = 1
        #plt.scatter(asfm[i],am[i], s=10, color = 'b', marker = 's')
        print('lin1', nameo[i],aromm[i])
    elif nameo[i] not in lin1:
        indx[i] = 0
        #plt.scatter(asfm[i],am[i], s=10, color = 'r', marker = 'o')
        #print('Pre-syn', asfm[i],am[i], nameo[i])

l_indices = np.where(indx==0)
g_indices = np.where(indx==1)

print('vo:',np.mean(avomm[l_indices]), np.mean(avomm[g_indices]),np.std(avomm[l_indices]),np.std(avomm[g_indices]),stats.ks_2samp(avomm[l_indices],avomm[g_indices])[1])
print('so:',np.mean(asomm[l_indices]), np.mean(asomm[g_indices]),np.std(asomm[l_indices]),np.std(asomm[g_indices]),stats.ks_2samp(asomm[l_indices],asomm[g_indices])[1])
print('r:',np.mean(aromm[l_indices]), np.mean(aromm[g_indices]),np.std(aromm[l_indices]),np.std(aromm[g_indices]),stats.ks_2samp(aromm[l_indices],aromm[g_indices])[1])
print('l:',np.mean(alomm[l_indices]), np.mean(alomm[g_indices]),np.std(alomm[l_indices]),np.std(alomm[g_indices]),stats.ks_2samp(alomm[l_indices],alomm[g_indices])[1])
print('ar:',np.mean(asfm[l_indices]), np.mean(asfm[g_indices]),np.std(asfm[l_indices]),np.std(asfm[g_indices]),np.round(stats.ks_2samp(asfm[l_indices],asfm[g_indices])[1],decimals=3))
print('k1:',np.mean(am[l_indices]),np.mean(am[g_indices]),np.std(am[l_indices]),np.std(am[g_indices]),np.round(stats.ks_2samp(am[l_indices],am[g_indices])[1],decimals=3))
#print('k2:',np.mean(am[l_indices]),np.mean(am[g_indices]),np.std(am[l_indices]),np.std(am[g_indices]),np.round(stats.ks_2samp(am[l_indices],am[g_indices])[1],decimals=3))
