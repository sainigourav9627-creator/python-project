
name = input("Enter Student Name: ")
city = input("Enter City: ")
marks = float(input("Enter Marks: "))

# String Methods

result1 = name.title()
result2 = name.capitalize()

print(result1)
print(result2)

# String Length

print(len(name))

# Marks Formatting

print(f"Marks: {marks:.2f}")

# First and Last Character

print(name[0])
print(name[-1])

# Character Counting

print(name.count("a"))
print(name.count("o"))


# Sentence Analyzer

a = input("enter the sentence : ")
search_word = input("enter the word to search : ")
replace_word = input("enter replacement word : ")

result4 = a.strip()
result5 = a.split()
result6 = a.count("python")
result8 = a.lower()

result7 = a.replace(search_word, replace_word)

print(result4)
print(result5)
print(result6)
print(len(result5))
print(search_word in a)

result9 = search_word.lower()

print(result9 in result8)
print(result8.count(result9))
print(result8.find(result9))

result10 = result8.count(result9)

result11 = a.startswith(search_word)
result12 = a.endswith(search_word)

print(result11)
print(result12)

result13 = result5
result14 = "-".join(result13)

print(result14)

b = input("enter the sentence : ")

result = b.isalpha()
result1 = b.isdigit()
result2 = b.isalnum()

print(result)
print(result1)
print(result2)

# Final Summary

print("1. Original sentence:", a)
print("2. Total words:", len(result5))
print("3. Search word:", search_word)
print("4. Search word count:", result10)
print("5. Replaced sentence:", result7)
