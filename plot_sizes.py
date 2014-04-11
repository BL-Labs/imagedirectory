import numpy as np
import matplotlib.pyplot as plt

import json

data = json.load(file("sizecounts.json"))

m = 0
m_key = None

x = []
y = []
s = []

for k,v in data.iteritems():
  if v>m: 
    m=v
    m_key = k
  tx, ty = map(lambda x: int(x), k.split("_"))
  x.append(tx)
  y.append(ty)
  if v > 100:
    s.append(np.pi * (2.0 * v / 250.0)**2)
  else:
    s.append(np.pi / 4.0)
  
print("Number of different sizes: {0}\n Most of a given size:{1} {2}".format(len(data), m, m_key))

plt.scatter(x,y,s,alpha=0.5)

plt.savefig("size_distribution.png", dpi=600)

