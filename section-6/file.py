my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w')# WHAT EVER YOU WRITE BECOMING NEW CONTENT
my_file_writing.write(user_name)
my_file_writing.close



