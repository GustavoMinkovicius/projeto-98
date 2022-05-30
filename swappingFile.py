def swapFileData():
    data_a = open('sample1.txt', 'r')
    print(data_a.read())
    data_b = open('sample2.txt', 'r')
    print(data_b.read())

swapFileData()