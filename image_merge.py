from PIL import Image

image1 = Image.open('image/1.jpg')
image2 = Image.open('image/2.jpg')
image3 = Image.open('image/3.jpg')
image4 = Image.open('image/4.jpg')


image1 = image1.resize((426, 240))
image1_size = image1.size
image2 = image2.resize((426, 240))
image2_size = image2.size
image3 = image3.resize((426, 240))
image3_size = image1.size
image4 = image4.resize((426, 240))
image4_size = image4.size

new_image = Image.new('RGB', (2*image1_size[0], 2*image1_size[1]), (250, 250, 250)) # 통합 이미지 그림판, 곱하기는 가로 세로 칸 개수
new_image.paste(image1,(0,0))
new_image.paste(image2, (image1_size[0], 0))
new_image.paste(image3,(0,image1_size[1]))
new_image.paste(image4, (image1_size[0], image1_size[1]))
new_image.save("merged_images/merged1.jpg", "JPEG")
new_image.show()
