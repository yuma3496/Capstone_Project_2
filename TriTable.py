# ================= Compulsory Task =================
# Write a program that uses nested for loops to create the following number pyramid.
# 1
# 2     4       
# 3     6       9
# 4     8       12      16
# 5     10      15      20      25
# 6     12      18      24      30      36
# 7     14      21      28      35      42      49
# 8     16      24      32      40      48      56      64
# 9     18      27      36      45      54      63      72      81
# ================= Compulsory Task =================

# Ask user input for the number of rows
max_range = int(input("Enter the number of lines you want to create: "))

# Create nested loops and print it out
for i in range(1, max_range + 1):
    x = " "
    for j in range(1, i + 1):
        x = x + str(i * j) + " "
    print(x)