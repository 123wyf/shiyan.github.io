from itertools import islice
st = open ("存储文件，不要删除！.reiiio","r")
with open("存储文件，不要删除！.reiiio") as f:
    金币 = list(islice(f, 2))
    pass
print(金币[1])
input()
