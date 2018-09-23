import getpass

username = input("username:")
password = getpass.getpass("password:")
#print(type(password))

_username = "Thomas"
_password = "123"
#print(type(_password))

if _username == username and _password == password:
    print("welcome user {_name} login...".format(_name=username))
else:
    print("invaild username of password!")
    
    
    
