"""
彩票
"""
import random

list_ticket = []
while len(list_ticket) < 7:
    num_red = random.randint(1, 33)
    if num_red not in list_ticket:
        list_ticket.append(num_red)
num_blue = random.randint(1, 17)
list_ticket.append(num_blue)
print(list_ticket)
