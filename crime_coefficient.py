from PIL import Image, ImageFont, ImageDraw
import random
import requests

maxWidth = 1024
maxHeight = 1024


def coefficient(url: str, name: str, user_id: int):
	random.seed(user_id)
	cc_int = random.randint(0, 320)
	cc_float = random.randint(0, 9)
	if cc_int < 100:
		layer = Image.open("layers/blue_layer.png")
		target_text = "Not Target"
	elif 100 <= cc_int < 299:
		target_text = "Execution"
		layer = Image.open("layers/yellow_layer.png")
	else:
		layer = Image.open("layers/red_layer.png")
		target_text = "Execution"

	pp = Image.open(requests.get(url, stream=True).raw)

	width, height = pp.size
	ratio = min(maxWidth / width, maxHeight / height)
	size = (int(pp.size[0]*ratio), int(pp.size[1]*ratio))
	pp = pp.resize(size)

	cc_text = str(cc_int) + "." + str(cc_float)
	cc_font = ImageFont.truetype("ArialCEBoldItalic.ttf", 80)
	target_font = ImageFont.truetype("ArialCEBoldItalic.ttf", 43)

	pp.paste(layer, (0, 0), layer)

	draw = ImageDraw.Draw(pp)
	draw.text((752, 254), cc_text, (255, 255, 255), font=cc_font)
	draw.text((752, 371), target_text, (255, 255, 255), font=target_font)
	pp.save(name + ".png")
