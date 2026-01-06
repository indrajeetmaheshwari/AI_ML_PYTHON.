def create_file():
    name = input("Enter file name: ")
    open(name, "w")
    print("File created")

def write_file():
    name = input("Enter file name to write in it: ")
    text = input("Enter text: ")
    f = open(name, "a")
    f.write(text + "\n")
    f.close()
    print("Written successfully")

def read_file():
    name = input("Enter file name to read data from it: ")
    f = open(name, "r")
    print(f.read())
    f.close()
