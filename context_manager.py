file = open("hello.txt", "w")
file.write("Hello, I am a context manager!")
file.close()

file = open("hello.txt", "w")
file.write("Testing a few things")
print(file)
file.close()

file = open("hello.txt", "w")
file.write("Hello, I am a context manager!")
file.close()

with open("hello.txt", mode="r") as file:
    print(file)


