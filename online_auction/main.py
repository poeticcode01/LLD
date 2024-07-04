from auction_entities.auction_manager import AuctionManger
from auction_entities.bidder import Bidder

if __name__ == "__main__":
    acm = AuctionManger("Coal India limited")
    print(f"*****Bidding Manager: {acm} created*****")
    bidder1 =  Bidder(acm,"bidder1")
    bidder2 =  Bidder(acm,"bidder2")
    bidder3 =  Bidder(acm,"bidder3")

    acm.add_bidder(bidder1)
    acm.add_bidder(bidder2)
    acm.add_bidder(bidder3)

    bidder1.make_bidding(100)
    bidder2.make_bidding(200)
    bidder3.make_bidding(300)
