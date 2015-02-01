from planets.planets import *

# Entirely not to scale.
# For an exercise, fit to actual parameters.

sun = Sun(100, 'sun')
earth = Planet(10, 'earth', 1000, 1000, 0.5, sun)
system = System([sun, earth], (0, 0, 0)) 
system.run()
