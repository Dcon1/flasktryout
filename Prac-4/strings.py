"""
I ran in to some dificulties with adding to the list - using the append first I would end up with duplicate entries, I
added in an if statement at line 20 to add to the list prior to appending this fixed the issue. Is there a mmore effieciant way to do this?
Also, Is there a more efficiant way to search for duplicates in a list?

"""

def main():
    user_input = input("Please enter any amount of strings this program will stop if an empty string is entered: ")
    strings = [user_input]
    duplicate_strings = []
    while user_input != "":
        user_input = input("Enter string: ")
        if user_input == "":
            break
        strings.append(user_input)
    for i in range(0,len(strings), 1):
        #print(strings[i],strings[:i], strings[i+1:])
        if strings[i] in strings[:i] or strings[i] in strings[i+1:]:
            if len(duplicate_strings) > 0:
                duplicate_strings = [strings[i]]
            else:
                duplicate_strings.append([strings[i]])
    if len(duplicate_strings) == 0:
        print("no duplicate strings found")
    else:
        print("duplicate strings found: {}".format(duplicate_strings))

main()