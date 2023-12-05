import random, string


def get_password(length):
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(length))
    return password

if __name__ == '__main__':
    print(get_password(10))
