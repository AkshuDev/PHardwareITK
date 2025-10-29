import random
import time
import ctypes
import sys
import os

if not os.path.join(os.path.dirname(__file__), "..") in sys.path:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from phardwareitk.GPU._gl_driver import GL_FRAGMENT_SHADER, GL_VERTEX_SHADER
from phardwareitk.GUI.pheonix_ion import *

print("Initializing Pheonix Ion + Window...")
ion = PheonixIon()
win = ion.create_window("OpenGL Driver Feature Test", 800, 600)
ion.show_window(win)

print("Creating GPU context...")
ctx = ion.get_gpu(win)
ion.attach_gpu(win, ctx)
driver = ctx.driver

driver.viewport(800, 600)

print("Preparing test assets...")
# buffer = driver.create_buffer()
# driver.bind_array_buffer(buffer)

# data = [random.random() for _ in range(12)]
# driver.buffer_data(data)

# texture = driver.create_texture()
# driver.bind_texture(texture)

# # Fill with random data
# w, h = 64, 64
# pixels = (ctypes.c_float * (w * h * 4))(*[random.random() for _ in range(w * h * 4)])
# driver.tex_image_2d(w, h, pixels)

try:
    vertex_src = """
    #version 330 core
    layout(location = 0) in vec3 pos;
    void main() {
        gl_Position = vec4(pos, 1.0);
    }
    """

    frag_src = """
    #version 330 core
    out vec4 FragColor;
    void main() {
        FragColor = vec4(0.3, 0.8, 0.2, 1.0);
    }
    """

    vertex_shader = driver.create_shader(GL_VERTEX_SHADER, vertex_src)
    fragment_shader = driver.create_shader(GL_FRAGMENT_SHADER, frag_src)

    program = driver.create_program(vertex_shader, fragment_shader)
    driver.use_program(program)
    HAS_SHADERS = True
    print("Shader pipeline OK.")
except Exception as e:
    print("Shader test skipped or failed:", e)
    HAS_SHADERS = False

print("""
Interactive Tests Ready:

  LEFT CLICK    - Test Clear + Swap (random color)
  RIGHT CLICK   - Test Buffers (random upload)
  MIDDLE CLICK  - Test Texture Binding
  [R] key       - Reset viewport size
  [C] key       - Compile / link shaders again
  [ESC] or QUIT - Exit

Watch the console for logs and window for color changes.
""")

running = True
frame_count = 0

while running:
    events = ion.poll_events(win)
    for e in events:
        # Quit
        if e.type == PIonEvent_Types["QUIT"]:
            running = False

        # LEFT CLICK: clear + swap
        elif e.type == PIonEvent_Types["LEFT_DOWN"]:
            r, g, b = [random.randint(0, 255) for _ in range(3)]
            print(f"Clear + Swap → RGB=({r},{g},{b})")
            driver.clear(r, g, b, 255)
            driver.swap()

        # RIGHT CLICK: buffer test
        elif e.type == PIonEvent_Types["RIGHT_DOWN"]:
            print("Rebinding + reuploading buffer data...")
            driver.bind_array_buffer(buffer)
            data = [random.random() for _ in range(6)]
            driver.buffer_data(data)

        # MIDDLE CLICK: texture test
        elif e.type == PIonEvent_Types["MIDDLE_DOWN"]:
            print("Rebinding texture with random pixels...")
            driver.bind_texture(texture)
            pixels = (ctypes.c_float * (w * h * 4))(*[random.random() for _ in range(w * h * 4)])
            driver.tex_image_2d(w, h, pixels)

        # Keyboard tests
        elif e.type == PIonEvent_Types["KEYDOWN"]:
            key = e.data["keycode"]
            # ESC or Q to quit
            if key in (0x1B, 0x51):
                print("Exiting test...")
                running = False
            # R – Reset viewport
            elif key in (0x52,):  # 'R'
                new_w, new_h = random.randint(400, 1600), random.randint(400, 1200)
                print(f"Resizing viewport to {new_w}x{new_h}")
                driver.viewport(new_w, new_h)
            # C – Recompile shaders
            elif key in (0x43,):  # 'C'
                if HAS_SHADERS:
                    print("Recompiling shaders...")
                    try:
                        driver.shader_source(vertex_shader, vertex_src)
                        driver.compile_shader(vertex_shader)
                        driver.shader_source(fragment_shader, frag_src)
                        driver.compile_shader(fragment_shader)
                        program = driver.create_program(vertex_shader, fragment_shader)
                        driver.use_program(program)
                        print("Shader recompile success.")
                    except Exception as ex:
                        print("Shader recompile failed:", ex)
                else:
                    print("Shader tests not available.")

    if frame_count % 200 == 0:
        driver.clear(random.randint(0,255), random.randint(0,255), random.randint(0,255), 255)
        driver.swap()

    frame_count += 1
    time.sleep(0.01)


print("Shutting down and releasing resources...")
driver.shutdown()
ion.destroy_window(win)
print("Pheonix Ion feature test complete.")
