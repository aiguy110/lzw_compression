import numpy as np

# Load compressed file
input_nums = []
with open('lzw_compressed.lzw', 'r') as in_file:
    for line in in_file:
        input_nums.append(int(line))

# Add initial entries to the table
table = []
for i in range(256):
    table.append(chr(i))

#

# Start decoding
output_chars = []
old = input_nums.pop(0)
output_chars.append(table[old])
while len(input_nums) > 0:
    new = input_nums.pop(0)
    if new >= len(table):
        s = table[old]
        s += c
    else:
        s = table[new]
    for c in s:
        output_chars.append(c)
    c = s[0]
    table.append(table[old]+c)
    old = new


# Write output to file
with open('lzw_decode.txt', 'w') as out_file:
    for c in output_chars:
        out_file.write(c+'\n')
