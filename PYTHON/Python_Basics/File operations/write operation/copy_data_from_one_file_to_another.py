read_data = open('Demo_file', 'r')
write_data = open('write_demo', 'w')
for i in read_data:
    write_data.write(i)
