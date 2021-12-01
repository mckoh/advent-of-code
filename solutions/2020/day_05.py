
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=5, typ="str")

class SeatFinder:
    
    def __init__(self, data=data):
        self.data = data
        self.rows = list(range(128))
        self.cols = list(range(8))
    
    def _find_seat(self, boarding_card, side_indicators=3):
        r = self.rows.copy()
        c = self.cols.copy()
        
        for char in boarding_card[:-side_indicators]:
            if char == "F":
                r = r[:int(len(r)/2)]
            elif char == "B":
                r = r[int(len(r)/2):]

        for char in boarding_card[-side_indicators:]:
            if char == "L":
                c = c[:int(len(c)/2)]
            elif char == "R":
                c = c[int(len(c)/2):]
                
        return r[0], c[0]
    
    def find_highest(self, multiplier=8):
        
        highest = 0
        
        for card in self.data:
            r, c = self._find_seat(boarding_card=card)
            seat = r*multiplier+c
            
            if seat > highest:
                highest = seat
        
        return highest
    
    def get_seat_list(self, multiplier=8):
        
        seat_list = list()
        for card in self.data:
            r, c = self._find_seat(boarding_card=card)
            seat = r*multiplier+c
            seat_list.append(seat)
        return sorted(seat_list)
    
    def finde_seat(self):
        
        l = self.get_seat_list()
        for i, seat in enumerate(l):
            if l[i+1]-l[i]==2:
                return seat+1

# %%
# Part 1
sf = SeatFinder()
sf.find_highest()

# %%

# Part 2
sf = SeatFinder()
sf.finde_seat()    
