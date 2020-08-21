usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
users_username = input("Username:")
for i in range(len(usernames)-1):
    if users_username == usernames[i]:
        print("Access Granted")
        quit()

print("Access Declined")