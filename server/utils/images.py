import uuid
import os

from fastapi import HTTPException, UploadFile


def add_image(image: UploadFile):
    file_extension = image.filename.split('.')[-1]
    if file_extension not in ['jpg', 'png', 'jpeg']:
        raise HTTPException(status_code=400, detail="Unsupported extension")
    
    file_path = os.path.join('static/product', f'{uuid.uuid4()}.{file_extension}')
    with open(file_path, 'wb') as file:
        file.write(image.file.read())

    return file_path