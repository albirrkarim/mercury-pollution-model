import matplotlib.pyplot as plt
from fungsi import *
from data import *

# _____________________________[ Mercury Cycle ] __________________________
# ______________________________ Initialization ___________________________

# ___________________ Current time ____________________
CT = CurrentTime()
# Pools
Atmosphere, MixedLayer = CT.getPools()
# Fluxes
currentTimeFluxesData  = CT.getFluxes()

# _________________ Simulation settings _______________
Config   = SimulationConfig()
x0, x, h = Config.getConfig()

# ___________________ List for output _________________
listAtmospherePopulation = []
listMixedLayerPopulation = []
listTime = []

#  _______________________________ Process ________________________________

# Tambahkan populasi awal
listAtmospherePopulation.append( Atmosphere )
listMixedLayerPopulation.append( MixedLayer )
listTime.append(x0)
x0 += h 

n = (int)((x - x0)/h) + 1

for i in range(0,n): # perulangan per 0.01 year 

    # Mixed Layer
    MixedLayer = processRunge(growthMixedLayerPools,h,x0,MixedLayer,currentTimeFluxesData)
    listMixedLayerPopulation.append(MixedLayer)

    # Atmosphere
    Atmosphere = processRunge(growthAtmospherePools,h,x0,Atmosphere,currentTimeFluxesData)
    listAtmospherePopulation.append(Atmosphere)

    # Update Fluxes Rate
    currentTimeFluxesData=CT.updateFluxes(MixedLayer)

    listTime.append(x0)

	# update x0 dgn delta 
    x0 += h 

#  ________________________________ Output _________________________________

# Jika ingin lihat nilai populasi dari setiap iterasi
outputTable(listTime,listAtmospherePopulation,listMixedLayerPopulation)

# Draw point based on above x, y axis values.
plt.plot(listTime,listAtmospherePopulation)
plt.plot(listTime,listMixedLayerPopulation)

plt.legend(["Atmosphere","MixedLayer"], loc='upper right')

# Set chart title.
plt.title("Current Time grafik")

# Set x, y label text.
plt.xlabel("Time")
plt.ylabel("Population")
plt.show()