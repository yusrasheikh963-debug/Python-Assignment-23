import math  # Import math module
try:
    sentence = input("Enter a sentence: ")  # Take a sentence from the user
    words = sentence.split()  # Split the sentence into words

    unique_words = set(words)  # Store unique words in a set
    sorted_words = sorted(unique_words)  # Sort the unique words

    print("\nUnique Words (Sorted):")   # Display unique words
    for word in sorted_words:
        print(word)

    total_words = len(unique_words)   # Count the total number of unique words
    result = math.pow(total_words, 2)  # Find the square of the total unique words

    print("\nTotal Unique Words:", total_words)    # Display the result
    print("Square of Total Unique Words:", result)

except Exception as e:  # Handle any unexpected errors
    print("Error:", e)