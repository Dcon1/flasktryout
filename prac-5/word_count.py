text = str(input("Please enter a string of text and I will count the words"))
word_list = text.split()
word_dict = {}
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
for word in word_dict:
    print("{} : {}".format(word, word_dict[word]))