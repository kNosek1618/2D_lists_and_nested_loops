
# create a 2D list
twoD_list = [
    [1, 2, 3], #row0
    [4, 5, 6], #row1
    [7, 8, 9], #row2
    [0]        #row3
    #col0
       #col1
          #col2
]

# access to 2D list through 2D index
print(twoD_list[0][0])

print("")

for row in twoD_list:
    for column in row:
       print(column)