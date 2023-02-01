hammer = '''
 _________________.---.______
 (_(______________(_o o_(____()
              .___.'. .'.___.
              \ o    Y    o /
               \ \__   __/ /
                '.__'-'__.'
                    '''
''''''


print("--+--+-Welcome to The Bid!-+--+--")
print(hammer)
bid_dictionary = {}
bidding_finished = False

def highest_bidder(bidding_record):
      highest_bid = 0
      winner = ""
      for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > highest_bid:
                  highest_bid = bid_amount
                  winner = bidder
      print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
      name = input("What is your name?\n")
      bid_price = int(input("What's your Bid?\n$"))
      bid_dictionary[name] = bid_price
      more_users = input("Is there other users? (Yes/No)\n").lower
      if more_users == "no":
            bidding_finished = True
            highest_bidder(bid_dictionary)

# Não rodou muito bem.