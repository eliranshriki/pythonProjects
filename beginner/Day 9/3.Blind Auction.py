import os
import art_Blind_Auction

blind_auction={}
end_bid=False
print(art_Blind_Auction.logo)
while end_bid==False:
  name=input("What is your name? ")
  bid=int(input("What's your bid? "))
  blind_auction[name]=bid
  bidder=input("Are there any other bidders? Type 'yes' or 'no' ")
  if bidder == "yes":
    os.system('clear')
  elif bidder == "no":
    end_bid=True

higher_bidder=""
higher=0

for key in blind_auction:
  if blind_auction[key] > higher:
    higher=blind_auction[key]
    higher_bidder=key
print (f"The winner is {higher_bidder} with a bid of {higher}$ ")

