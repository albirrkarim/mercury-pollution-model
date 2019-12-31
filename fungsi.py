def processRunge(growthFunc, *args):
    # Fungsi runge kutta 4
    # IF : growthFunc   -> fungsi pertumbuhan
    #      args         -> h        -> Delta Time
    #                      x0       -> Waktu yg terus bertambah (ditambah delta time)
    #                      populasi -> Populasi pada waktu sebelumnya
    #                      lisData  -> Tuple untuk passing data fluxes ke fungsi pertumbuhan
    # FS : Populasi pada waktu x

    h, x0, populasi, listData = args

    k1 = h * growthFunc(x0, populasi,listData)
    k2 = h * growthFunc(x0 + 0.5 * h, populasi + 0.5 * k1,listData)
    k3 = h * growthFunc(x0 + 0.5 * h, populasi + 0.5 * k2,listData)
    k4 = h * growthFunc(x0 + h, populasi + k3,listData)
    
    return populasi + ((k1 + 2 * k2 + 2 * k3 + k4) / 6.0 )


def growthAtmospherePools(waktu,populasi, *args):
    # Fungsi Pertumbuhan Atmosphere
    TerrestrialDeposition, MarineDeposition, Evasion, NaturalEmission, ParticulateRemoval = args[0]

    return (NaturalEmission + Evasion)*waktu


def growthMixedLayerPools(waktu, populasi, *args):
    # Fungsi Pertumbuhan MixedLayer
    TerrestrialDeposition, MarineDeposition, Evasion, NaturalEmission, ParticulateRemoval = args[0]

    return (-ParticulateRemoval - Evasion - NaturalEmission + TerrestrialDeposition + MarineDeposition)*waktu



def outputTable(time,listAtmosphere,listMixedLayer):
    # Outputkan nilai populasi pada setiap iterasi
    from tabulate import tabulate
    results=[]
    for i in range(0,len(time)):
        results.append((time[i],listAtmosphere[i],listMixedLayer[i]))

    print(tabulate(results,headers=["Time","Atmosphere","MixedLayer"],tablefmt="fancy_grid"))