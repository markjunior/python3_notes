with open('file_io.txt', 'w') as f:
    for i in ['first', 'second', 'third', 'fourth']:
        f.write(f'This is the {i} line...\n')

if __name__ == '__main__':
    file = open('file_io.txt')
    file.seek(3)
    print(file.readline())
    print(file.read())
    file.seek(3)
    print(file.readlines())
    file.close()

    print('-------------------------------')
    # the file_io.txt has to be an existing file if using 'r+'
    with open('file_io.txt', 'r+') as f:
        # start from index 0
        f.write('added first line\n')  # cover the content
        f.truncate()
        print(f.read())
        f.seek(0)
        print(f.read())
        f.seek(10000)
        f.write('added second line')
        f.seek(0)
        print(f.read())
