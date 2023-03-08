# pyxapi
API to generate pixel art from image files

Endpoints
1) GET - "/test" - Returns json "message": "Test successful" if API is functioning normally.
2) GET - "/pixelate(?url=...)" - Saves a pixel art version of the image in the provided url(in the form of a url parameter).
3) GET - "/getImage" - Returns the file with the pixel art image.

To run API locally use - uvicorn main:app --reload 

NOTE: API can be tested locally, since Heroku's free services have been terminated.

Special thanks: https://github.com/sedthh/pyxelate 
