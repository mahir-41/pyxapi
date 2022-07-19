from pyxelate import Pyx
from skimage import io
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import requests

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "Test successful"}

@app.get("/pixelate", response_class=FileResponse)
async def pixelate():
    image = Image.open('image_name.jpg')
    new_image = image.resize((100, 100))
    new_image.save('image_name.png')

    image = io.imread("image_name.png") 

    new_image = Pyx(palette=10, dither ="none", alpha=.6).fit_transform(image)

    io.imsave("pixel.png", new_image)

    return FileResponse("pixel.png")

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    with open('image_name.jpg', 'wb') as handler:
        handler.write(contents)
    return {"filename": file.filename}