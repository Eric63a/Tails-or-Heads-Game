import random


coin_list = ["Tails(0)", "Heads(1)"]

player = input("please choose Tails(0) or Heads(1) ")

random_coin = random.choice(coin_list)

if player == 0:
    print("Trails")
else:
    print("Heads")

print(random_coin)
