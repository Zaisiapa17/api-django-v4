from rest_framework import status, settings
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import os
from PIL import Image
import secrets

from . import test_img_model
from . import test_img_serializer



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def crop_and_save_image(input_file, output_path, target_width, target_height):
    img = Image.open(input_file)
    print(img)
    
    # Calculate the aspect ratio of the target dimensions
    target_aspect_ratio = target_width / target_height
    
    # Calculate the aspect ratio of the original image
    original_aspect_ratio = img.width / img.height
    
    if original_aspect_ratio > target_aspect_ratio:
        # Crop the width
        new_width = int(target_height * original_aspect_ratio)
        img = img.resize((new_width, target_height), Image.LANCZOS)
        
        left_margin = (new_width - target_width) / 2
        right_margin = left_margin + target_width
        top_margin = 0
        bottom_margin = target_height
    else:
        # Crop the height
        new_height = int(target_width / original_aspect_ratio)
        img = img.resize((target_width, new_height), Image.LANCZOS)
        
        left_margin = 0
        right_margin = target_width
        top_margin = (new_height - target_height) / 2
        bottom_margin = top_margin + target_height
    
    # Crop the image
    cropped_img = img.crop((left_margin, top_margin, right_margin, bottom_margin))
    
    # delete original file
    os.remove(input_file)
    
    # Save the cropped image
    cropped_img.save(output_path)



def fileSave(request):
    image_file = request.data.get("image_name")

    # Check if the uploaded file has an allowed extension
    if not allowed_file(image_file.name):
        return Response({'error': 'Invalid file format'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate a random string of length 10 for the file name
    random_file_name = secrets.token_hex(5)  # 5 bytes will result in a 10-character hex string

    # Get the file extension from the original file name
    file_extension = os.path.splitext(image_file.name)[1]
    
    # Construct the new file name with the random string and original extension
    new_file_name = f'{random_file_name}{file_extension}'
    
    # Construct the save file path
    save_file_path = f'static/uploads/image/{new_file_name}'

    # Save the original file
    with open(save_file_path, 'wb') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)

    # Crop and save the image
    cropped_file_path = f'static/uploads/cropped/{new_file_name}'
    crop_and_save_image(save_file_path, cropped_file_path, target_width=500, target_height=200)

    # Save the new file name in the database
    test_img_model.Picture.objects.create(img_name=new_file_name)

    return Response({'message': 'Image uploaded and cropped successfully'}, status=status.HTTP_201_CREATED)