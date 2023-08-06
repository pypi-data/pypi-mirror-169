# -*- coding: utf-8 -*- 
"""
    @Author: N. Papadakis
    @Date: 2022/07/02
    @Credit: original functions from G. Arnaoutakis
"""
import numpy as np
import pandas as pd
from CombiCSP import OutputContainer, CtoK, HOYS_DEFAULT, SolarSystemLocation
import CombiCSP.SolarGeometry as sgh
from CombiCSP.solar_system_location import SolarSystemLocation
  
class SolarTowerCalcs():
    def __init__(self, 
        alt = 200*10e-3 
        , Ht = 0.1
        , Ar = 99.3 
        , A_helio = 225000
        , slobj:SolarSystemLocation = None
        ):
        self.Ar_m2 = Ar# receiver area [m2] pp.44 in Pacheco
        self.alt_m = alt #Height above sea level [m]
        self.Ht_km = Ht # Tower height [km]
        self.A_helio_m2 = A_helio # SolarII 82,750 m² for 10MW https://en.wikipedia.org/wiki/The_Solar_Project
        self.Ctow = self.A_helio_m2 / self.Ar_m2
        if slobj is None:
            raise ValueError('System location not found')
        else:
            self._sl = slobj

    def perform_calc(self, Ib, transmittance=1, nG=0.97, hoy=HOYS_DEFAULT):
        """Performs solar tower calculations

        Args:
            Ib (_type_): _description_
            transmittance (int, optional): _description_. Defaults to 1.
            nG (float): Generator efficiency (TODO Crosscheck??)
            hoy (_type_, optional): _description_. Defaults to HOYS_DEFAULT.

        Returns:
            _type_: _description_
        """        
        # data = solarII(Ib=Ib,Trans=transmittance, IAM=IAM_tow(hoy)
        data = self.solarII(Ib=Ib,Trans=transmittance, nG=0.97, hoy=hoy)
        self._hourly_results = OutputContainer(data = data, \
                A_helio=self.A_helio_m2, Ctow=self.Ctow)
        return self._hourly_results
    
    def solarII(self, Ib:pd.Series,Trans:float, nG:float = 0.97, hoy:np.array=HOYS_DEFAULT)->pd.Series:
        """Calculates the power of the solar tower with heliostat
    
        R.K. McGovern, W.J. Smith, Optimal concentration and temperatures of solar thermal power plants,
        Energy Conversion and Management. 60 (2012) 226–232.
        J.E. Pacheco, R.W. Bradshaw, D.B. Dawson, W.D. la Rosa, R. Gilbert, S.H. Goods, P. Jacobs, M.J. Hale, S.A. Jones, G.J. Kolb, M.R. Prairie, H.E. Reilly, S.K. Showalter, L.L. VANT-HULL, 
        Final Test and Evaluation Results from the Solar Two Project, n.d. https://core.ac.uk/reader/193342950 (accessed September 8, 2020).
    


        Args:
            Ib (pd.Series): direct irradiance
            Trans (float): transmissivity 
            IAM (np.array): incidence angle modifier
            A_helio (float): heliostat area in m^2
            Ar (float): receiver area in m^2
            nG (float):  efficiency of generator Mosleh19 (Defaults to 0.97)

        Returns:
            pd.Series: power in MW
        """
        IAM  = self.IAM_tow(hoy=hoy)
        A_helio = self.A_helio_m2
        Ar = self.Ar_m2
        
        Effopt=100 # heliostat optical effiency [%] 65% pp.24 in Pacheco
        #A_helio = 71140 + 10260 # total heliostat area [m2] pp.22 in Pacheco
        R = 1 # reflectivity [%] 1 if IAM is IAM_tow(hoy)
        Qin = Ib * R * Trans * IAM * A_helio * Effopt/100 # Eq. 17  in McGovern12
        
        epsilon = 1 # the emissivity of the receiver’s material https://en.wikipedia.org/wiki/Emissivity
        sigma = 5.67 * 1e-8 # Stefan – Boltzman constant [W/m2K4]
        Trec = 565 # the working fluid temperature in the receiver [oC] 565 oC 838K
        Ta = 15 # ambient temperature close to the receiver [oC] 15 oC 288K
        Tin = 290 # working fluid inlet temperature to the receiver [oC] 290 oC 563K
        alpha = 1 # absorptivity of the receiver
        #Ar = 99.3 # receiver area [m2] pp.44 in Pacheco
        
        Qrad = epsilon * sigma * Ar * (CtoK(Trec)**4-CtoK(Ta)**4)
        hconv = CtoK(Trec)/60 + 5/3 # [W/m2K] convection coefficient Eq. 20 in McGovern12
        '''D.L. Siebers, J.S. Kraabel, Estimating convective energy losses from solar central 
        receivers, Sandia National Lab. (SNL-CA), Livermore, CA (United States), 1984. 
        https://doi.org/10.2172/6906848.'''
        Qconv = hconv * Ar * (CtoK(Trec) - CtoK(Ta))
        
        Qnet = alpha * Qin - Qrad - Qconv # Eq. 8 in McGovern12
        
        nR = 0.412 # SAM default

        if Qnet.all() <= 0: #<<<<<<<<<<<<<<<<<<< check with Qin
            P = 0
        else:
            P = Qnet * nR * nG
        return P/1e6 # convert W to MW

    #%% Incidence angle methods for towers

    def IAM_tow(self, hoy:np.array=HOYS_DEFAULT)->np.array : 
        """Incidence angle modifier of Tower (azimuth)

        for explanation see: http://www.solarpanelsplus.com/solar-tracking/
        
        # polynomial fit, see file IAM.py for data
        
        Args:
            hoy (np.array): hour of year

        Returns:
            np.array : Incidence angle modifier of Tower in rad
        """    
        return 1.66741484e-1 + 1.41517577e-2 * np.degrees(self._sl.z(hoy)) - 9.51787164e-5 * np.degrees(self._sl.z((hoy)))**2
    
    def incident_energy_on_system(self,  Ib:pd.Series, hoy:np.array = HOYS_DEFAULT)->pd.Series:
        return Ib*self.IAM_tow(hoy)

    def mutate(self,   alt = None , Ht = None
        , Ar = None 
        , A_helio = None
        , slobj:SolarSystemLocation = None):
        alt = self.alt_m if alt is None else alt
        Ht = self.Ht_km if Ht is None else Ht
        Ar = self.Ar_m2 if Ar is None else Ar
        A_helio = self.A_helio_m2 if A_helio is None else A_helio
        slobj = self._sl if slobj is None else slobj
        return SolarTowerCalcs(alt = alt, Ht=Ht, Ar=Ar, A_helio=A_helio, slobj=slobj)
        
    
