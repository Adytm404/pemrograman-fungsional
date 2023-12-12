from PIL import Image, ImageDraw, ImageFont

gambarku = Image.open("img/image.png")

gambarBW = gambarku.convert("L")

draw = ImageDraw.Draw(gambarBW)

font_directory = "fonts/Poppins-Bold.ttf"
font_size = 24
font = ImageFont.truetype(font_directory, font_size)

text = f"Ogya Adyatma Putra\n202110370311228"
text_box = font.getbbox(text)

text_width = text_box[2] - text_box[0]
text_height = text_box[3] - text_box[1]

text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill="white")

gabung = Image.new("RGB", (gambarku.width, gambarku.height), "white")

gabung.paste(gambarBW, (0, 0))
gabung.save("percobaan.png")

gabung.show()
