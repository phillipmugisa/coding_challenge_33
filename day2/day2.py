
def validPassword():
    validPasswords = []
    with open("./input.txt", "r") as file:
        for password_data in file.readlines():
            #split data into list
            #this will ease getting the password and the checking criteria
            pass_parts = password_data.split(":") 

            password = pass_parts[1].strip() #get user password
            check_data = pass_parts[0].split(" ") #get checking data

            #getting upper and lower limit
            limits = check_data[0].split("-") 
            lower_limit, upper_limit = int(limits[0]), int(limits[1])

            #getting letter we base on while checking
            check_letter = check_data[1] 
            
            if check_letter in password and lower_limit <= password.count(check_letter) <= upper_limit:
                validPasswords.append(password)
            else:
                continue

    return validPasswords

valid_passwords = validPassword()

for pwd in valid_passwords:
    print(pwd)