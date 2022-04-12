import cProfile
import logging
import sys

import coloredlogs
import timeout_decorator

from panoramix.decompiler import decompile_address, decompile_bytecode
from panoramix.utils.helpers import C

logger = logging.getLogger(__name__)

if "--verbose" in sys.argv:
    log_level = logging.DEBUG
elif "--silent" in sys.argv:
    log_level = logging.CRITICAL
elif "--errors" in sys.argv:
    log_level = logging.ERROR
else:
    log_level = logging.INFO

logging.getLogger("panoramix.matcher").setLevel(logging.INFO)

coloredlogs.install(
    level=log_level,
    fmt="%(asctime)s %(name)s %(message)s",
    datefmt="%H:%M:%S",
    field_styles={"asctime": {"color": "white", "faint": True}},
)

def print_decompilation(addr):
    assert len(addr)==42
    
    function_name = None
    for arg_inx, arg in enumerate(sys.argv):
        if arg=="--function_name":
            function_name = sys.argv[arg_inx+1]
            break
           
    decompilation = decompile_bytecode(addr, function_name)

    print(decompilation.text)

def main():
    if len(sys.argv) == 1:
        print("panoramix --address --function_name")
        exit(1)
    
    for arg_inx, arg in enumerate(sys.argv):
        if arg=="--address":
            addr = sys.argv[arg_inx+1]
            print_decompilation(addr)

if __name__ == "__main__":
    main()
