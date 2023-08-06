import os
import numpy as np
import pandas as pd
import sdapy.interaction_processes as ip
from collections import namedtuple
from scipy.interpolate import RegularGridInterpolator
from sdapy import __path__, constants
srcpath = __path__[0]

def get_csm_properties(nn, eta):
    csm_properties = namedtuple('csm_properties', ['AA', 'Bf', 'Br'])
    filepath = f"{srcpath}/data/csm_table.txt"
    assert os.path.exists(filepath)
    ns, ss, bfs, brs, aas = np.loadtxt(filepath, delimiter=',', unpack=True)
    bfs = np.reshape(bfs, (10, 30)).T
    brs = np.reshape(brs, (10, 30)).T
    aas = np.reshape(aas, (10, 30)).T
    ns = np.unique(ns)
    ss = np.unique(ss)
    bf_func = RegularGridInterpolator((ss, ns), bfs)
    br_func = RegularGridInterpolator((ss, ns), brs)
    aa_func = RegularGridInterpolator((ss, ns), aas)

    Bf = bf_func([nn, eta])[0]
    Br = br_func([nn, eta])[0]
    AA = aa_func([nn, eta])[0]

    csm_properties.AA = AA
    csm_properties.Bf = Bf
    csm_properties.Br = Br
    return csm_properties

def _csm_engine(time, mej, csm_mass, vej, eta, rho, kappa, r0):
    """
    :param time: time in days in source frame
    :param mej: ejecta mass in solar masses
    :param csm_mass: csm mass in solar masses
    :param vej: ejecta velocity in km/s
    :param eta: csm density profile exponent
    :param rho: csm density profile amplitude
    :param kappa: opacity
    :param r0: radius of csm shell in AU    
    :return: named tuple with 'lbol','r_photosphere' 'mass_csm_threshold'
    """
    mej = mej * constants.M_sun
    csm_mass = csm_mass * constants.M_sun
    r0 = r0 * constants.au_cgs
    vej = vej * constants.km_cgs
    Esn = 3. * vej ** 2 * mej / 10.
    ti = 1.
    
    #efficiency: in converting between kinetic energy and luminosity, default 0.5
    #delta: default 1,
    #nn: default 12,
    delta = 1
    nn = 12
    efficiency = 0.5
    
    csm_properties = get_csm_properties(nn, eta)
    AA = csm_properties.AA
    Bf = csm_properties.Bf
    Br = csm_properties.Br

    # Derived parameters
    # scaling constant for CSM density profile
    qq = rho * r0 ** eta
    # outer CSM shell radius
    radius_csm = ((3.0 - eta) / (4.0 * np.pi * qq) * csm_mass + r0 ** (3.0 - eta)) ** (
            1.0 / (3.0 - eta))
    # photosphere radius
    r_photosphere = abs((-2.0 * (1.0 - eta) / (3.0 * kappa * qq) +
                         radius_csm ** (1.0 - eta)) ** (1.0 / (1.0 - eta)))

    # mass of the optically thick CSM (tau > 2/3).
    mass_csm_threshold = np.abs(4.0 * np.pi * qq / (3.0 - eta) * (
            r_photosphere ** (3.0 - eta) - r0 ** (3.0 - eta)))

    # g**n is scaling parameter for ejecta density profile
    g_n = (1.0 / (4.0 * np.pi * (nn - delta)) * (
            2.0 * (5.0 - delta) * (nn - 5.0) * Esn) ** ((nn - 3.) / 2.0) / (
                   (3.0 - delta) * (nn - 3.0) * mej) ** ((nn - 5.0) / 2.0))

    # time at which shock breaks out of optically thick CSM - forward shock
    t_FS = (abs((3.0 - eta) * qq ** ((3.0 - nn) / (nn - eta)) * (
            AA * g_n) ** ((eta - 3.0) / (nn - eta)) /
                (4.0 * np.pi * Bf ** (3.0 - eta))) ** (
                    (nn - eta) / ((nn - 3.0) * (3.0 - eta))) * (mass_csm_threshold) ** (
                    (nn - eta) / ((nn - 3.0) * (3.0 - eta))))

    # time at which reverse shock sweeps up all ejecta - reverse shock
    t_RS = (vej / (Br * (AA * g_n / qq) ** (
            1.0 / (nn - eta))) *
            (1.0 - (3.0 - nn) * mej /
             (4.0 * np.pi * vej **
              (3.0 - nn) * g_n)) ** (1.0 / (3.0 - nn))) ** (
                   (nn - eta) / (eta - 3.0))

    mask_1 = t_FS - time * constants.day_to_s > 0
    mask_2 = t_RS - time * constants.day_to_s > 0

    lbol = efficiency * (2.0 * np.pi / (nn - eta) ** 3 * g_n ** ((5.0 - eta) / (nn - eta)) * qq **
                         ((nn - 5.0) / (nn - eta)) * (nn - 3.0) ** 2 * (nn - 5.0) * Bf ** (5.0 - eta) * AA **
                         ((5.0 - eta) / (nn - eta)) * (time * constants.day_to_s + ti) **
                         ((2.0 * nn + 6.0 * eta - nn * eta - 15.) /
                          (nn - eta)) + 2.0 * np.pi * (AA * g_n / qq) **
                         ((5.0 - nn) / (nn - eta)) * Br ** (5.0 - nn) * g_n * ((3.0 - eta) / (nn - eta)) ** 3 * (
                                     time * constants.day_to_s + ti) **
                         ((2.0 * nn + 6.0 * eta - nn * eta - 15.0) / (nn - eta)))

    lbol[~mask_1] = 0
    lbol[~mask_2] = 0

    csm_output = namedtuple('csm_output', ['lbol', 'r_photosphere', 'mass_csm_threshold'])
    csm_output.lbol = lbol
    csm_output.r_photosphere = r_photosphere
    csm_output.mass_csm_threshold = mass_csm_threshold
    return csm_output

def csm_interaction_bolometric(times, mej, csm_mass, vej, eta, rho, kappa, r0, texp=None):
    """
    :param times: time in days in source frame
    :param mej: ejecta mass in solar masses
    :param csm_mass: csm mass in solar masses
    :param vej: ejecta velocity in 1000 km/s
    :param eta: csm density profile exponent
    :param rho: csm density profile amplitude
    :param kappa: opacity
    :param r0: radius of csm shell in AU    
    :param texp: time in days, time between first light to the peak epoch
    :return: bolometric_luminosity
    """
    time = times
    if texp is not None: time = times - texp
    csm_output = _csm_engine(time=time, mej=mej, csm_mass=csm_mass, vej=vej*1000.,
                             eta=eta, rho=rho, kappa=kappa, r0=r0)    
    lbol = csm_output.lbol
    r_photosphere = csm_output.r_photosphere
    mass_csm_threshold = csm_output.mass_csm_threshold    
    _ip = ip.CSMDiffusion(time=time, luminosity=lbol,
                          kappa=kappa, r_photosphere=r_photosphere,
                          mass_csm_threshold=mass_csm_threshold, csm_mass=csm_mass)        
    lbol = _ip.new_luminosity
    return lbol
