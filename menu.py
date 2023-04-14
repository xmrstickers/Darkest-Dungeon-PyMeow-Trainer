import pyMeow as pm
from time import sleep
from DDOffsets import *



debug = True

menu_key = 0x2D #windows
    #menu_key = 0xff63 #linux
menu_x = 500
menu_y = 500
menu_width = 500
menu_height = 200
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
    
offsets = DDOffsets(mod) #initialize our offsets - we pass this to functions that read/write to memory 

#   globals 
draw = False #if true, we draw trainer overlay - menu_key toggles this
GOLD = -1
BUSTS = -1
PORTRAITS = -1
DEEDS = -1
CRESTS = -1
SHARDS = -1
#               initialize passed, start overlay
pm.overlay_init(game_title, 60, "Balvand")
def check_key():
    global draw
    if pm.key_pressed(menu_key):
        draw = not draw
        pm.toggle_mouse()
        sleep(0.15)
def refresh_inventory(offsets): 
    global GOLD
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
def write_gold(amount, offsets):
    gold_base = offsets.gold_address() 
    gold_offset = offsets.gold_offsets() 
    try:
        gold_addr = pm.pointer_chain_32(proc,gold_base, gold_offset) #get the dynamic address using pointers (magic)
        pm.w_int(proc,gold_addr, amount)
    except Exception as e : 
        print("Sleeping for 1 second...")
        sleep(1)   
def write_busts(amount, offsets):
    busts_base = offsets.busts_address() 
    busts_offset = offsets.busts_offsets() 
    try:
        busts_addr = pm.pointer_chain_32(proc,busts_base, busts_offset) #get the dynamic address using pointers (magic)
        pm.w_int(proc,busts_addr, amount)
    except Exception as e : 
        print("Sleeping for 1 second...")
        sleep(1)   
def write_portraits(amount, offsets):
    portraits_base = offsets.portraits_address() 
    portraits_offset = offsets.portraits_offsets() 
    try:
        portraits_addr = pm.pointer_chain_32(proc,portraits_base, portraits_offset) #get the dynamic address using pointers (magic)
        pm.w_int(proc,portraits_addr, amount)
    except Exception as e : 
        print("Sleeping for 1 second...")
        sleep(1)   
def write_deeds(amount, offsets):
    deeds_base = offsets.deeds_address() 
    deeds_offset = offsets.deeds_offsets() 
    try:
        deeds_addr = pm.pointer_chain_32(proc,deeds_base, deeds_offset) #get the dynamic address using pointers (magic)
        pm.w_int(proc,deeds_addr, amount)
    except Exception as e : 
        print("Sleeping for 1 second...")
        sleep(1)   
def write_crests(amount, offsets):
    crests_base = offsets.crests_address() 
    crests_offset = offsets.crests_offsets() 
    try:
        deeds_addr = pm.pointer_chain_32(proc,crests_base, crests_offset) #get the dynamic address using pointers (magic)
        pm.w_int(proc,deeds_addr, amount)
    except Exception as e : 
        print("Sleeping for 1 second...")
        sleep(1)   
def write_shards(amount, offsets):
    shards_base = offsets.shards_address() 
    shards_offset = offsets.shards_offsets() 
    try:
        deeds_addr = pm.pointer_chain_32(proc,shards_base, shards_offset) #get the dynamic address using pointers (magic)
        pm.w_int(proc,deeds_addr, amount)
    except Exception as e : 
        print("Sleeping for 1 second...")
        sleep(1)   



            #the main overlay loop
