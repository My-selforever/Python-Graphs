import pandas as pd
import os
import matplotlib.pyplot as mpp

os.system('cls')

df = pd.read_csv("Plots/Filtered.csv")

m = df["Mass"].to_list()
r = df["Radius"].to_list()
g = df["Gravity"].to_list()

m.sort()
r.sort()
g.sort()

mpp.plot(r,m)
mpp.title("Mass And Radius")
mpp.xlabel("Radius")
mpp.ylabel("Mass")
mpp.show()

#Mass and Gravity

mpp.plot(m,g)
mpp.title("Mass and Gravity")
mpp.xlabel("Mass")
mpp.ylabel("Gravity")
mpp.show()