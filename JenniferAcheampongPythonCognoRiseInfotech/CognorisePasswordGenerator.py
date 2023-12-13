print("\tPASSWORD\t\tGENERATOR   ")
print(".....................................................")
import random
import string

length = int(input("Enter the desired length of the password: "))
password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
print("Generated Password:", password)