# Darkest-Dungeon-PyMeow-Trainer

basic/crude trainer I made to practice with the PyMeow library. 

The DDOffsets file could be useful to you when making your own hack, even outside of PyMeow. 

To use: 

ensure you have 64-bit python installed and [PyMeow](https://github.com/qb-0/pyMeow/)

Run the game and get to the caravan/inventory screen where you can see all your gold/portraits/deeds/crests etc. 

Download all python files into a folder and navigate there. On Windows, you open command prompt and then do `cd C:\Hacks\` where the `Hacks` folder contains the python files.

Simply run `menu.py` and then press INSERT to toggle the overlay which lets you edit your inventory. You can also run `read_gold.py` as a check to see if the hack is up to date/working - this simply prints the player's gold to command prompt as a way for us to easily check if `DDOffsets.py` (the file containing all of the Darkest Dungeon memory offsets) is working with the current game build. 

Yes, your screen will go black when the overlay comes up. Simply "click back into the game" and provide focus to the game menu when you are done with the overlay, even if the screen goes black, and all is fine. These overlay issues only happen in Darkest Dungeon to me so far, and I am not sure how to fix it. 

In Action: 
![image](https://user-images.githubusercontent.com/89484281/232171157-0c592ccf-02b5-4a2c-8af2-793002fc4d27.png)

Known Issues: 

The Overlay makes the screen go black. This only happens to me in Darkest Dungeon and may not be something I can fix without altering PyMeow source. Any advice appreciated, though. 

Updating the game "breaks" the hack - this is expected and unavoidable as I cannot predict changes made to the game binary; all memory-based hacks deal with this logisitcal hurdle. 
If DDOffsets is broken, open an issue and I can fix it easily. Or you could fix it yourself and submit a PR :)  

