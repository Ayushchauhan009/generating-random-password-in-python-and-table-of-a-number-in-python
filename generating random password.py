import random
passlen=int(input("Enter the length of password:"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNIOPQRSTUVWXYZ!@#$%^&*()"
p="".join(random.sample(s,passlen))
print(p)