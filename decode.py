def decode(password):
    newpassword = ''
    for num in password:
        newpassword += str(int(num) - 3)
    return newpassword

