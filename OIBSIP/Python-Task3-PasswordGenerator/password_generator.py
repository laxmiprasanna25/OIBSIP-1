
import random
import string

def generate_password():
    print("\n===== RANDOM PASSWORD GENERATOR =====")

    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")
        return

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += [
        random.choice(characters)
        for _ in range(length - 4)
    ]

    random.shuffle(password)

    print("\nYour generated password is:")
    print("".join(password))


if __name__ == "__main__":
    generate_password()
