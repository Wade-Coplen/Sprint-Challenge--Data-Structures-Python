import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
vec = [[names_1], [names_2]]
echo = [name for elem in vec for name in elem]
for i in range(0, len(echo)):    
    for j in range(i+1, len(echo)):    
        if(echo[i] == echo[j]):    
            duplicates.append(echo[j]);   
#for name_1 in names_1:
  #  for name_2 in names_2:
    #    if name_1 == name_2:
    #        duplicates.append(name_1)

#print(vec)    
#a = [[1, 2, 4], [3, 5, 6]]
#b = [i for elem in a for i in elem]
#print(b)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
