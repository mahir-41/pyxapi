from pyxelate import Pyx
from skimage import io
from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from PIL import Image
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    new_image = Pyx(palette=20, dither ="none", alpha=.6).fit_transform(image)

    io.imsave("raw.png", new_image)
    image = Image.open('raw.png')
    new_image = image.resize((200, 200), resample=Image.NEAREST)

    new_image.save("pixel.png", quality = 50)
    return "OK"

@app.get("/getImage")
async def getImage():
    return FileResponse("pixel.png")