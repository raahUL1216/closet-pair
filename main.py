import os
from typing import List

import json

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

from color.color_utils import is_color_nuetral, is_color_cool, is_color_warm, is_color_complementary

IMAGEDIR = 'static/closet/'
DATADIR = 'static/data/'

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class Outfit(BaseModel):
	top: str
	bottom: str
	style: str
    
class Outfits(BaseModel):
    items: List[Outfit]


@app.get("/")
async def test():
	return {"Hello": "World"}


# @app.post("/cloth/")
# async def add_user_cloth(file: UploadFile = File(...)):

#     file.filename = f"{uuid.uuid4()}.jpg"
#     contents = await file.read()  # <-- Important!

#     # example of how you can save the file
#     with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
#         f.write(contents)

#     return {"filename": file.filename}

@app.get("/cloths/")
async def get_user_cloths():
	cloths = []

	with os.scandir(IMAGEDIR) as images:
		for image in images:
			if image.is_file():
				cloths.append(IMAGEDIR + image.name)

	return {"cloths": cloths}


@app.get("/suggested-outfits", response_model=Outfit, response_model_exclude_unset=True)
def get_suggested_outfits():
	f = open(DATADIR + 'closet.json')
	outfits = []

	try:
		closet = json.load(f)
		
		tops = closet['top']
		bottoms = closet['bottom']

		for bottom in bottoms:
			style = ''
   
			for top in tops:
				# 1) Nuetral + Anything
				if is_color_nuetral(bottom['main_color']):
					if is_color_cool(top['main_color']):
						style = 'Nuetral + Cool'
					elif is_color_warm(top['main_color']):
						style = 'Nuetral + Warm'
					elif is_color_complementary(top['main_color']):
						style = 'Nuetral + Complementry'
         
					outfits.append({
						"top": top["image"],
						"bottom": bottom['image'],
						"style": style
					})
				
				# elif is_color_cool()
    
		print(outfits)
		return Outfits(items=outfits)
	except:
		raise Exception("Error while browsing closet.")
	finally:
		f.close()
