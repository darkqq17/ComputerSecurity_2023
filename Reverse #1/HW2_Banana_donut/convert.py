# Adjusted code to handle the file content as a single long string representation of a list

with open('./memory_values.txt', 'r') as file:
    # Reading the entire file content as a single string
    file_content = file.read()

# Removing the leading and trailing characters to convert the string into a list format
file_content = file_content.strip("[]\n")

# Splitting the string into a list of items
data_list = file_content.split("', '")

# Extracting the values and storing them in an array
extracted_values = []
for item in data_list:
    # Extracting the part of the string between '\t' and '\n'
    value_str = item.split('\\t')[1].rstrip('\\n')
    # Converting the extracted part to an integer and appending to the list
    try:
        extracted_values.append(int(value_str))
    except ValueError:
        # Handling lines that may not contain valid integer values
        print(f"Skipping invalid value: {value_str}")
print(extracted_values)  # Displaying the first 10 values for brevity
