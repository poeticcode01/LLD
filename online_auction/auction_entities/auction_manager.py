from typing import List
from .bidder import Bidder

class AuctionManger:
    def __init__(self,name: str):
        self.bidder_list: List[Bidder] = []
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def announce_bidding(self,cur_biider: Bidder,amount: int):
        message = f"New bidding by {cur_biider.name} for Amount: {amount} "
        print(f"Acknowledged bidding for Amount {amount} by {cur_biider}")
        for each_bidder in self.bidder_list:
            if each_bidder.name != cur_biider.name:
                print(f"Broadcasting to bidder:  {each_bidder}")
                each_bidder.receive_new_bidding_info(message)
        print(f"Done broadcasting to all bidders")
                
        


    def add_bidder(self,new_bidder: Bidder):
        self.bidder_list.append(new_bidder)
        print(f"{new_bidder} added to the list ")

