# Read the input file
with open('channel.txt', 'r') as file: data = file.read()
# Split the data into individual URLs based on whitespace
urls = data.split()
# Join the URLs with a newline character
new_data = '\n'.join(urls)
# Write the result to a new file
with open('channels.txt', 'w') as file:
    file.write(new_data)