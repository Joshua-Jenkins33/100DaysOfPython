##################################################################################################
# READ TO A FILE
##################################################################################################
# file = open("my_file.txt")
with open(r"C:\repos\100DaysOfPython\Day_24\my_code\read_and_write\my_file.txt") as file:
  contents = file.read()
  print(contents)
  # file.close() # file.close() is now unnecessary; we don't have to remember to close our file.



##################################################################################################
# WRITE TO A FILE
##################################################################################################

with open(r"C:\repos\100DaysOfPython\Day_24\my_code\read_and_write\my_file.txt", mode='w') as file:
  file.write("New text.")


##################################################################################################
# WRITE (APPEND) TO A FILE
##################################################################################################

with open(r"C:\repos\100DaysOfPython\Day_24\my_code\read_and_write\my_file.txt", mode='a') as file:
  file.write("New text.")
