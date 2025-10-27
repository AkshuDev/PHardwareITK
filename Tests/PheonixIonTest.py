import random
import time
import ctypes
import sys
import os

if not os.path.join(os.path.dirname(__file__), "..") in sys.path:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from phardwareitk.GUI.pheonix_ion import *

print("Creating Ion and Window...")
ion = PheonixIon()
win = ion.create_window("Stress Test No Shaders", 800, 600)

print("Attaching GPU context...")
ctx = ion.get_gpu(win)
ion.attach_gpu(win, ctx)
driver = ctx.driver

driver.viewport(800, 600)

# Stress test parameters
NUM_BUFFERS = 100       # increase number of buffers
NUM_TEXTURES = 50       # increase number of textures
NUM_ITERATIONS = 1000   # iterations per frame
running = True

print("Creating buffers...")
buffers = [driver.create_buffer() for _ in range(NUM_BUFFERS)]
for buf in buffers:
    data = [random.random() for _ in range(5000)]  # bigger data
    driver.bind_array_buffer(buf)
    driver.buffer_data(data)

print("Creating textures...")
textures = [driver.create_texture() for _ in range(NUM_TEXTURES)]
for tex in textures:
    driver.bind_texture(tex)
    width, height = 512, 512  # larger textures
    pixel_data = (ctypes.c_float * (width*height*4))(*[random.random() for _ in range(width*height*4)])
    driver.tex_image_2d(width, height, pixel_data)

print("Starting intensive stress loop...")
while running:
    events = ion.poll_events(win)
    for e in events:
        if e.type == PIonEvent_Types["QUIT"]:
            running = False
        elif e.type == PIonEvent_Types["LEFT_DOWN"]:
            # Flood clear + swap multiple times
            for _ in range(NUM_ITERATIONS):
                r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                driver.clear(r, g, b, 255)
                driver.swap()
                
                # Randomly bind buffer & texture every iteration
                driver.bind_array_buffer(random.choice(buffers))
                driver.bind_texture(random.choice(textures))
    
    # Random viewport resize every frame
    driver.viewport(random.randint(200, 1600), random.randint(200, 1200))
    time.sleep(0.005)  # shorter sleep for higher load

print("Shutting down...")
driver.shutdown()
ion.destroy_window(win)
print("Stress test finished!")
