from bid_art import logo
print(logo)
bid_dic = {}
def bid(name, price):
  bid_dic[name] = price
  
should_end = True
while should_end == True:
  name_bid = input("What's your name ? : \n")
  bid_price = int(input(f"{name_bid} what's your bid ?  $"))
  bid(name = name_bid, price = bid_price)

  restart = input("Type 'yes' There is another person. Otherwise type 'no'. \n").lower()
  if restart == "yes":
      should_end = True
  elif restart == "no":
      should_end = False
      x = max(bid_dic.values())
      for i in bid_dic:
        if x == bid_dic[i]:
          print(f"Congrat highest bid {i} with ${x}") 