import pytest

from utilities import number_fudger

from transfer import *
from solar_bodies import *

# STEP 1
def test_1_semi_major_axis():
    """
    Get the semi major axis of start and finish positions
    """
    
    results = find_semimajor_axis(earth, mars)
    
    assert number_fudger(results['SMA Start'], 149598023)
    assert number_fudger(results['SMA Finish'], 227939200)

# STEP 2
    """
    Note - Step 2 isn't being tested because it is a constant
    """
    
    
# STEP 3
    """
    Note - Step 3 isn't being tested because the results are readily available as constants
    """
    
# STEP 4
def test_2_transfer_orbit():
    """
    Find the semimajor axis of the transfer orbit
    """
    
    a_transfer = find_transfer_orbit(earth, mars)
    
    assert number_fudger(a_transfer, 188768611.5)
    assert number_fudger(a_transfer, 188000000)
    # 188768611.5km is derived from Wikipedia's information
    # 1.885×10^8 km is derived from WolframAlpha using 1AU and 1.56AU
    # Either is an acceptable answer, but AU is less precise
    
# STEP 5
def test_3_transfer_period():
    """
    Find the period in seconds of the transfer orbit using Kepler's Third Law
    """
    
    results = find_transfer_period(earth, mars)
    
    assert number_fudger(results, 44734138.6)
    assert number_fudger(results, (4.493 * 10 ** 7))
    # 44734138.6 seconds were derived by hand
    # 4.493E7 is  derived from WolframAlpha <less precise>
    
    
# STEP 6
def test_4_target_velocities(): 
    """
    Calculate the velocities at the starting and ending positions
    """
    
    results = find_target_velocities(earth, mars)
    
    assert number_fudger(results['V1'], 29.78)
    assert number_fudger(results['V2'], 24.007)
    #29.78km/s and 24.007km/s are taken from the wiki pages for Earth and Mars
    