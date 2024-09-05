print("welcome to pizza online ordering.\nplease input \"y\" if you want to order, otherwise input \"n\"\n")
ans = ["y", "n"]

price = 0
s1 = input("pizza? (price_359): ")
if s1=="y":
    price+=359
s2 = input("chicken? (price_3 pieces for 199): ")
if s2=="y":
    price+=199
s3 = input("pasta? (price_99): ")
if s3=="y":
    price+=99
s4 = input("salad? (price_99): ")
if s4=="y":
    price+=99
s5 = input("coke? (price_25): ")
if s5=="y":
    price+=25

if s1 not in ans or s2 not in ans or s3 not in ans or s4 not in ans or s5 not in ans:
    print("Error")
else:
    print("\ntotal price is", price, "\nthanks")