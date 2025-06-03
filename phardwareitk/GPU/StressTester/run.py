import sys
import os

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

if not baseDir in sys.path:
    sys.path.append(baseDir)

from GPU import *
from Extensions import *
from CLI.cliToolKit import *

import time

clinfo = True

def stress_test_torch(duration=60, tensor_size=3000):
    """Stress test for CUDA or ROCm GPUs using PyTorch."""
    import torch

    if not torch.cuda.is_available():
        Text.WriteText("No CUDA/ROCm GPU detected. Exiting PyTorch stress test.", FontEnabled=True, Font=TextFont(font_color=Color("red")))
        exit(1)

    device = torch.device("cuda")
    start_time = time.time()
    elapsed_time = 0
    iterations = 0
    ranking = 0
    pps = 0
    sl = ""

    while elapsed_time < duration:
        try:
            # GPU-intensive operations
            A = torch.randn((tensor_size, tensor_size), device=device)
            B = torch.randn((tensor_size, tensor_size), device=device)
            C = torch.matmul(A, B)
            D = torch.sin(C) + torch.cos(C)
            del A, B, C, D
            torch.cuda.empty_cache()

            elapsed_time = time.time() - start_time
            iterations += 1
        except RuntimeError as e:
            Text.WriteText(e, FontEnabled=True, Font=TextFont(font_color=Color("red")))
            torch.cuda.empty_cache()
            break

    memory_allocated = torch.cuda.memory_allocated()  # Memory usage in bytes
    total_memory = torch.cuda.get_device_properties(0).total_memory
    memory_percentage = (memory_allocated / total_memory) * 100

    # Simple heuristic for stress level
    if memory_percentage > 90:
        sl = "Very High"
    elif memory_percentage > 70:
        sl = "High"
    elif memory_percentage > 50:
        sl = "Medium"
    else:
        sl = "Low"

    ranking = iterations / elapsed_time

    pps = tensor_size ** 2 / elapsed_time

    return iterations, elapsed_time, ranking, sl, pps, memory_allocated, memory_percentage, total_memory

