# pyxapi
API to generate pixel art from image files

Endpoints
1) GET - "/test" - Returns json "message": "Test successful" if API is functioning normally.
2) GET - "/pixelate(?url=...)" - Saves a pixel art version of the image in the provided url(in the form of a url parameter).
3) GET - "/getImage" - Returns the file with the pixel art image.

NOTE: API can be tested locally.

Two ways to run API locally: 
1) step 1: install python dependencies  - step 2: run "uvicorn main:app --reload" command to start fast api server
2) step 1: docker pull mahir41/pyxapi - step 2: docker run -d -p 80:80 mahir41/pyxapi

Special thanks: https://github.com/sedthh/pyxelate 

Demo:
<br>
<img width="547" alt="190949159-270d54d2-9f31-4bf5-977a-6978dca1ea1a" src="https://github.com/mahir-41/pyxapi/assets/28959987/71530f91-b091-4c04-a9b4-b024d2390053">

