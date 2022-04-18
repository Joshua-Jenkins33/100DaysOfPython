# pages = 0
# print(f"Pages: {pages}")
# word_per_page = 0
# print(f"Words per page: {word_per_page}")
# pages = int(input("Number of pages: "))
# print(f"Pages after input: {pages}")
# word_per_page == int(input("Number of words per page: ")) # there's a conditional operator, not an assignment one; == should be =
# print(f"Words per page after input: {word_per_page}")
# total_words = pages * word_per_page
# print(f"Total Words: {total_words}")

# =======================================================================================
# FIXED CODE
# =======================================================================================
# pages = 0
# print(f"Pages: {pages}")
# word_per_page = 0
# print(f"Words per page: {word_per_page}")
# pages = int(input("Number of pages: "))
# print(f"Pages after input: {pages}")
# word_per_page = int(input("Number of words per page: ")) # there's a conditional operator, not an assignment one; == should be =
# print(f"Words per page after input: {word_per_page}")
# total_words = pages * word_per_page
# print(f"Total Words: {total_words}")



def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])