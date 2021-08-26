file = open("testmode.txt", "w")
file.write("this is a test")
file.close()

file = open("./testmode.txt", "a")
file.write("\n this is the second sentence")
file.close()

"""
while True:
    data = file.readline()
    print(data)

    if data == "":
        break

file.close()
"""