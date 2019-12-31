import matplotlib.pyplot as plt
from fungsi import *
from data import *

# _____________________________[ Mercury Cycle ] __________________________
# _____________________________ Initialization ____________________________

# __________________ Pre industrial __________________
PI = PreIndustrial()
# Pools
Atmosphere1 , MixedLayer1 = PI.getPools()
#Fluxes
preIndustrialFluxesData = PI.getFluxes()

# ___________________ Current time ____________________
CT = CurrentTime()
# Pools
Atmosphere2, MixedLayer2 = CT.getPools()
# Fluxes
currentTimeFluxesData = CT.getFluxes()

# _________________ Simulation settings _______________
Config   = SimulationConfig()
x0, x, h = Config.getConfig()

# ___________________ List for output _________________
listAtmospherePopulation1 = []
listMixedLayerPopulation1 = []

listAtmospherePopulation2 = []
listMixedLayerPopulation2 = []
listTime = []

#  ________________________________ Process ________________________________

# Tambahkan populasi awal
listAtmospherePopulation1.append(Atmosphere1)
listMixedLayerPopulation1.append(MixedLayer1)

listAtmospherePopulation2.append(Atmosphere2)
listMixedLayerPopulation2.append(MixedLayer2)

listTime.append(x0)
x0 += h

n = (int)((x - x0)/h) + 1

for i in range(0,n): # perulangan per 0.01 year
    # ___________________ PreIndustri ____________________

    # Mixed Layer
    MixedLayer1 = processRunge(growthMixedLayerPools,h,x0,MixedLayer1,preIndustrialFluxesData)
    listMixedLayerPopulation1.append( MixedLayer1 )

    # Atmosphere
    Atmosphere1 = processRunge(growthAtmospherePools,h,x0,Atmosphere1,preIndustrialFluxesData)
    listAtmospherePopulation1.append( Atmosphere1 )

    # Update Fluxes Rate
    preIndustrialFluxesData = PI.updateFluxes(MixedLayer1)
    
    # ___________________ CurrentTime ___________________


    # Mixed Layer
    MixedLayer2 = processRunge(growthMixedLayerPools,h,x0,MixedLayer2,currentTimeFluxesData)
    listMixedLayerPopulation2.append(MixedLayer2)

    # Atmosphere
    Atmosphere2 = processRunge(growthAtmospherePools,h,x0,Atmosphere2,currentTimeFluxesData)
    listAtmospherePopulation2.append(Atmosphere2)

    # Update Fluxes Rate
    currentTimeFluxesData=CT.updateFluxes(MixedLayer2)

    # Catat waktu
    listTime.append(x0)

	# Update x0 dgn delta
    x0+=h

#  ___________________________________ Output __________________________________

# Draw point based on above x, y axis values.
plt.plot(listTime,listAtmospherePopulation1)
plt.plot(listTime,listMixedLayerPopulation1)

plt.plot(listTime,listAtmospherePopulation2)
plt.plot(listTime,listMixedLayerPopulation2)

# Set chart title.
plt.title("Pre Industrial vs Current Time grafik")

# Beri keterangan garis
plt.legend(['Atmosphere PreIndustrial',"MixedLayer PreIndustrial", 'Atmosphere CurentTime',"MixedLayer CurrentTime"], loc='upper right')

# Set x, y label text.
plt.xlabel("Time")
plt.ylabel("Population")
plt.show()