def solarII(Ib:pd.Series,Trans:float,IAM:np.array,A_helio:float,Ar:float, 
            nG:float = 0.97)->pd.Series:
    """Calculates the power of the solar tower with heliostat
 
    R.K. McGovern, W.J. Smith, Optimal concentration and temperatures of solar thermal power plants,
    Energy Conversion and Management. 60 (2012) 226–232.
    J.E. Pacheco, R.W. Bradshaw, D.B. Dawson, W.D. la Rosa, R. Gilbert, S.H. Goods, P. Jacobs, M.J. Hale, S.A. Jones, G.J. Kolb, M.R. Prairie, H.E. Reilly, S.K. Showalter, L.L. VANT-HULL, 
    Final Test and Evaluation Results from the Solar Two Project, n.d. https://core.ac.uk/reader/193342950 (accessed September 8, 2020).
 


    Args:
        Ib (pd.Series): direct irradiance
        Trans (float): transmissivity 
        IAM (np.array): incidence angle modifier
        A_helio (float): heliostat area in m^2
        Ar (float): receiver area in m^2
        nG (float):  efficiency of generator Mosleh19 (Defaults to 0.97)

    Returns:
        pd.Series: power in MW
    """
    Effopt=100 # heliostat optical effiency [%] 65% pp.24 in Pacheco
    #A_helio = 71140 + 10260 # total heliostat area [m2] pp.22 in Pacheco
    R = 1 # reflectivity [%] 1 if IAM is IAM_tow(hoy)
    Qin = Ib * R * Trans * IAM * A_helio * Effopt/100 # Eq. 17  in McGovern12
    
    epsilon = 1 # the emissivity of the receiver’s material https://en.wikipedia.org/wiki/Emissivity
    sigma = 5.67 * 1e-8 # Stefan – Boltzman constant [W/m2K4]
    Trec = 565 # the working fluid temperature in the receiver [oC] 565 oC 838K
    Ta = 15 # ambient temperature close to the receiver [oC] 15 oC 288K
    Tin = 290 # working fluid inlet temperature to the receiver [oC] 290 oC 563K
    alpha = 1 # absorptivity of the receiver
    #Ar = 99.3 # receiver area [m2] pp.44 in Pacheco
    
    Qrad = epsilon * sigma * Ar * (CtoK(Trec)**4-CtoK(Ta)**4)
    hconv = CtoK(Trec)/60 + 5/3 # [W/m2K] convection coefficient Eq. 20 in McGovern12
    '''D.L. Siebers, J.S. Kraabel, Estimating convective energy losses from solar central 
    receivers, Sandia National Lab. (SNL-CA), Livermore, CA (United States), 1984. 
    https://doi.org/10.2172/6906848.'''
    Qconv = hconv * Ar * (CtoK(Trec) - CtoK(Ta))
    
    Qnet = alpha * Qin - Qrad - Qconv # Eq. 8 in McGovern12
    
    nR = 0.412 # SAM default

    if Qnet.all() <= 0: #<<<<<<<<<<<<<<<<<<< check with Qin
        P = 0
    else:
        P = Qnet * nR * nG
    return P/1e6 # convert W to MW

#%% Incidence angle methods for towers

def IAM_tow(hoy:np.array=HOYS_DEFAULT)->np.array : 
    """Incidence angle modifier of Tower (azimuth)

    for explanation see: http://www.solarpanelsplus.com/solar-tracking/
    
    # polynomial fit, see file IAM.py for data
    
    Args:
        hoy (np.array): hour of year

    Returns:
        np.array : Incidence angle modifier of Tower in rad
    """    
    return 1.66741484e-1 + 1.41517577e-2 * np.degrees(sgh.z(hoy)) - 9.51787164e-5 * np.degrees(sgh.z((hoy)))**2
    
def IAM_tow2(hoy:np.array=HOYS_DEFAULT) ->np.array : # polynomial fit, see file IAM.py for data
    """Incidence angle modifier of Tower - elevation

    Args:
        hoy (np.array): hour of year

    Returns:
        np.array : Incidence angle modifier of Tower - elevation in rad
    """    
    return 1.66741484e-1 + 1.41517577e-2 * np.degrees(sgh.ele(hoy)) - 9.51787164e-5 * np.degrees(sgh.ele((hoy)))**2
