import qrcode

img = qrcode.make("www.programmerzamannow.com")

img.save("qr_pzn.png")