
from PIL import Image
from PIL import ImageFilter 
try:
    img = Image.open("./img/jururu.jpg", mode='r')
    im01 = Image.open("./img/ocean.jpg", mode='r')
    #img1 = img.filter(ImageFilter.BLUR)// 흐리게 처리, 블러
    #img1 = img.filter(ImageFilter.EMBOSS) // 엠보싱 효과
    img1 = img.filter(ImageFilter.CONTOUR) #윤관만 표시
    img2= img.filter(ImageFilter.BoxBlur(5))
    img3 = img.filter(ImageFilter.MedianFilter(size=3))
    
    img1.show()
    img2.show()
    img3.show()
    
    #이미지 블렌드
    img_resized1 = img.resize((900,900))
    img_resized2 = im01.resize((900,900))
    im_bl=Image.blend(img_resized1, img_resized2, 0.5)
    im_bl.show()
    
    # 이미지 RGB 보기
    r,g,b = img.split() # 색상 출출
    
    r.show()
    b.show()
    g.show()
    rgb_img = Image.merge("RGB",(r,g,b))
    rgb_img.show()
    
    rgb_img = Image.merge("RGB",(b,r,g))
    rgb_img.show()
    
    
    
    img.rotate(45).show()
    img.rotate(90).show()
    
except IOError as err:
    print("unable to load image")


