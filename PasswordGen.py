import string
import random

if __name__ == "__main__":
    # Letter Sets
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    service_name = input("Enter the site: ") #enter the name of the site for which you are generating password
    plen = int(input("Enter the password length: "))

    # Combining all the sets
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    # print(s)
    random.shuffle(s)
    # print (s)

    print("Your password is: ")
    print("".join(s[0:plen]))

    # Saving the password in the file
    file = open("pass.txt", "a")
    file.write(f"\n{service_name} : ")
    file.write("".join(s[0:plen]))
    file.close()

    print("Password has been saved in the file.")
