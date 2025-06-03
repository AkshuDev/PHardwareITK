import subprocess
import platform
import importlib

def get_gpu_type():
    try:
        # Check for NVIDIA GPU using nvidia-smi command
        if platform.system() == "Linux":
            try:
                result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    return "NVIDIA"
            except Exception:
                pass
        elif platform.system() == "Windows":
            try:
                result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    return "NVIDIA"
            except Exception:
                pass

        # Check for Intel UHD Graphics
        if platform.system() == "Windows":
            try:
                result = subprocess.run(['wmic', 'path', 'win32_VideoController', 'get', 'name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if b'Intel' in result.stdout:
                    return "Intel UHD"
            except Exception:
                pass

        # Check for AMD GPU
        if platform.system() == "Windows":
            try:
                result = subprocess.run(['wmic', 'path', 'win32_VideoController', 'get', 'name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if b'AMD' in result.stdout:
                    return "AMD"
            except Exception:
                pass

        # For Linux, we can check the /proc directory
        if platform.system() == "Linux":
            try:
                with open('/proc/driver/nvidia/version', 'r') as f:
                    if 'NVIDIA' in f.read():
                        return "NVIDIA"
                with open('/var/log/Xorg.0.log', 'r') as f:
                    log_content = f.read()
                    if 'Intel' in log_content:
                        return "Intel UHD"
                    elif 'AMD' in log_content:
                        return "AMD"
            except Exception:
                pass

    except Exception as e:
        print(f"Error detecting GPU: {e}")

    return "No compatible GPU detected"

# Import the appropriate module based on the GPU type
gpu_type = get_gpu_type()
if gpu_type == "NVIDIA":
    importlib.import_module("GPU.NVIDIA")
elif gpu_type == "Intel UHD":
    importlib.import_module("GPU.IntelUHD")
elif gpu_type == "AMD":
    importlib.import_module("GPU.AMD")
else:
    print("Using CPU or unsupported GPU")