import pytest

from utilities import number_fudger

from transfer import *
from solar_bodies import *

# STEP 1
def test_semi_major_axis():
    """Get the semi major axis of start and finish positions"""
    
    results = find_semimajor_axis(earth, mars)
    
    print(results['SMA Start'], 149598023)
    assert number_fudger(results['SMA Start'], 149598023) == True
    print(results['SMA Finish'], 227939200)
    assert number_fudger(results['SMA Finish'], 227939200) == True
    