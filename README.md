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
