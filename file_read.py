file = open("./testmode.txt", "r")

while True:
    data = file.readline()
    print(data)
    if data == "":
        break

file.close()
