from planets.planets import *

# Sun has been shrunk 100 times
# Planet distances shrunk by 1000 times
# One pixel is 1000km
# One Earth day is 1000 ticks

sun = Sun(14, 'sun')
mercury = Planet(2, 'mercury', 57, 240, 0.2056, sun) 
venus = Planet(6, 'venus', 108, 620, 0.0068, sun) 
earth = Planet(6, 'earth', 150, 1000, 0.0167, sun)
mars = Planet(3, 'mars', 228, 1880, 0.0934, sun) 
jupiter = Planet(139, 'jupiter', 779, 410,  0.04889, sun)
bodies = [sun, mercury, venus, earth, mars, jupiter]
system = System(bodies, (0, 0, 0))
system.run()
