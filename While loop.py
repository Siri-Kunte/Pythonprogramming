#While loop to find the sum of first n numbers
end_point = int(input("Enter the value of end_point: "))
sum_of_numbers = 0
i = 0
while i<= end_point:
    sum_of_numbers = sum_of_numbers + i
    i = i+1
print("The sum of first {} whole numbers is{}". format(end_point,sum_of_numbers))