def stress_test_opencl(duration=60, tensor_size=1024):
    """Stress test for OpenCL-supported GPUs."""
    import pyopencl as cl

    if not cl:
        Text.WriteText("PyOpenCL is not installed. Exiting OpenCL stress test.", FontEnabled=True, Font=TextFont(font_color=Color("red")))
        exit(1)

    platforms = cl.get_platforms()
    if not platforms:
        Text.WriteText("No OpenCL platforms found. Exiting OpenCL stress test.", FontEnabled=True, Font=TextFont(font_color=Color("red")))
        exit(1)

    device = platforms[0].get_devices(device_type=cl.device_type.GPU)[0]
    context = cl.Context(devices=[device])
    queue = cl.CommandQueue(context)

    start_time = time.time()
    elapsed_time = 0
    iterations = 0
    ranking = 0
    sl = ""
    pps = 0

    # Simple kernel code
    kernel_code = """
    __kernel void matmul(__global float* A, __global float* B, __global float* C, int N) {
        int row = get_global_id(0);
        int col = get_global_id(1);
        float sum = 0;
        for (int k = 0; k < N; k++) {
            sum += A[row * N + k] * B[k * N + col];
        }
        C[row * N + col] = sum;
    }
    """
    program = cl.Program(context, kernel_code).build()
    matmul_kernel = program.matmul

    while elapsed_time < duration:
        try:
            # Allocate buffers for the matrices
            A = cl.Buffer(context, cl.mem_flags.READ_WRITE, size=tensor_size * tensor_size * 4)
            B = cl.Buffer(context, cl.mem_flags.READ_WRITE, size=tensor_size * tensor_size * 4)
            C = cl.Buffer(context, cl.mem_flags.READ_WRITE, size=tensor_size * tensor_size * 4)

            import ctypes
            # Explicitly cast tensor_size to int or size_t as expected by OpenCL
            matmul_kernel.set_args(A, B, C, ctypes.c_size_t(tensor_size))

            # Enqueue kernel and execute
            global_size = (tensor_size, tensor_size)
            cl.enqueue_nd_range_kernel(queue, matmul_kernel, global_size, None)

            # Synchronize and clear buffers
            queue.finish()
            elapsed_time = time.time() - start_time
            iterations += 1
        except cl.RuntimeError as e:
            Text.WriteText(f"OpenCL runtime error: {e}", FontEnabled=True, Font=TextFont(font_color=Color("red")))
            exit(1)

    memory_allocated = None
    memory_percentage = None

    if clinfo:
        result = subprocess.run(["clinfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  # Memory usage in bytes
        out = None

        if result != 0:
            Text.WriteText(f"\n{result.stderr}", FontEnabled=True, Font=TextFont(font_color=Color("red")))
        else:
            out = result.stdout

        if out:
            for line in out.splitlines():
                if "used memory" in line.lower():
                    memory_allocated = int(line.lower().split(":")[1].strip()[0])
    else:
        memory_allocated = device.global_mem_cache_size

    total_memory = device.global_mem_size # Not accurate

    if not memory_allocated == None:
        memory_percentage = (memory_allocated / total_memory) * 100

        # Simple heuristic for stress level
        if memory_percentage > 90:
            sl = "Very High"
        elif memory_percentage > 70:
            sl = "High"
        elif memory_percentage > 50:
            sl = "Medium"
        else:
            sl = "Low"
    else:
        memory_allocated = "Unknown"
        memory_percentage = "Unknown"
        sl = "Unknown"

    ranking = iterations / elapsed_time

    pps = tensor_size ** 2 / elapsed_time

    return iterations, elapsed_time, ranking, sl, pps, memory_allocated, memory_percentage, total_memory


Screen.ClearScreen()
Cursor.MoveCursor(0, 0)
Text.WriteText(f"Initializing Stress-Test for GPU:[{get_gpu_type()}] ...", FontEnabled=True, Font=TextFont(font_color=Color("yellow")))
Cursor.MoveCursor(0, 3)
Text.WriteText("Checking Required Modules..." , FontEnabled=True, Font=TextFont(font_color=Color("yellow")))

from importlib import util

time.sleep(1)

rq_mod = ""

if get_gpu_type().lower() == "nvidia":
    rq_mod = "torch"
elif get_gpu_type().lower() in ["intel uhd", "amd"]:
    rq_mod = "pyopencl"

if util.find_spec("torch") and get_gpu_type().lower() == "nvidia":
    Cursor.MoveCursor(0, 3)
    Text.WriteText("All Required Modules Present!" , FontEnabled=True, Font=TextFont(font_color=Color("green")))
elif util.find_spec("pyopencl") and get_gpu_type().lower() in ["intel uhd", "amd"]:
    Cursor.MoveCursor(0, 3)
    Text.WriteText("All Required Modules Present!", endl="\n", FontEnabled=True, Font=TextFont(font_color=Color("green")))
    try:
        out = subprocess.run(["clinfo"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if out != 0:
            Text.WriteText(f"[clinfo] not present. Download [clinfo] to run this program with better accuracy on [{get_gpu_type()}]", FontEnabled=True, Font=TextFont(font_color=Color("yellow")))
            clinfo = False
            time.sleep(4)
    except FileNotFoundError:
        Text.WriteText(f"[clinfo] not present. Download [clinfo] to run this program with better accuracy on [{get_gpu_type()}]", FontEnabled=True, Font=TextFont(font_color=Color("yellow")))
        clinfo = False
        time.sleep(4)
else:
    Cursor.MoveCursor(0, 3)
    Text.WriteText(f"Required Module [{rq_mod}] not Present!" , FontEnabled=True, Font=TextFont(font_color=Color("red")))
    time.sleep(0.5)
    Cursor.MoveCursor(0, 4)
    out = Text.InputText(f"Do you want to attempt auto install [{rq_mod}]? (y/n): " , endl=None, FontEnabled=True, Font=TextFont(font_color=Color("blue")))
    if out.lower() == "n":
        Screen.ClearScreen()
        Cursor.MoveCursor(0, 0)
        exit(1)
    elif out.lower() == "y":
        try:
            os.system(f"pip install {rq_mod}")
        except Exception as e:
            Cursor.MoveCursor(0, 4)
            Text.WriteText("Exception during auto install ->\n", e, FontEnabled=True, Font=TextFont(font_color=Color("red")))
            exit(1)

        Screen.ClearScreen()
        Cursor.MoveCursor(0, 0)
        Text.WriteText(f"Initialized Stress-Test for GPU:[{get_gpu_type()}]: Completed", FontEnabled=True, Font=TextFont(font_color=Color("green")))
        Cursor.MoveCursor(0, 2)
        Text.WriteText("Re-Running Program...", FontEnabled=True, Font=TextFont(font_color=Color("yellow")))
        time.sleep(1)
        try:
            os.system(f"python {os.path.relpath(__file__)}")
        except Exception:
            os.system(f"py {os.path.relpath(__file__)}")
    else:
        Screen.ClearScreen()
        Cursor.MoveCursor(0, 0)
        exit(1)

Screen.ClearScreen()
Cursor.MoveCursor(0, 0)
Text.WriteText(f"Initialized Stress-Test for GPU:[{get_gpu_type()}] ...", FontEnabled=True, Font=TextFont(font_color=Color("green")))

Cursor.MoveCursor(0, 2)
Text.WriteText("Starting Stress-Test...", FontEnabled=True, Font=TextFont(font_color=Color("yellow")))
Cursor.MoveCursor(0, 3)

iterations = 0
elapsed_time = 0
ranking = 0
stress_levels = 0
pps = 0
memAll = None
memPer = None
TotalMem = None
type_ = ""

dur = Text.InputText("Duration of test in seconds (Leave for default 60 seconds): ", endl=None, FontEnabled=True, Font=TextFont(font_color=Color("blue")))
if dur == "":
    dur = "60"
while not dur.isdigit():
    Screen.ClearLine(3)
    Cursor.MoveCursor(0, 3)
    dur = Text.InputText("Invalid input! Please enter a number or leave for default: ", endl=None, FontEnabled=True, Font=TextFont(font_color=Color("blue")))
    if dur == "":
        dur = "60"

dur = int(dur)

Screen.ClearLine(3)
Cursor.MoveCursor(0, 3)
Text.WriteText(f"Duration set to [{dur}] seconds.", endl="\n", FontEnabled=True, Font=TextFont(font_color=Color("green")))

tensor = Text.InputText("Tensor of test (Leave for default 1024/3000): ", endl=None, FontEnabled=True, Font=TextFont(font_color=Color("blue")))
if tensor == "":
    if get_gpu_type().lower() == "nvidia":
        tensor = "3000"
    elif get_gpu_type().lower() in ["intel uhd", "amd"]:
        tensor = "1024"
while not tensor.isdigit():
    Screen.ClearLine(4)
    Cursor.MoveCursor(0, 4)
    tensor = Text.InputText("Invalid input! Please enter a number or leave for default: ", endl=None, FontEnabled=True, Font=TextFont(font_color=Color("blue")))
    if tensor == "":
        if get_gpu_type().lower() == "nvidia":
            tensor = "3000"
        elif get_gpu_type().lower() in ["intel uhd", "amd"]:
            tensor = "1024"

tensor = int(tensor)

Screen.ClearLine(4)
Cursor.MoveCursor(0, 4)
Text.WriteText(f"Tensor set to [{tensor}].", endl="\n", FontEnabled=True, Font=TextFont(font_color=Color("green")))

try:
    if get_gpu_type().lower() == "nvidia":
        tensor = 3000
        iterations, elapsed_time, ranking, stress_levels, pps, memAll, memPer, TotalMem = stress_test_torch(dur, tensor)
        type_ = "PyTorch"
    elif get_gpu_type().lower() in ["intel uhd", "amd"]:
        iterations, elapsed_time, ranking, stress_levels, pps, memAll, memPer, TotalMem = stress_test_opencl(dur, tensor)
        type_ = "PyOpenCL"
except Exception as e:
    Text.WriteText(e, FontEnabled=True, Font=TextFont(font_color=Color("red")))
    exit(1)

time.sleep(1)

Screen.ClearScreen()
Cursor.MoveCursor(0, 0)
Text.WriteText(f"Initialized Stress-Test for GPU:[{get_gpu_type()}]: Completed", FontEnabled=True, Font=TextFont(font_color=Color("green")))

Cursor.MoveCursor(0, 2)
Text.WriteText(f"Stress-Test: Completed using -> [{type_}]\nResults ->\n\tIterations: {iterations}\n\tElapsed Time: {elapsed_time:.2f} Seconds\n\tStress Levels: {stress_levels}\n\tPixel Per Second (Estimated): {pps}\n\tTotal Memory: {TotalMem / (1024**3):.2f} GB\n\tMemory Usage: {memPer:.2f}%\n\tMemory Allocated: {memAll / (1024**3):.2f} GB\n\n\tOverall Ranking: {ranking}", FontEnabled=True, Font=TextFont(font_color=Color("green")))