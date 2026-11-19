
while True:
    password = input("Enter your password: ")

    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    number_check = any(char.isdigit() for char in password)
    special_check = any(char in "!@#$%^&*()_+-=" for char in password)

    count = 0

    if length_check:
        count += 1

    if uppercase_check:
        count += 1

    if lowercase_check:
        count += 1

    if number_check:
        count += 1

    if special_check:
        count += 1

    print("\nPassword Strength:", end=" ")

    if count <= 2:
        print("Weak")
    elif count <= 4:
        print("Medium")
    else:
        print("Strong")

    print("\nMissing requirements:")

    if not length_check:
        print("- At least 8 characters")

    if not uppercase_check:
        print("- One uppercase letter")

    if not lowercase_check:
        print("- One lowercase letter")

    if not number_check:
        print("- One number")

    if not special_check:
        print("- One special character")

    if count == 5:
        print("All security conditions are satisfied!")

    choice = input("\nDo you want to try another password? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you!")
        break
