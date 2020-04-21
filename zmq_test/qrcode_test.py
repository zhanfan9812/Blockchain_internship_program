import base64
import io
import qrcode

text = 'https://www.baidu.com'
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.make(fit=True)
qr.add_data(text)
img = qr.make_image()

buf = io.BytesIO()
img.save(buf,format='PNG')
image_stream = buf.getvalue()
heximage = base64.b64encode(image_stream)
print('data:image/png;base64,' + heximage.decode())