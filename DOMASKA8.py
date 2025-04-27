def login(username, password):
    correct_username = "QWERTY"
    correct_password = "3367"

    assert username == correct_username and password == correct_password, "Невірне ім'я користувача або пароль"
    print("Вхід виконано успішно")

login("QWERTY", "3367")
