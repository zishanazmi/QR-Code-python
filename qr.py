import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version= 1,
    box_size= 10,
    border= 4
)

data = "https://youtube.com/@imranyazmi?si=HhhmAuXckXsvV94h"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill= "black", back_color= "white")

img.save("qrcode.png")
img.show()




