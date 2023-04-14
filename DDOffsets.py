
class DDOffsets:
    """
    Contains hardcoded offsets and magic numbers necessary to access the memory of Darkest Dungeon (Darkest.exe)
    """
    def __init__(self, game_base_address):
        self.game_base_address = game_base_address
        self.SPENDABLES_ADDRESS = 0x01C4C168 #static "spendables" (gold, busts, portrasits, deeds, crests, shards) inventory offset
        self.GOLD_OFFSETS = [0x0, 0x1C0, 0x4, 0xB8, 0xBAC, 0x0] #gold pointer chain
        self.BUSTS_OFFSETS = [0x0, 0x1C0, 0x4, 0xB8, 0xBAC, 0x48] #busts pointer chain
        self.PORTRAITS_OFFSETS = [0x0, 0x1C0, 0x4, 0xB8, 0xBAC, 0x90] #.. .. .. 
        self.DEEDS_OFFSETS = [0x0, 0x1C0, 0x4, 0xB8, 0xBAC, 0xD8]
        self.CRESTS_OFFSETS =[0x0, 0x1C0, 0x4, 0xB8, 0xBAC, 0x120]
        self.SHARDS_OFFSETS = [0x0, 0x1C0, 0x4, 0xB8, 0xBAC, 0x168]
    
    # GOLD 
    def gold_address(self):
        return self.game_base_address + self.SPENDABLES_ADDRESS
    def gold_offsets(self):
        return self.GOLD_OFFSETS

    #BUSTS
    def busts_address(self):
        return self.game_base_address + self.SPENDABLES_ADDRESS
    def busts_offsets(self):
        return self.BUSTS_OFFSETS
    # PORTRAITS 
    def portraits_address(self):
        return self.game_base_address + self.SPENDABLES_ADDRESS
    def portraits_offsets(self):
        return self.PORTRAITS_OFFSETS
    # DEEDS 
    def deeds_address(self):
        return self.game_base_address + self.SPENDABLES_ADDRESS
    def deeds_offsets(self):
        return self.DEEDS_OFFSETS
    # CRESTS 
    def crests_address(self):
        return self.game_base_address + self.SPENDABLES_ADDRESS
    def crests_offsets(self):
        return self.CRESTS_OFFSETS
    # SHARDS 
    def shards_address(self):
        return self.game_base_address + self.SPENDABLES_ADDRESS
    def shards_offsets(self):
        return self.SHARDS_OFFSETS
