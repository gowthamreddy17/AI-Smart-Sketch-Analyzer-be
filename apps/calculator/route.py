# from fastapi import APIRouter
# import base64
# from io import BytesIO
# from apps.calculator.utils import analyze_image
# from schema import ImageData
# from PIL import Image

# router = APIRouter()

# @router.post('') 
# async def run(data: ImageData):
#     image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
#     image_bytes = BytesIO(image_data)
#     image = Image.open(image_bytes)
#     responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
#     data = []
#     for response in responses:
#         data.append(response)
#     print('response in route: ', response)
#     return {"message": "Image processed", "data": data, "status": "success"}
from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('') 
async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    
    # Call the analyze_image function and get responses
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    
    # Prepare a list to store responses
    data = []
    for response in responses:
        data.append(response)
        print('response in route: ', response)  # Print each response

    return {"message": "Image processed", "data": data, "status": "success"}
