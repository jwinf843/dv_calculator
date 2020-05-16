from kerbol_bodies import *
from solar_bodies import *
from math import pi as π
from math import sqrt

def find_semimajor_axis(p_start, p_finish):
    R1 = (p_start['ap'] + p_start['pe']) / 2
    R2 = (p_finish['ap'] + p_finish['pe']) / 2
    
    output = {
        'SMA Start': R1,
        'SMA Finish': R2,
    }
    
    return output


    
results = find_semimajor_axis(earth, mars)
print(results)