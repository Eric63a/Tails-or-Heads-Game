import random



coin_list = ["Heads","Tails"]

player = input("please choose Heads(1) or Tails(0) ")

random_coin = random.choice(coin_list)

if player == "Heads" or "Tails":
    print(f"Heads or Tails!!?? {random_coin}!")
else:
    exit()


