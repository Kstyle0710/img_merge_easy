from PIL import Image, ImageDraw, ImageFont
import glob
import math

img_list = []
name_list = []
dirpath = "C:/my_develop/image_merge_02/image/*.jpg"
files = sorted(glob.glob(dirpath))
for file in files:     # 해당 폴더에 사진이 저장된 순서에 따라 불러온다.
    extract = file.split('\\')[-1]
    img_list.append(extract)
    name_list.append(extract.split('.')[0])
print(name_list)
# print(len(img_list))
td_len = math.ceil(len(img_list)/2)
# print(td_len)

w, h = 426, 240   # 이미지 리사이즈 가로, 세로 길이
font = ImageFont.truetype('HMFMMUEX.TTC', size=100)
color = 'rgb(255, 0, 0)'
(x, y) = (15, 15)

new_image = Image.new('RGB', (2 * w, td_len * h), (250, 250, 250))

for idx, img in enumerate(img_list):
    # print(idx)
    image = Image.open('image/{0}'.format(img))
    draw = ImageDraw.Draw(image)
    message = "Photo_No.{0} : {1}".format(int(idx) + 1, name_list[int(idx)])
    draw.text((x, y), message, fill=color, font=font)

    image = image.resize((w, h))
    if int(idx) % 2 == 0:
        new_image.paste(image, (0, int(h * int(idx)/2)))
    else:
        new_image.paste(image, (w, int(h * math.floor(int(idx)/2))))

new_image.save("merged_images/merged4.jpg", "JPEG")
new_image.show()
