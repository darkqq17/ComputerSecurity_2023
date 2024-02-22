from PIL import Image

file_path = "./flag.mem"
with open(file_path, "rb") as file:
    data = file.read()
width, height = 600, 600
img = Image.frombytes("RGBA", (width, height), data)
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.save("./flag.png", 'png')
