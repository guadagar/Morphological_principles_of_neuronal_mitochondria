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
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter,AutoMinorLocator
from matplotlib import ticker

''''
This script was used to plot part of figure 4b
GCG
07.09.21
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
l =[]
r = []
loc =[]
cluster =[]
g = []
with open('data_last.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        name.append(row[0])
        loc.append(row[11])
        v_om.append(np.float(row[1]))
        s_om.append(np.float(row[2]))
        sf.append(np.float(row[14]))
        g.append(np.float(row[15]))
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
gf = []
folder_path = './curvature_om'
#bins = np.arange(-5e2, 5e2,1)

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
        gf.append(float(g[name.index(namec)]))

asfm = np.array(sfm)
am = np.array(m)
avomm = np.array(vomm)
asomm = np.array(som)
aromm = np.array(r_om)
alomm = np.array(l_om)
acl = np.array(cl)
agf = np.array(gf)
acjsf = np.array(cjsf)
print(np.corrcoef(gf,acjsf))
slope, intercept, r_value, p_value, std_err = stats.linregress((gf),(acjsf))
print('r2',r_value**2)
fig, ax = plt.subplots(1,1)

for i,j in enumerate(avomm):
    if locl[i] == 'Axonal':
        ax.scatter(avomm[i],asomm[i], s=10, color = 'b', marker = 's',zorder =100)
    else:
        ax.scatter(avomm[i],asomm[i], s=10, color = 'r', marker = 'o',zorder =100)

circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="r",mec='r')
circ1 = Line2D([0], [0], linestyle="none", marker="s",  markersize=3, markerfacecolor="b",mec='b')
plt.legend((circ1, circ2), ("Axonal","Presynaptic"), numpoints=1, loc="upper left", frameon = True)

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(avomm),np.log(asomm))
print(r_value**2,slope,np.exp(intercept),p_value)
a1 = np.exp(intercept)
b1 = slope
ax.plot(avomm, a1*(avomm**b1),'-',color='k',zorder=1)

yText1 = r'y = %.2f * x$^{%.2f}$' %(np.round(intercept,decimals=2),np.round(slope,decimals=2))
yText2 = r'$R^2$ = %.2f' %(np.round(r_value,decimals=2))
plt.text(1.5e-2,2e-1, yText1, fontsize=6,color='k')
plt.text(1.5e-2,1.8e-1, yText2, fontsize=6,color='k')


#plt.xlim(0.004,0.05)
#ax.autoscale(False)

ax.set_yscale('log')
ax.set_xscale('log')

ax = plt.gca()

ax.set_yticks([2e-1,3e-1,4e-1, 5e-1,6e-1,7e-1,8e-1])
ax.set_xticks([0.5e-2,1e-2,2e-2, 5e-2])

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,2))
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter)


plt.xlabel(r'OM volume ($\mu$m$^3$)')
plt.ylabel(r'OM surface area ($\mu$m$^2$)')

#plt.savefig('OM_vol_SA.png',bbox_inches='tight',dpi = 600)
plt.show()

#print('vo:',np.mean(avomm[l_indices]), np.mean(avomm[g_indices]),np.std(avomm[l_indices]),np.std(avomm[g_indices]),stats.ks_2samp(avomm[l_indices],avomm[g_indices])[1])
#print('so:',np.mean(asomm[l_indices]), np.mean(asomm[g_indices]),np.std(asomm[l_indices]),np.std(asomm[g_indices]),stats.ks_2samp(asomm[l_indices],asomm[g_indices])[1])
#print('r:',np.mean(2*aromm[l_indices]), np.mean(2*aromm[g_indices]),np.std(2*aromm[l_indices]),np.std(2*aromm[g_indices]),stats.ks_2samp(aromm[l_indices],aromm[g_indices])[1])
#print('l:',np.mean(alomm[l_indices]), np.mean(alomm[g_indices]),np.std(alomm[l_indices]),np.std(alomm[g_indices]),stats.ks_2samp(alomm[l_indices],alomm[g_indices])[1])
#print('ar:',np.mean(asfm[l_indices]), np.mean(asfm[g_indices]),np.std(asfm[l_indices]),np.std(asfm[g_indices]),np.round(stats.ks_2samp(asfm[l_indices],asfm[g_indices])[1],decimals=3))
#print('k1:',np.mean(am[l_indices]),np.mean(am[g_indices]),np.std(am[l_indices]),np.std(am[g_indices]),np.round(stats.ks_2samp(am[l_indices],am[g_indices])[1],decimals=3))
#print('k2:',np.mean(am[l_indices]),np.mean(am[g_indices]),np.std(am[l_indices]),np.std(am[g_indices]),np.round(stats.ks_2samp(am[l_indices],am[g_indices])[1],decimals=3))
