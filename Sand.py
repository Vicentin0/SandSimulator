import pygame as py

simulation_speed = 5

gravity = 9.8 * simulation_speed

class Sand_particle:

    WIDTH = 350
    HEIGHT = 350

    SIZE = 1.5

    def __init__(self,x,y,color) -> None:

        self.x = x
        self.y = y
        self.velocity_y = 0
        self.velocity_x = 0
        self.last_update_time = py.time.get_ticks()
        self.color = color

    def update(self, particles,wind) :

        if self.y + Sand_particle.SIZE >= Sand_particle.HEIGHT:
            return 

        current_time = py.time.get_ticks()
        dt = max((current_time - self.last_update_time) / 1000,0.005 ) # Convert milliseconds to seconds
        self.last_update_time = current_time


        # Apply gravity
        self.velocity_y += gravity * dt
        new_y = self.y + self.velocity_y * dt
        
        #apply wind
        if wind != None:
            wind_vector = wind.get_wind_vector()
            self.velocity_x = wind_vector[0]
            new_x = self.x + self.velocity_x * dt
        else: 
            new_x = self.x

        collision_y = False
        collision_x = False
        for p in particles:
            if p is not self:  # Skip itself
                if (p.y - p.SIZE <= new_y + Sand_particle.SIZE <= p.y + p.SIZE) and \
               (p.x - p.SIZE <= new_x <= p.x + p.SIZE):
                    collision_y = True

            # Check horizontal collision
            if (p.x - p.SIZE <= new_x + Sand_particle.SIZE <= p.x + p.SIZE) and \
               (p.y - p.SIZE <= new_y <= p.y + p.SIZE):
                    collision_x = True

        if not (collision_y and collision_x)  and new_y + Sand_particle.SIZE < Sand_particle.HEIGHT:
            self.y = new_y

        if wind !=  None:   
            if 5 + Sand_particle.SIZE <= new_x < Sand_particle.WIDTH - Sand_particle.SIZE: 
                self.x = new_x