def analyze_string(s):
    if len(s) == 0:   #check for empty string
        print("Empty string entered")   #print message on the output screen
        return
    
    print("Length of string:",len(s))   #Print length of string
    print("Reverse string:",s[::-1])   #Print reverse of string

    vowels = "aeiou"
    count = 0   #count vowels in the string
    for char in s.lower():   #convert string to lower case
        if char in vowels:   #check if character is a vowel
            count += 1   #increment count if vowel is found
    print("Number of vowels:", count)   #Print number of vowels in the string

    print("\nCharacter with Position and Negative Index:")
    for i in range (len(s)):
        print("Positive index:", i, "Negative index:", i-len(s), "character:", s[i]) #Print character with positive and negative index

        string = input("Enter a string: ")   #Take input from user
        analyze_string(string)   #Call the function to analyze the string