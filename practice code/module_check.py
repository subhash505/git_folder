import importlib

def is_module_installed(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False

# Usage example
module_name = "memory_profile"
if is_module_installed(module_name):
    print(f"{module_name} is installed.")
else:
    print(f"{module_name} is not installed.")
