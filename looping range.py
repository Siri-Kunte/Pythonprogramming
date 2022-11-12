#Finding the sum of numbers between a given range (start point,end point)
start_point = int(input("Enter the start point:"))
endpoint = int(input("Enter the end point:"))
sum_of_numbers = 0
for i in range(start_point,endpoint):
    sum_of_numbers = sum_of_numbers + i
print("The sum of numbers between {} and {} is {}".format(start_point,endpoint,sum_of_numbers))