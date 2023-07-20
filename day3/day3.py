#string.index(value, start, end)
#string.rindex(value, start, end) -> reverse search

'''var=10
for i in range(12):
    for j in range(8,11,1):
        if var%2==0:
            continue
            var+=1
    var+=1
else:
    var+=1
print(var)

for i in 'python':
    if i=='o':
        pass
    print(i)
    
N = int(input("Enter a number: "))

# Initialize the sum variable
sum_digits = 0

# Extract and sum the digits
while N > 0:
    digit = N % 10
    sum_digits += digit
    N //= 10

print("Sum of the digits:", sum_digits)

num=int(input())

num_str=str(num)
sum=0
for digit in num_str:
    sum+=int(digit)
print(sum)'''

 
"""arr = map(int, input().split())
    
new_arr = list(arr)
print(new_arr)
#list(new_arr).sort()
#print(new_arr)

"""

text = input("Enter a text of your choice: ")
letters = []

text = text.lower()
letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the third letter: ").lower())

print("\n")
print("LETTER REPETITIONS")

letter_repetition1 = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print(f"We have found the letter '{letters[0]}' repeated {letter_repetition1} times")
print(f"We have found the letter '{letters[1]}' repeated {letter_repetition2} times")
print(f"We have found the letter '{letters[2]}' repeated {letter_repetition3} times")

print("\n")
print("NUMBER OF WORDS")

words = text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("FIRST AND LAST LETTERS")

first_letter = text[0]
last_letter = text[-1]
print(f"The initial letter is '{first_letter}', the final letter is '{last_letter}'")

print("\n")
print("INVERTED TEXT")

words.reverse()
inverted_text = ' '.join(words)
print(f"If we order your text backwards it will say '{inverted_text}'")

print("\n")
print("LOOKING FOR THE WORD PYTHON")

is_python = 'python' in text
dic = {True: "was", False: "was not"}

print(f"The word 'Python' {dic[is_python]} found in the text")