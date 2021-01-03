import face_recognition
from PIL import Image
import os

print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))

categories = os.listdir('downloads')
print(categories)
for category in os.listdir('downloads'):
    files = os.listdir(f'downloads/{category}')

    for humans in os.listdir(f'downloads/{category}'):
        try:
            os.mkdir(f'./downloads/{category}/invert')
        except Exception as ex:
            print(f'ERROR !! - {ex}')

        for index, file in enumerate(os.listdir(f'downloads/{category}/{humans}')):
            print(index)
            print(f'{category} - {humans} - {file}')

            try:
                image = face_recognition.load_image_file(f'./downloads/{category}/{humans}/{file}')
                face_locations = face_recognition.face_locations(image)
            except Exception as ex:
                print(f'ERROR !! - {ex}')

            for file_num, face_location in enumerate(face_locations):
                top, right, bottom, left = face_location
                print(top, right, bottom, left)

                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image).convert('L')

                try:
                    pil_image.save(f'./downloads/{category}/invert/{humans}_{index}_{file_num}.jpg', 'JPEG')
                except Exception as ex:
                    print(f'ERROR !! - {ex}')
