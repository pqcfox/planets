import math
import os
import pygame
import pygame.gfxdraw
from pygame.locals import *
from scipy.optimize import fsolve

def get_screen_size():
    info = pygame.display.Info()
    return (info.current_w, info.current_h)

def get_screen_middle():
    size = get_screen_size()
    return (size[0]/2.0, size[1]/2.0)
 
class Sun:
    def __init__(self, radius, image_name, position=None):
        self.radius = radius
        self.color = color
        self.position = position 
        image = pygame.image.load(os.path.join('images', image_name + '.png'))
        self.image = pygame.transform.scale(image, [radius*2, radius*2])

    def update(self, t):
        pass

class Planet: 
    def __init__(self, radius, image_name, semi_major_axis, period, eccentricity, sun):
        self.radius = radius
        image = pygame.image.load(os.path.join('images', image_name + '.png'))
        self.image = pygame.transform.scale(image, [radius*2, radius*2])
        self.semi_major_axis = semi_major_axis
        self.period = period
        self.eccentricity = eccentricity
        self.sun = sun
        self.center = None
        if self.sun.position is not None:
            self.center = self.sun.position


    def update(self, t):
       # Compute the mean motion
       n = 2.0 * math.pi / self.period
       M = n * t
       # Compute the eccentric anomaly
       epsilon = self.eccentricity
       E = fsolve(lambda E: E - epsilon * math.sin(E) - M, 0.0)
       # Compute the true anomaly
       theta = fsolve(lambda theta: (1.0-epsilon) * math.tan(theta/2.0)**2 - (1.0 + epsilon) * math.tan(E/2.0) ** 2, 2*math.pi/self.period*t)
       # Compute the heliocentric distance
       a = self.semi_major_axis
       r = a * (1.0 - epsilon * math.cos(E)) 
       x = r * math.cos(theta)
       y = r * math.sin(theta)
       if self.center is None:
           self.center = get_screen_middle()
       self.position = (int(x) + self.center[0], int(y) + self.center[1])

class System:
    def __init__(self, bodies, color):
        self.bodies = bodies 
        self.color = color
        self.time = 0

    def run(self):
        pygame.init()
        self.screen_size = get_screen_size()
        screen = pygame.display.set_mode(self.screen_size, pygame.FULLSCREEN)
        quit = False
        while not quit:
            screen.fill(self.color)

            for body in self.bodies:
                body.update(self.time)
                if body.position is None:
                    body.position = get_screen_middle() 
                x = body.position[0] - body.radius
                y = body.position[1] - body.radius
                screen.blit(body.image, (x, y)) 

            self.time += 1 
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit() 
                    quit = True


