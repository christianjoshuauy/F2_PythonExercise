num = int(input('Enter a number: '))
max = num % 10; min = max
num = int(num / 10)
digits = 1
while num > 0:
    rem = num % 10
    if rem > max:
        max = rem
    if rem < min:
        min = rem
    num = int(num / 10)
    digits += 1

print(f'Number of digits in the given number is: {digits}')
print(f'Smallest number is: {min}')
print(f'Highest number is: {max}')
