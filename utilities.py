from kerbol_bodies import *
from solar_bodies import *
from math import pi as π
from math import sqrt

def number_fudger(data, reality):
    """A function to determine if the data is within 1% margin of error with reality"""
    reality_up = reality + (reality * 0.001)
    reality_down = reality - (reality * 0.001)
    
    if reality_up > data > reality_down:
        return True

def calculate_interplanetary_transfer(p_start, p_finish): 
    """Calculate the dv required for a Hohmann transfer from start to finish
    
    p_start and p_finish should both be bodies in orbit about the same stellar mass, passed as dictionaries to the function.
    """
    
    # STEP 1
    R1 = (p_start['ap'] + p_start['pe'] / 2)
    R2 = (p_finish['ap'] + p_finish['pe'] / 2)
    
    # STEP 2
    GM = 1.172 * (10 ** 18)
    
    # STEP 3
    P1 = p_start['period']
    P2 = p_finish['period']
    
    # STEP 4
    a_transfer = (R1 + R2) / 2
    
    # STEP 5
    p_transfer = sqrt((4 * π ** 2) * (a_transfer ** 3) / GM)
    
    # STEP 6
    V1 = (2 * π * R1) / P1
    V2 = (2 * π * R2) / P2
    
    # STEP 7
    top = (2 * π * a_transfer) / p_transfer
    bottom = sqrt(2 * a_transfer / R1) - 1
    Vp = top * bottom
    
    # STEP 8
    ΔV1 = Vp - V1
    
    # STEP 9
    top = (2 * π * a_transfer) / p_transfer
    bottom = sqrt(2 * a_transfer / R2) - 2
    Va = top * bottom
    
    # STEP 10
    ΔV2 = V2 - Va
    
    # FINAL
    dv = ΔV1 + ΔV2
    
    print(Vp)
    print(π)
    
    return dv
    

k_e = calculate_interplanetary_transfer(earth, mars)
print(k_e)