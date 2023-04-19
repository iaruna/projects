import random
passlen = int(input("Enter the length of password: "))
s="01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print(p)