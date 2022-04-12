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


def main():
    if len(sys.argv) == 1:
        print("panoramix [--address --byte_code] [--function_name --function_hash] [--verbose] [--silent] [--profile]")
        exit(1)

    addr = None
    function_name = None
    function_hash = None
    byte_code = None
    for arg_inx, arg in enumerate(sys.argv):
        if arg=="--address":
            addr = sys.argv[arg_inx+1]
        elif arg=="--byte_code":
            byte_code = sys.argv[arg_inx+1]
        elif arg=="--function_name":
            function_name = sys.argv[arg_inx+1]
        elif arg=="--function_hash":
            function_hash = sys.argv[arg_inx+1]
            
    if byte_code is not None:
        decompilation = decompile_bytecode(byte_code, function_name, function_hash)
    elif addr is not None:
        decompilation = decompile_address(addr, function_name, function_hash)
    else:
        raise ValueError()

    print(decompilation.text)

if __name__ == "__main__":
    main()
