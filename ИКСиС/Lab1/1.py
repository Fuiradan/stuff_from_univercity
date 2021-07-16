import requests
s = requests.session()
email = 'maxfedorenko86@mail.ru'
password = 'Qwerty123qwerty'
user_data = {'email': email, 'password': password}
url = "https://ru.stackoverflow.com/users/login"

response = s.post(url, data=user_data)
file = open('11.html', 'wb')
file.write(response.content)
file.close()

