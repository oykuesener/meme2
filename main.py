import random

words = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_lenght = int(input("Parolaniz kaç haneli olacak?:"))

password = ""

for i in range(pass_lenght):
    password = password + random.choice(words)

print(password)


