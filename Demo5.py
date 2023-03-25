def mix(dict1,dict2):
    res={**dict1,**dict2}
    return res

dict1={1:3,2:5}
dict2={1:5,3:7}
dict3=mix(dict1,dict2)
print(dict3)