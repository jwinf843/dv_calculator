from kerbol_bodies import *
from solar_bodies import *
from math import pi as π
from math import sqrt
from pprint import pprint

def find_semimajor_axis(p_start, p_finish):
    R1 = (p_start['ap'] + p_start['pe']) / 2
    R2 = (p_finish['ap'] + p_finish['pe']) / 2
    
    output = {
        'SMA Start': R1,
        'SMA Finish': R2,
    }
    
    return output


def find_transfer_orbit(p_start, p_finish):
    data = find_semimajor_axis(p_start, p_finish)
    
    R1 = data['SMA Start']
    R2 = data['SMA Finish']
    
    a_transfer = R1 + R2
    output = a_transfer / 2
    
    return output

def find_transfer_period(p_start, p_finish):
    # p_transfer = √(4π²·a³/GM )
    GM = None
    
    if p_start in kerbol_bodies:
        GM = 1.172 * 10 ** 9
    else:
        GM = 1.327 * 10 ** 11
    
    data = find_transfer_orbit(p_start, p_finish)
    
    numerator_left = 4 * π ** 2
    numerator_right = data ** 3
    numerator_total = numerator_left * numerator_right
        
    result = numerator_total / GM
    p_transfer = sqrt(result)
    
    return p_transfer

def find_target_velocities(p_start, p_finish):
    data_set = find_semimajor_axis(p_start, p_finish)
    R1 = data_set['SMA Start']
    R2 = data_set['SMA Finish']

    P1 = p_start['period']
    P2 = p_finish['period']
    
    numerator = 2 * π
    
    V1 = numerator * R1 / P1
    V2 = numerator * R2 / P2
    
    output = {
        'V1': V1,
        'V2': V2,
    }
    
    return output
    
def find_transfer_velocity(p_start, p_finish):
    a_transfer = find_transfer_orbit(p_start, p_finish)
    p_transfer = find_transfer_period(p_start, p_finish)
    data_set = find_semimajor_axis(p_start, p_finish)
    R1 = data_set['SMA Start']
    
    top_left = 2 * π * a_transfer
    left = top_left / p_transfer
    
    top_right = 2 * a_transfer
    right_inside = top_right / R1
    right_inside -= 1
    right = sqrt(right_inside)
    
    v_periapsis = left * right
    
    return v_periapsis
    
def find_insertion_velocity(p_start, p_finish):
    vp_data = find_target_velocities(p_start, p_finish)
    v_periapsis = find_transfer_velocity(p_start, p_finish)    
    V1 = vp_data['V1']
    
    ΔV1 = v_periapsis - V1
    
    return ΔV1
    
def find_velocity_at_destination(p_start, p_finish):
    a_transfer = find_transfer_orbit(p_start, p_finish)
    p_transfer = find_transfer_period(p_start, p_finish)
    
    data_set = find_semimajor_axis(p_start, p_finish)
    R2 = data_set['SMA Finish']
    
    top_left = 2 * π * a_transfer
    left = top_left / p_transfer
    
    top_right = 2 * a_transfer
    inside_right = top_right / R2
    inside_right -= 1
    right = sqrt(inside_right)
    
    v_aphelion = left * right
    
    return v_aphelion
