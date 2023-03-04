database = {
    "unec": "nizami",
    "username": "password",
    "abc": "123"
}

username = input('Username: ')
password = input('Password: ')

logged = username in database and database[username] == password

print(
    "Logged in successfully. Welcome!" if  logged
    else "Login failed. Incorrect username or password."
)
