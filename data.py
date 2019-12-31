class SimulationConfig:
    x0 = 0.0 		# Waktu awal
    x  = 1.0 		# Waktu Selesai (Sampai ke perulangan ke berapa)
    h  = 0.01 		# Delta time

    def getConfig(self):
        return (
            self.x0,
            self.x,
            self.h,
        )

class PreIndustrial:
    # Pools
    Atmosphere = 1600
    MixedLayer = 3600

    # Fluxes
    TerrestrialDeposition  = 1000
    MarineDeposition       = 600
    Evasion                = 600
    NaturalEmission        = 1000
    ParticulateRemoval     = 60

    def __init__(self): 
        self.sumFluxes = self.TerrestrialDeposition+self.MarineDeposition+self.Evasion+self.NaturalEmission+self.ParticulateRemoval
        self.TerrestrialDepoPrec = self.TerrestrialDeposition/self.sumFluxes
        self.MarineDepoPrec      = self.MarineDeposition/self.sumFluxes
        self.EvasionPrec         = self.Evasion/self.sumFluxes
        self.NatEmissionPrec     = self.NaturalEmission/self.sumFluxes
        self.ParRemovalPrec      = self.ParticulateRemoval/self.sumFluxes

    def updateFluxes(self,population):
        a = round( self.sumFluxes  *  (population / self.MixedLayer) , 3)
        return (
            a*self.TerrestrialDepoPrec,
            a*self.MarineDepoPrec,
            a*self.EvasionPrec,
            a*self.NatEmissionPrec,
            a*self.ParRemovalPrec
        )

    def getPools(self):
        return (self.Atmosphere,self.MixedLayer)

    def getFluxes(self):
        return (
            self.TerrestrialDeposition,
            self.MarineDeposition,
            self.Evasion,
            self.NaturalEmission,
            self.ParticulateRemoval,
        )


class CurrentTime:
    # Pools
    Atmosphere = 5000
    MixedLayer = 10800

    # Fluxes
    TerrestrialDeposition  = 5000
    MarineDeposition       = 2000
    Evasion                = 2000
    NaturalEmission        = 1000
    ParticulateRemoval     = 200

    def __init__(self): 
        self.sumFluxes = self.TerrestrialDeposition+self.MarineDeposition+self.Evasion+self.NaturalEmission+self.ParticulateRemoval
        self.TerrestrialDepoPrec = self.TerrestrialDeposition/self.sumFluxes
        self.MarineDepoPrec      = self.MarineDeposition/self.sumFluxes
        self.EvasionPrec         = self.Evasion/self.sumFluxes
        self.NatEmissionPrec     = self.NaturalEmission/self.sumFluxes
        self.ParRemovalPrec      = self.ParticulateRemoval/self.sumFluxes

    def updateFluxes(self,population):
        a = round( self.sumFluxes  *  (population / self.MixedLayer) , 3)
        return (
            a * self.TerrestrialDepoPrec,
            a * self.MarineDepoPrec,
            a * self.EvasionPrec,
            a * self.NatEmissionPrec,
            a * self.ParRemovalPrec
        )

    def getPools(self):
        return (self.Atmosphere,self.MixedLayer)

    def getFluxes(self):
        return (
            self.TerrestrialDeposition,
            self.MarineDeposition,
            self.Evasion,
            self.NaturalEmission,
            self.ParticulateRemoval,
        )