#string.index(value, start, end)
#string.rindex(value, start, end) -> reverse search

var=10
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
print(sum)
