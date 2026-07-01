def analyze_string(s):   #function to analyze the string

    print("Length of string:", len(s))   #print the length of the string
    print("Reversed string:", s[::-1])   #print the reversed string

    vowels = "aeiou"     #store all vowels 
    count = 0    #count the number of vowels in the string

    for ch in s.lower():     #convert the string to lowercase
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)   #Display total number of vowels in the string
    print("\nCharacter Positions:")    #print character positions

    for i in range(len(s)):
        print("Character:", s[i],     #current character
             "| Positive Index:", i,  #positive index
             "| Negative Index:", i - len(s))  #negative index
        
text = input("Enter a string: ")   #take input from the user

if text == "":    #check if the string is empty

    print("Empty string is not allowed.")
else:
    analyze_string(text)     #call the function to analyze the string