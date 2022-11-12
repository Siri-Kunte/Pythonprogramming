#Finding the sum of first "n" whole number using for loop
endpoint = int(input("Enter the value of n:"))
sum_of_numbers = 0
for i in range(endpoint):
    print("Sum of number value is:",sum_of_numbers)
    print("Index i value is:",i)
    sum_of_numbers = sum_of_numbers + i
print("The sum of first {} whole numbers is {}". format(endpoint,sum_of_numbers))