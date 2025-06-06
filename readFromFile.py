import tryCatch as ct

employee_image_file = open("image.png","r")
employee_txt_file = open("employees.txt","w")
employee_csv_file = open("employees1.csv","r+")


employee_csv_file.write(employee_txt_file.read())
#print(employee_csv_file.readlines())

#print(employee_csv_file.read())

employee_txt_file.close()
employee_csv_file.close()