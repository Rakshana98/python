dict1={'key1': 1, 'key2': 3, 'key3': 2}
dict2={'key1': 1, 'key2': 2}
for i in dict1:
    for j in dict2:
        if(i==j):
            if(dict1[i]==dict2[j]):
                print(i,":",dict1[i])
