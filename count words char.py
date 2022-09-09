word_count = 0
char_count = 0
usr_input = input("Enter a string : ")
s= usr_input.split()
word_count = len(s)
for word in s:
    char_count += len(word)
print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))
