with open('5.txt', 'w') as file:
    nums = input('Введите числа через пробел: ')
    file.write(nums)

numbers = []
with open('5.txt', 'r') as file:
    numbers = file.read().strip().split()

summ = 0
for num in numbers:
    summ += int(num)
print(summ)