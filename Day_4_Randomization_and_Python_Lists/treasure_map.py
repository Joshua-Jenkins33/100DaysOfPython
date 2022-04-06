# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
x = int(position[0])
y = int(position[1])

if y == 1:
    if x == 1:
        row1 = ["X","⬜️","⬜️"]
    elif x == 2:
        row1 = ["⬜️","X","⬜️"]
    else:
        row1 = ["⬜️","⬜️","X"]
elif y == 2:
    if x == 1:
        row2 = ["X","⬜️","⬜️"]
    elif x == 2:
        row2 = ["⬜️","X","⬜️"]
    else:
        row2 = ["⬜️","⬜️","X"]
else:
    if x == 1:
        row3 = ["X","⬜️","⬜️"]
    elif x == 2:
        row3 = ["⬜️","X","⬜️"]
    else:
        row3 = ["⬜️","⬜️","X"]

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

'''
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
'''