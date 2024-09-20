import random
import math

class Wind:
    def __init__(self,dir,str=1):
        self.direction = dir  # Wind direction (-1 to 1, can be adjusted)
        self.speed = random.uniform(0.1, 1)  # Wind speed (pixels per second)
        self.turbulence = 0.0005  # Amount of random fluctuation in wind speed
        self.str = str

    def update(self):
        # Add some turbulence to the wind direction and speed
        self.direction += random.uniform(-self.turbulence, self.turbulence)
        self.speed += random.uniform(0, self.turbulence)

    def get_wind_vector(self):
        # Convert direction to a unit vector
        radian = math.radians(self.direction * 180)
        return (self.speed * math.cos(radian) * self.str , self.speed * math.sin(radian) * self.str)