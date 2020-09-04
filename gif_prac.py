# 복수의 이미지를 사이즈 변경하여 저장후 GIF 파일로 변형하는 코드

import glob
from PIL import Image, ImageDraw, ImageFont
import imageio



resized_images = []    # 리사지즈 파일을 저장할 빈 리스트를 만들고
folder_path = "source_image/*"     # 특정 폴더에 있는 모든 파일 목록
images = sorted(glob.glob(folder_path))

## 여기는 리사지즈 크기관련 조건들
w, h = 900, 600   # 이미지 리사이즈 가로, 세로 길이
font = ImageFont.truetype('HMFMMUEX.TTC', size=100)
color = 'rgb(255, 0, 0)'
new_image = Image.new('RGB', (w, h), (250, 250, 250))
##########################################3

for img in images:
    img = img.split('\\')[-1]   # 파일 경로에서 순수한 이미지 파일 이름만 뽑아내고
    image = Image.open('source_image/{0}'.format(img))    # 그 이미지 파일을 오픈하고
    image = image.resize((w, h))   # 리사이즈를 하고
    new_image.paste(image,(0,0))    # 리사이즈된 이미지를 new_image에 담고
    # print(img)
    new_image.save("resized_image/resized_{0}".format(img), "JPEG")


images = []
folder_path = "resized_image/*"     # 리사이즈 폴더에서 파일을 읽어오고
filenames = sorted(glob.glob(folder_path))

for filename in filenames:
    images.append(imageio.imread(filename))     # 순수 이미지 파일이름 뿐만 아니라, 경로 정보도 포함된 상태로 합친다.
imageio.mimsave('result_image/test4.gif', images, duration=1)

