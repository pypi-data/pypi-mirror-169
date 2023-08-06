import numpy as np
import scipy.special as ss
from collections import namedtuple
from scipy.interpolate import interp1d
from scipy.integrate import quad, cumtrapz
from inspect import isfunction
from sdapy import constants, models
import sdapy.interaction_processes as ip

# assume a constant optical opacity for SLSN?
k_opt_slsn = 0.1

def basic_magnetar(time, p0, bp, mass_ns, theta_pb):
    """
    https://ui.adsabs.harvard.edu/abs/2006ApJ...648L..51S/abstract
    
    :param time: time in seconds in source frame
    :param p0: initial spin period in seconds
    :param bp: polar magnetic field strength in Gauss
    :param mass_ns: mass of neutron star in solar masses
    :param theta_pb: angle between spin and magnetic field axes    
    :return: luminosity
    """
    erot = 2.6e52 * (mass_ns/1.4)**(3./2.) * p0**(-2)
    tp = 1.3e5 * bp**(-2) * p0**2 * (mass_ns/1.4)**(3./2.) * (np.sin(theta_pb))**(-2)
    luminosity = 2 * erot / tp / (1. + 2 * time / tp)**2
    return luminosity

def magnetar_only(time, l0, tau, nn):
    """
    https://ui.adsabs.harvard.edu/abs/2017ApJ...843L...1L/abstract
    
    :param time: time in seconds
    :param l0: initial luminosity parameter
    :param tau: spin-down damping timescale
    :param nn: braking index    
    :return: luminosity or flux (depending on scaling of l0) as a function of time.
    """
    lum = l0 * (1. + time / tau) ** ((1. + nn) / (1. - nn))
    return lum

def basic_magnetar_powered_bolometric(times, p0, bp, mass_ns,
                theta_pb, mej, ek, texp=None, k_opt=None, k_gamma=None):
    """
    :param times: time in days in source frame
    :param p0: initial spin period
    :param bp: polar magnetic field strength in Gauss
    :param mass_ns: mass of neutron star in solar masses
    :param theta_pb: angle between spin and magnetic field axes        
    :param mej: total ejecta mass in solar masses
    :param ek: total kinetic energy in foe   
    :texp: explosion epoch, unit in days
    :k_opt: optical opacity 
    :k_gamma: gamma ray opacity 
    :return: bolometric_luminosity
    """
    time = times
    if texp is not None: time = times - texp
    if k_opt is None: k_opt = k_opt_slsn
    if k_gamma is None: k_gamma = constants.k_gamma
    
    lbol = basic_magnetar(time=time * constants.day_to_s, p0=p0, bp=bp, mass_ns=mass_ns, theta_pb=theta_pb)
    vej = models.arnett_tail.Mej_Ek_to_vej(mej, ek)
    _ip = ip.Diffusion(time, lbol, k_opt, k_gamma, mej, vej*1e3)
    lbol = _ip.new_luminosity
    return lbol

def general_magnetar_slsn_bolometric(time, l0, tsd, nn, mej, ek, k_opt=None, k_gamma=None):
    """
    :param time: time in days in source frame
    :param l0: magnetar energy normalisation in ergs
    :param tsd: magnetar spin down damping timescale in source frame days
    :param nn: braking index    
    :param mej: total ejecta mass in solar masses
    :param ek: total kinetic energy in foe   
    :k_opt: optical opacity 
    :k_gamma: gamma ray opacity 
    :return: bolometric_luminosity
    """
    if k_opt is None: k_opt = k_opt_slsn
    if k_gamma is None: k_gamma = constants.k_gamma        
    lbol = magnetar_only(time=time * constants.day_to_s, l0=l0, tsd=tsd * constants.day_to_s, nn=nn)
    vej = Mej_Ek_to_vej(mej, ek)
    _ip = ip.Diffusion(time, lbol, k_opt, k_gamma, mej, vej*1e3)
    lbol = _ip.new_luminosity    
    return lbol
