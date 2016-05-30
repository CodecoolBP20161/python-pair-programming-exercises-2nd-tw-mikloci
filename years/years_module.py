from datetime import date


def years(age):
    this_year = date.today().year
    hundred_age = 100 - age + this_year
    return hundred_age


def main():
    name = input('What is your name?: ')
    age = int(input("How old are you?: "))
    age = years(age)
    print("Dear %s you are gonna be 100 years old in %d." % (name, age))
    return age


if __name__ == '__main__':
    main()
