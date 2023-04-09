import pyqrcode

from pyqrcode import QRCode

url = input("Enter the url to generate QR Code: ")
code = pyqrcode.create(url)


code.svg("qr_code.svg",scale = 6)