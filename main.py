import shlex

print('Welcome to UNEC Kabinet!')
print('Use - `help` to see all available commands')

accounts = {}

while True:
  cmd, *args = shlex.split(input('> '))

  if cmd=='exit':
    break

  elif cmd=='help':
    print("Commands:")
    print(' exit - Exit the program')
    print(' help - print all available commands')
    print(' login <username> <password> - login to account')
    print(' list - list all accounts')
    print(' delete <username> <password> - delete account')
    print(' register - create new account')

  elif cmd=='login':
    if len(args) < 2:
      print("Usage: login <username> <password>")
    else:
      username, password = args
      if username in accounts and accounts[username] == password:
        print('Successful login. %s, Welcome!' % username)
      else:
        print('Login failed. Invalid username or password')

  elif cmd=='delete':
    if len(args) < 2:
      print("Usage: delete <username> <password>")
    else:
      username, password = args
      if username in accounts and accounts[username] == password:
        del accounts[username]
        print('Account "%s" successfully deleted!' % username)
      else:
        print('Delete failed. Invalid username or password')

  elif cmd=='register':
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    accounts[new_username] = new_password
    print('Account "%s" successfully created!' % new_username)
  
  elif cmd=='list':
    n = 0
    for username, password in accounts.items():
      n += 1
      print(str(n) + ') ' + username)

  else:
    print('Unknown command: {}'.format(cmd))
