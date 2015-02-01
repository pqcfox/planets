from planets.planets import *

# Entirely not to scale.
# For an exercise, fit to actual parameters.
# Warning: if you set the eccentricity too high, the circle approxmation
# for theta given to fsolve will deviate from the actual path enough 
# to cause the planet to flash between both sides of the orbit.

sun = Sun(100, 'sun')
earth = Planet(10, 'earth', 1000, 1000, 0.2, sun)
system = System([sun, earth], (0, 0, 0)) 
system.run()
