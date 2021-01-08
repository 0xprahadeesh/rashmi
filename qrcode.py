import pyqrcode
import png

url='https://instagram.com/chill_tamizha'
p = pyqrcode.create(url)
p.png('C:/Users/Qr.png',scale=10)

def profile():
    from PIL import Image 
  
    im = Image.open(r"C:/Users/Qr.png")  
    im.show()

profile()
