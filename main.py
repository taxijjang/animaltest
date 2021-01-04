from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

limit = 100
print_urls = True
image_format = 'jpg'

arguments = {}
tmp = {}
# # 강아지 (여우상, 늑대상)
# 강아지 = {"keywords": '강다니엘,박보검,엑소 백현,임시완,차은우'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
# 강아지여 = {"keywords": '박보영,수지,아이유,웬디,티파니,한지민,한효주'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'강아지': 강아지})
#
# # 고양이 (사자상, 범상)
# 고양이 = {"keywords": 'BTS 슈가,빅스 레오,시우민,황민현,지코,강동원,JBJ 권현빈,'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
# 고양이여 = {"keywords": '안소희,현아,초아,슬기,아이린'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'고양이': 고양이})
# tmp.update({'고양이': 고양이})
# # 쥐
# 쥐 = {"keywords": '민경훈,윤시윤,이명박,이특,하하,유재석,홍록기,서세원,배영만,독고영재'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'쥐': 쥐})
#
# # 공룡
# 공룡 = {"keywords": '육성재,공유,류준열,김우빈,홍종현,탑,동해,이민기'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'공룡': 공룡})
#
# # 호랑이
# 호랑이 = {"keywords": '김윤석,김진태,노태우,백윤식,윤석열,이덕화,임재범,천호진,최민식'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'호랑이': 호랑이})
#
# # 곰
# 곰 = {"keywords": '조진웅,마동석,안재홍,박성웅,김윤석'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'곰': 곰})
#
# # 돼지
# 돼지 = {"keywords": '강호동,김준현,정형돈,백종원,싸이'
#     , "limit": limit, "print_urls": print_urls, "format": image_format}
#
# arguments.update({'돼지': 돼지})

# 원숭이
원숭이 = {"keywords": 'MC몽'
    , "limit": limit, "print_urls": print_urls, "format": image_format}

arguments.update({'원숭이': 원숭이})

for key, value in arguments.items():
    value.update({'output_directory': key})
    paths = response.download(value)  # passing the arguments to the function
    print(paths)  # printing absolute paths of the downloaded images
