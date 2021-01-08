import pyqrcode
import png

url='https://instagram.com/chill_tamizha'
p = pyqrcode.create(url)
p.png('C:/Users/91860/Documents/Qr.png',scale=10)

def profile():
    from PIL import Image 
  
    im = Image.open(r"C:/Users/91860/Documents/Qr.png")  
    im.show()

profile()