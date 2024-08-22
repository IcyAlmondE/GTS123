full = float(input("Input Full Score = "))
real = float(input("Input Real Score = "))

line = "----------------------------"
print(line)
print("--- Calculate Percentage ---")
print(line)
print("Full Score: %.2f" % full)
print("Real Score: %.2f" % real)
print(line)
print("Percentage: %.2f%%" % ((real/full)*100))
print(line)