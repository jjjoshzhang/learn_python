import art

print(art.logo1)

new_bids = True

bid_dic ={}

while new_bids:
    maximum = 0
    name_max = ""
    name = input("What's your name?: ")
    price = int(input("What is your bid?: $"))
    bid_dic[name] = price
    yes_or_no = input("Any other bidders? Type yes or no. \n").lower()
    if yes_or_no == "no":
        new_bids = False
        for key in bid_dic:
            if maximum<bid_dic[key]:
                maximum = bid_dic[key]
                name_max = key
        print(f"The winner is {name_max} with a bid of ${maximum}!")
    else:
        print("\n"*20)


