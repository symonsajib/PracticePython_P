with open('C:\\Users\\Symon\\Desktop\\nameslist.txt', 'r') as f:
    line = f.read()
    name_count = {}

    for name in line.split('\n'):
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    print (name_count)






