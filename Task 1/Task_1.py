input = input('Enter elements of a list separated by space: \n')
list = input.split()
sum = 0
for num in list:
    num = int(num)
    if num%2!=0:
        sum = sum+num
print('Sum of odd numbers in the list is:',sum)
