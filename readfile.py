


employee_File = open("python/employee.txt", "r")
#open("employee.txt", "a")
#open("employee.txt", "w")
#open("employee.txt", "r+")
for employee in employee_File.readlines():
    print(employee)



print(employee_File.readlines())

print(employee_File.readable())
print(employee_File.readline())
print(employee_File.readline())
print(employee_File.read())








employee_File.close()









