import sys
from Sand import Sand_particle, py
from Wind import Wind, random

py.init()
UNIT_LIMITS = 400
ADD_WIND = bool(0)
WIDTH = Sand_particle.WIDTH
HEIGHT = Sand_particle.HEIGHT

BLACK = (0,0,0)
SAND_COLORS= [ (194, 178, 128), (0, 255, 0), (255, 192, 203),
              (128, 0, 128), (0, 0, 255) ]
marker = 0

SCREEN = py.display.set_mode( (WIDTH,HEIGHT) )
py.display.set_caption("SandBox")

sand_particles = []

wind = None
if ADD_WIND:
    wind = Wind( random.choice([-1,1]*4),10 )

#Display screen
running = True
mouse_down = False

while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        elif event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_down = True
        elif event.type == py.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                mouse_down = False

        if mouse_down:
            mouse_x, mouse_y = py.mouse.get_pos()
            sand_particles.append( Sand_particle(mouse_x, mouse_y, SAND_COLORS[marker]) )
            marker += 1

            if marker >= len(SAND_COLORS):
                marker -= len(SAND_COLORS)

    SCREEN.fill(BLACK)

    if ADD_WIND:
        wind.update()
    sand_particles = sand_particles[-UNIT_LIMITS:]
    for sp in sand_particles:
         # update sand particles position
        sp.update( sand_particles,wind )
        py.draw.circle(SCREEN,sp.color,(sp.x,sp.y),Sand_particle.SIZE)

    py.display.flip()