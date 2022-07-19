from pyxelate import Pyx
from skimage import io
from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image
import requests

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "Test successful"}

@app.get("/pixelate")
async def pixelate(url):
    img_data = requests.get(url).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)

    image = Image.open('image_name.jpg')
    new_image = image.resize((50, 50))
    new_image.save('image_name.png')

    image = io.imread("image_name.png") 

    new_image = Pyx(palette=10, dither="bayer", alpha=.6).fit_transform(image)

    io.imsave("pixel.png", new_image)

    filename = 'pixel.png'
    return FileResponse(filename)
