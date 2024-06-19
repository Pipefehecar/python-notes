
if __name__ == '__main__':
    file1 = open('../sample.text', 'wt') # writes text, deleting old content
    file2 = open('../sample.text', 'rt') # read text
    file3 = open('../sample.text', 'at') # append
    file4 = open('../sample_new1.text', 'xt') # create new file, raises error if exists
    # t means text mode, b means binary mode
    file5 = open('../sample.text', 'wb')
    file6 = open('../sample.text', 'rb')
    file7 = open('../sample.text', 'ab')
    file8 = open('../sample_new2.text', 'xb')

with('../sample.text', 'rt') as file:
    text : str = file.read(10) # num of characters
    print(text)


