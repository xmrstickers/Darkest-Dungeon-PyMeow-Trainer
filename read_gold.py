import pyMeow as pm
from time import sleep
from DDOffsets import *



debug = True

#                   initialize:
game_title = "Darkest Dungeon"
game_process = "Darkest.exe"
exists = pm.process_exists(game_process) #are we running game?
if debug:
    print("process_exists: ")
    print(exists)
if not exists:
    print("error: DD not running!")
    sys.exit()

pid = pm.get_process_id(game_process)
if debug:
    print(game_process+" PID = ")
    print(pid)
    print()
if debug:
    print("opening process...")
proc = pm.open_process(pid,game_process,False)
mod = pm.get_module(proc, "darkest.exe")["base"] 
if debug:
    print(game_process+" base address:")
    print(hex(mod))
    print()
    
offsets = DDOffsets(mod)
gold_address = offsets.gold_address() 
gold_offsets = offsets.gold_offsets() 
try:
    gold_addr = pm.pointer_chain_32(proc,gold_address, gold_offsets) #get the dynamic address using pointers (magic)
    GOLD = pm.r_int(proc, gold_addr)
    print(GOLD)
except Exception as e : 
    print("Caught an exception - GOLD:", type(e).__name__)
    print("Sleeping for 2 seconds...")
    sleep(2)
#end gold