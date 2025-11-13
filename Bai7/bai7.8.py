my_list = ["Hello", "Python", "World"]
with open('output.txt', 'w', encoding='utf-8') as f:
    for item in my_list:
        f.write(item + '\n')   
print("Đã ghi danh sách vào file output.txt thành công!")
