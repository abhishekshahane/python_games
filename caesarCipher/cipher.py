plain = list(input("plaintext: "))
key = int(input("key: "))
for each in plain:
    if each.isupper()==True:
        print(chr((ord(each) + key-65) % 26 + 65),end="")
    elif each.islower()==True:
        print(chr((ord(each) + key - 97) % 26 + 97),end="")
    else:
        print(each,end="")
print()
