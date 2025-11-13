source_file = 'input.txt'
destination_file = 'output.txt'
with open(source_file, 'r', encoding='utf-8') as src:
    content = src.read()
with open(destination_file, 'w', encoding='utf-8') as dest:
    dest.write(content) 