check = True
god_mode = False
while pm.overlay_loop():    
    pm.begin_drawing()
    
    check_key() #check to see if we are toggling the trainer menu or not 
    if not draw: 
        pm.draw_text("[Balvand Trainer] press INSERT to open...", 50, 10, 12, pm.new_color(0,255,0,200))
    elif draw:
        #INSERT KEY WAS PRESSED, SHOW TRAINER    
        window_box = pm.gui_window_box(menu_x, menu_y, menu_width, menu_height, "Balvand") #main GUI         
        if window_box:
            draw = not draw
            pm.toggle_mouse()
            print("X fire") #fires on "close X"
       # pm.load_texture("image.jpg")
        #refresh_inventory(offsets) #pulls from memory using pymeow + DDOffsets.py: gold, busts, portraits, deeds, crests, shards ("spendables")
       # pm.draw_text("INVENTORY:",menu_x+350, menu_y+10, 16, pm.new_color(0,0,0,255))
        #pm.gui_label(menu_x+200, menu_y+30, 150, 150, str(GOLD))  
       # pm.draw_text(str(GOLD),menu_x+200, menu_y+30, 16, pm.new_color(0,255,0,255))
        
        # if pm.gui_dropdown_box( #drop-down menu
            # posX=menu_x+120, posY=menu_y+30,
            # width=80, height=20,
            # text="Def;30;60;120;144;240",
            # id=0
        # ) == 2:
            # print("drop_down #2") 
            
            #GOLD
        gold_input = pm.gui_text_box(posX=menu_x+20, posY=menu_y+30, width=50, height=30, text="1337", id=0)
        gold_input = gold_input.rstrip('\x00') #WORKAROUND
        #print("GOLD_INPUT = "+gold_input)
        try:
           gold_input = int(gold_input)
        except Exception as e : 
           #sleep(1)
           gold_input = 0
           print("caught an exception - gold input:", type(e).__name__)
           print("(make sure you are inputting a number...)")
           
        if pm.gui_button(posX=menu_x+80, posY=menu_y+30, width=80, height=30, text="Set Gold"):
            print("Set Gold: "+str(gold_input))
            write_gold(gold_input, offsets)
            
            # #BUSTS            
        busts_input = pm.gui_text_box(posX=menu_x+20, posY=menu_y+60, width=50, height=30, text="0", id=1)
        busts_input = busts_input.rstrip('\x00') #WORKAROUND
        #print("busts_input = "+busts_input)
        try:
            if busts_input is not '':
                busts_input = int(busts_input)
        except Exception as e : 
           #sleep(1)
           busts_input = 0
           print("caught an exception - busts input:", type(e).__name__)
           print("(make sure you are inputting a number...)")
           
        if pm.gui_button(posX=menu_x+80, posY=menu_y+60, width=80, height=30, text="Set Busts"):
            print("Set Busts: "+str(busts_input))
            write_busts(busts_input, offsets)      
            #PORTRAITS           
        portraits_input = pm.gui_text_box(posX=menu_x+20, posY=menu_y+90, width=50, height=30, text="0", id=2)
        portraits_input = portraits_input.rstrip('\x00') #WORKAROUND
        #print("portraits_input = "+portraits_input)
        try:
            if portraits_input is not '':
                portraits_input = int(portraits_input)
        except Exception as e : 
           sleep(1)
           portraits_input = 0
           print("caught an exception - portraits input:", type(e).__name__)
           print("(make sure you are inputting a number...)")
           
        if pm.gui_button(posX=menu_x+80, posY=menu_y+90, width=80, height=30, text="Set Portraits"):
            print("Set Portraits: "+str(portraits_input))
            write_portraits(portraits_input, offsets)        
            # #DEEDS         
        deeds_input = pm.gui_text_box(posX=menu_x+165, posY=menu_y+30, width=50, height=30, text="0", id=3)
        deeds_input = deeds_input.rstrip('\x00') #WORKAROUND
        #print("deeds_input = "+deeds_input)
        try:
            if deeds_input is not '':
                deeds_input = int(deeds_input)
        except Exception as e : 
           #sleep(1)
           deeds_input = 0
           print("caught an exception - deeds input:", type(e).__name__)
           print("(make sure you are inputting a number...)")
           
        if pm.gui_button(posX=menu_x+225, posY=menu_y+30, width=80, height=30, text="Set Deeds"):
            print("Set Deeds: "+str(deeds_input))
            write_deeds(deeds_input, offsets)        
            #row 2 
            #CRESTS           
        crests_input = pm.gui_text_box(posX=menu_x+165, posY=menu_y+60, width=50, height=30, text="0", id=4)
        crests_input = crests_input.rstrip('\x00') #WORKAROUND
        #print("crests_input = "+crests_input)
        try:
            if crests_input is not '':
                crests_input = int(crests_input)
        except Exception as e : 
           #sleep(1)
           crests_input = 0
           print("caught an exception - portraits input:", type(e).__name__)
           print("(make sure you are inputting a number...)")
           
        if pm.gui_button(posX=menu_x+225, posY=menu_y+60, width=80, height=30, text="Set Crests"):
            print("Set Crests: "+str(crests_input))
            write_crests(crests_input, offsets)        
            #SHARDS           
        shards_input = pm.gui_text_box(posX=menu_x+165, posY=menu_y+90, width=50, height=30, text="0", id=5)
        shards_input = shards_input.rstrip('\x00') #WORKAROUND
        #print("shards_input = "+shards_input)
        try:
            if shards_input is not '':
                shards_input = int(shards_input)
        except Exception as e : 
           #sleep(1)
           shards_input = 0
           print("caught an exception - Shards input:", type(e).__name__)
           print("(make sure you are inputting a number...)")
           
        if pm.gui_button(posX=menu_x+225, posY=menu_y+90, width=80, height=30, text="Set Shards"):
            print("Set Shards: "+str(shards_input))
            write_shards(shards_input, offsets)        
        
                #how do i check box?
        # if check and pm.gui_check_box(menu_x+300, menu_y+30, 30, 30, "God", god_mode):
            # print("check box")
            # #god_mode = not god_mode
            # check = False
        # elif not check and not pm.gui_check_box(menu_x+300, menu_y+30, 30, 30, "God", god_mode):
            # print("check2")
        # elif not check and pm.gui_check_box(menu_x+300, menu_y+30, 30, 30, "God", god_mode):
            # print("check3")
        # else:
            # pm.gui_check_box(menu_x+300, menu_y+30, 30, 30, "God", god_mode)
            # print("check 4")
    pm.end_drawing()
    #sleep(0.15) #too laggy?
    
    
print()
print("closing process...")
pm.close_process(proc)
print()
print(" ~done")