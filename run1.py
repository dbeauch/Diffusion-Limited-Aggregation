from scipy.integrate import solve_ivp
import numpy as np
from math import sqrt

period = 2 * np.pi / 2.4

xlist = []
plist = []

def  func(t, y):
    m = 1
    a = 0.5
    b = .25
    F0 = 2
    w = 2.4
    gama = 0.1
    x = y[0]
    v = y[1]
    f0 = y[1]
    f1 = -(gama/m)*v + 2*(a/m)*x - 4*(b/m)*x*x*x + (F0/m)*np.cos(w*t)
    return [f0,f1]

y0 = [0.5, 0]


#print("period" + str(period))
t = np.linspace(0,period,200)
#print(t)

count = 25000

for i in range(count):
    sol = solve_ivp(func, [0,period], y0, t_eval=t)
    yf = sol.y
    #print(yf)
    #for y in sol:
    #    print(y)
    print("x final: " + str(yf[0][-1]))
    print("p final: " + str(yf[1][-1]))
    xlist.append(yf[0][-1])
    plist.append(yf[1][-1])
    y0[0] = yf[0][-1]
    y0[1] = yf[1][-1]

l = 2
matricies = []
nums = []
bs = []
while l <= 128:
    fractal = [[False for _ in range(l)] for _ in range(l)]
    b = 6./float(l)
    print("b = " + str(b))
    for i in range(count):
        div1 = xlist[i]/b
        div2 = plist[i]/b
        if div1 < 0:
            div1-=1
        if div2 < 0:
            div2-=1
        xpos = int(div1) + int(l/2)
        ypos = int(div2) + int(l/2)
        #print("xpos = " + str(xpos))
        #print("ypos = " + str(ypos))
        fractal[xpos][ypos] = True
        
    fraccount = 0
    for i in range(l):
        for j in range(l):
            if fractal[i][j]:
                fraccount += 1

    print("N(b) = " + str(fraccount))
    nums.append(fraccount)
    bs.append(b)
    matricies.append(fractal)
    l *= 2


    
from matplotlib import pyplot as plt
x = np.array(xlist)
y = np.array(plist)
x2 = np.array(np.log(bs))
y2 = np.array(np.log(nums))

plt.figure()
plt.scatter(x,y, s=1)
plt.xlabel('x')
plt.ylabel('p')
plt.title('Strange Attractor')

plt.figure()
plt.scatter(x2,y2)
plt.xlabel('log(b)')
plt.ylabel('log(N(b))')
plt.title('Dimension')
m, b = np.polyfit(x2,y2,deg=1)
xseq = np.linspace(-3, 2, 100)
plt.plot(xseq, b + m*xseq, color='k', lw=2.5)
print("slope: " + str(m))

print("Close plot window to exit")
for m in matricies:
    plt.matshow(m)
plt.show()


