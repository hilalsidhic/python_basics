# i=0
# while i<10:
#     i += 1
#     print(i)
row = int(input("input a number"))
i = 1
line = row
while i <= line:
    print((row * ' ') + i * "   *  ")
    row = row - 1
    i = i + 1