from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .auction_manager import AuctionManager

class Bidder:
    def __init__(self,acm: 'AuctionManger', name: str) -> None:
        self.acm = acm
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def make_bidding(self,amount: int):
        print(f"Bidding for Amount {amount} by {self}")
        self.acm.announce_bidding(self,amount)
        print(f"Done Bidding for Amount {amount} by {self}")

    def receive_new_bidding_info(self,message: str):
        print(f"{self} received: {message}")


        