# Open the file safely using 'with'
with open('csv_data.txt', 'r') as file:
    lines = file.readlines()

# Remove newline characters and skip the header
lines = [line.strip() for line in lines[1:]]

# Process each line
for line in lines:
    person_data = line.split('#')  # Split by hash

    # Extract and format data
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    # Print formatted output
    print(f'{name} is {age}, studying {degree} at {university}.')

# Example: creating a hash-separated string
sample_csv_value = '#'.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)
