accounts = {}

def print_all_accounts():
    if accounts:
        for account in accounts:
            print(f'{account}: {"*" * len(accounts[account])}')
    else:
        print('Нет сохраненных аккаунтов.')

def create_account():
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    accounts[username] = password
    print(f'Аккаунт {username} создан.')

def login():
    global current_user
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    if username in accounts and accounts[username] == password:
        current_user = username
        print(f'Вы вошли в систему как {current_user}.')
    else:
        print('Неверное имя пользователя или пароль.')

def logout():
    global current_user
    if current_user is not None:
        current_user = None
        print('Вы вышли из системы.')
    else:
        print('Нельзя выйти из системы, так как не были в ней залогинены.')

def delete_account():
    username = input('Введите имя пользователя, которого нужно удалить: ')
    if username in accounts:
        del accounts[username]
        print(f'Аккаунт {username} удален.')
    else:
        print(f'Аккаунт {username} не найден.')

def print_help():
    print('Доступные команды:')
    print('create - создать новый аккаунт')
    print('login - войти в систему')
    print('logout - выйти из системы')
    print('list - вывести список всех аккаунтов')
    print('delete - удалить аккаунт')
    print('help - вывести список доступных команд')
    print('exit - выйти из программы')

print('Добро пожаловать в нашу систему управления аккаунтами!')
print_help()

current_user = None

while True:
    command = input('> ')
    if command == 'create':
        create_account()
    elif command == 'login':
        login()
    elif command == 'logout':
        logout()
    elif command == 'list':
        print_all_accounts()
    elif command == 'delete':
        delete_account()
    elif command == 'help':
        print_help()
    elif command == 'exit':
        break
    else:
        print('Неизвестная команда. Введите help для получения списка доступных команд.')
