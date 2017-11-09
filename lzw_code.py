import numpy as np

# Load the file
input_chars = []
with open('lzw_input.txt', 'r') as in_file:
    for line in in_file:
        input_chars.append(line.strip())

# Add initial entries to the table
table = []
for i in range(256):
    table.append(chr(i))

# Start coding
output_nums = []
p = input_chars.pop(0)
while len(input_chars) > 0:
    c = input_chars.pop(0)
    if p+c in table:
        p += c
    else:
        output_nums.append(table.index(p))
        table.append(p+c)
        p = c
output_nums.append(table.index(p))


# Write code to file
with open('lzw_compressed.lzw', 'w') as out_file:
    for n in output_nums:
        out_file.write(str(n)+'\n')
