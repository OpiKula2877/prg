import re
class EthFrame:
    def __init__(self, dmac, smac, type, payload, fcs=None):
        
        if not self.is_valid_mac(dmac):
            raise ValueError(f"Invalid destination MAC address: {dmac}")
        if not self.is_valid_mac(smac):
            raise ValueError(f"Invalid source MAC address: {smac}")
        
        self.dmac = dmac
        self.smac = smac
        self.type = type
        self.payload = payload