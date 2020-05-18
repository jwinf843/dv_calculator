<img src="https://www.jpl.nasa.gov/edu/images/activities/launch_window.gif">

# STEP 1 - Find the distance of the target planets from their sun
 - Use distance in kilometers

R1 = distance_earth = 149,600,000km

R2 = distance_mars = 227,920,000km

# STEP 2 - Calculate the Standard Gravitational Parameter (GM)
 - Mass of the sun x the gravitational constant
 
GM = (grav_const) x (Mass of Star) = 1.327 x (10^11 km³/s²)

# STEP 3 - Convert the orbital periods of target planets into seconds

P1 = period_earth = 365.25636 x 86400 = 31,558,149.5 seconds

P2 = period_mars = 686.6812 x 86400 = 59,329,255.68 seconds

# STEP 4 - Calculate (a) the semi-major axis of the transfer orbit
<img src="https://cdn.instructables.com/F6J/AX0G/IJM04GNT/F6JAX0GIJM04GNT.LARGE.jpg?auto=webp&frame=1&width=724&fit=bounds">

a(transfer) = (R1 + R2) / 2

# STEP 5 - Find the period of the transfer orbit
 - Use Kepler's Third Law
 
<img src="https://cdn.instructables.com/FS4/5CCU/IJLZX244/FS45CCUIJLZX244.LARGE.gif?auto=webp&frame=1&fit=bounds">

P(transfer) = √(4π²·a³/GM )

# STEP 6 - Find the Velocity of the Target Planets
 - You use this velocity as a starting point (You're already going this fast)
 
V1 = (2π x R1) / P1

V2 = (2π x R2) / P2

# STEP 7 - Find velocity of the transfer orbit at periapsis

V(perihelion) = (2π x a(transfer) / P(transfer) ) x √( (2a(transfer) / R1) - 1)

# STEP 8 - Find the change in velocity required at the start
 - This is the amount of dv required to enter the transfer orbit
 
<img src="https://ai-solutions.com/_freeflyeruniversityguide/hohmanndiagram.png" width="300" height="300">
 
ΔV1 = V(perihelion) - V1 

# STEP 9 - Find the velocity at apoapsis
 - Calculate how fast your craft will be moving at the highest point (just as  you arrive at the target planet)
 
V(aphelion) = (2π x a(transfer) / P(transfer) ) x √( (2a(transfer) / R2) - 1)

# STEP 10 - Find the change in velocity required to inject from the transfer orbit into orbit around the target planet

ΔV2 = V2- V(aphelion)

# STEP 11 - Add ΔV1 and ΔV2 for your total Δv requirement

Δv = ΔV1 + ΔV2
