d = {'쥐':{"keywords": '프로듀스 101 정국,지한,형섭,'
    , "limit": 50, "print_urls": True, "format": "jpg", "output_directory": "abc"}}

c = {'고양이':{"keywords": '프로듀스 101 정국,지한,형섭,'
    , "limit": 50, "print_urls": True, "format": "jpg", "output_directory": "abc"}}


d.update(c)

for index, key in enumerate(d.items()):
    print(index, key )