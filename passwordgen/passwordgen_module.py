import random, string
def passwordgen():
    password = ""
    key_list = string.ascii_letters + string.digits + string.punctuation
    pass_lenght = 8
    for i in range(pass_lenght):
        next_index = random.randint(0, len(key_list) - 1)
        password += key_list[next_index]
    return password

def main():
    print(passwordgen())


if __name__ == '__main__':
    main()
