import matplotlib.pyplot as plt
from fungsi import *
from data import *

# _____________________________[ Mercury Cycle ] __________________________
# ______________________________ Initialization ___________________________

# ___________________ PreIndustri ____________________
PI = PreIndustrial()
# Pools
Atmosphere, MixedLayer = PI.getPools()
# Fluxes
preIndustrialFluxesData = PI.getFluxes()

# _________________ Simulation settings _______________
Config   = SimulationConfig()
x0, x, h = Config.getConfig()

# ___________________ List for output _________________
listAtmospherePopulation = []
listMixedLayerPopulation = []
listTime = []

# ________________________________ Process _________________________________

# Tambahkan populasi awal
listAtmospherePopulation.append( Atmosphere )
listMixedLayerPopulation.append( MixedLayer )
listTime.append(x0)
x0 += h 

n = (int)((x - x0)/h) + 1

for i in range(0,n): # perulangan per 0.01 year 
    
    # Mixed Layer
    MixedLayer = processRunge(growthMixedLayerPools,h,x0,MixedLayer,preIndustrialFluxesData)
    listMixedLayerPopulation.append( MixedLayer )

    # Atmosphere
    Atmosphere = processRunge(growthAtmospherePools,h,x0,Atmosphere,preIndustrialFluxesData)
    listAtmospherePopulation.append( Atmosphere )

    # Update Fluxes Rate
    preIndustrialFluxesData = PI.updateFluxes(MixedLayer)

    # Time List
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
plt.title("Pre Industrial grafik")

# Set x, y label text.
plt.xlabel("Time")
plt.ylabel("Population")
plt.show()