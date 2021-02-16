import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

data = np.loadtxt("data.txt")

E1 = np.empty(10)
E2 = np.empty(10)
E3 = np.empty(10)
v3 = np.empty(10)
v2 = np.empty(10)
v1 = np.empty(10)
v1e = np.empty(10)
v2e = np.empty(10)
v3e = np.empty(10)

for i in range(0,10):
    E1[i] = data[i][5]

for i in range(0,10):
    E2[i] = data[i+10][5]

for i in range(0,10):
    E3[i]=data[i+20][5]

for i in range(0,10):
    v1[i]=data[i][3]

for i in range(0,10):
    v2[i] = - data[i+10][3]

for i in range(0,10):
    v3[i] = data[i+20][3]

for i in range(0,10):
    v1e[i] = data[i][10]

for i in range(0,10):
    v2e[i] = data[i+10][10]

for i in range(0,10):
    v3e[i] = data[i+20][10]


def linearF(x,slope,intercept):
    y = slope*x +intercept
    return y


wf1,co1 = cf(linearF,E1,v1,sigma = v1e)
wf2,co2 = cf(linearF,E2,v2,sigma = v2e)
wf3,co3 = cf(linearF,E3,v3,sigma = v3e)

plt.errorbar(E1,v1,v1e,fmt = 'o',markersize = 5,linewidth=1.8,markeredgecolor = 'khaki',capsize = 5,label="droplet 1")
plt.errorbar(E2,v2,v2e,fmt = 'o',markersize = 5,linewidth=1.8,markeredgecolor = 'khaki',capsize = 5,label="droplet 2")
plt.errorbar(E3,v3,v3e,fmt = 'o',markersize = 5,linewidth=1.8,markeredgecolor = 'mediumaquamarine',capsize = 5,label="droplet 3")

fitf1 = np.poly1d(wf1)
fitf2 = np.poly1d(wf2)
fitf3 = np.poly1d(wf3)

plt.plot(xx1, xx1*wf1[0]+wf1[1], color='khaki')
plt.plot(xx1, xx1*wf2[0]+wf2[1], color='mediumaquamarine')
plt.plot(xx1, xx1*wf3[0]+wf3[1], color='lightpink')
plt.legend()
plt.xlabel("Electric field strength(N/C)")
plt.ylabel("Terminal velocity(m/s)")
plt.title("Terminal velocities at varied E's for three different oil droplets")
plt.savefig("lab2fig2.pdf")


print("Oil droplet 1's v_terminal vs. elecric field strength graph has a weighted linear fit slope",wf1[0],"and intercept",wf1[1],".")


print("Oil droplet 2's v_terminal vs. elecric field strength graph has a weighted linear fit slope",wf2[0],"and intercept",wf2[1],".")


print("Oil droplet 3's v_terminal vs. elecric field strength graph has a weighted linear fit slope",wf3[0],"and intercept",wf3[1],".")


print("droplet1's slope uncertainty is:",np.sqrt(co1[0][0]),", intercept uncertainty is:",np.sqrt(co1[1][1]),".")


print("droplet2's slope uncertainty is:",np.sqrt(co2[0][0]),", intercept uncertainty is:",np.sqrt(co2[1][1]),".")


print("droplet3's slope uncertainty is:",np.sqrt(co3[0][0]),", intercept uncertainty is:",np.sqrt(co3[1][1]),".")


slopeuncertainties = np.array([np.sqrt(co1[0][0]),np.sqrt(co2[0][0]),np.sqrt(co3[0][0])])
interceptuncertainties = np.array([np.sqrt(co1[1][1]),np.sqrt(co2[1][1]),np.sqrt(co3[1][1])])
rs = np.array([1.034*10**(-6),0.68914*10**(-6),0.67446*10**(-6)])
r_uncertainties = np.empty(3)
qs = np.array([4.79777*10**(-19),1.65127*10**(-19),3.3635*10**(-19)])
q_uncertainties = np.empty(3)
slopes = np.array([wf1[0],wf2[0],wf3[0]])
intercepts = np.array([-wf1[1],-wf2[1],-wf3[1]])


sixpieta = 3.4456988*10**(-4)

thelot = 4.644741*10**(-5)

r_uncertainties = thelot*interceptuncertainties/np.sqrt(intercepts)


q_uncertainties = np.sqrt((sixpieta*rs*slopeuncertainties)**2+(sixpieta*r_uncertainties*slopes)**2)


secondlot = 119788.6150


v_f = np.empty(10)
r = np.empty(10)
E = np.empty(10)
q = np.empty(10)
dr = np.empty(10)
dq = np.empty(10)
dE = 5
dv_f = np.empty(10)


for i in range(0,10):
    v_f[i] = data[i+30][3]

for i in range(0,10):
    dv_f[i] = data[i+30][10]

for i in range(0,10):
    E[i] = data[i+30][5]

r = thelot*2*np.sqrt(v_f)
q = secondlot*r**3/E

dr = thelot*dv_f/np.sqrt(v_f)

dq = np.sqrt((secondlot*r**2*dr/E)**2+(secondlot*r**3*dE/(3*E**2))**2)

plt.errorbar(rs,qs,q_uncertainties,fmt = 'o',markersize = 5,linewidth=1.8,markeredgecolor = 'lightgrey',capsize = 5)
plt.errorbar(r,q,dq,fmt = 'o',markersize = 5,linewidth=1.8,markeredgecolor = 'lightgrey',capsize = 5)
plt.title("charges q & $\Delta$q vs. radii of oil droplets")
plt.xlabel("radius(m)")
plt.ylabel("charge(C)")
plt.savefig("lab2fig3.pdf")
