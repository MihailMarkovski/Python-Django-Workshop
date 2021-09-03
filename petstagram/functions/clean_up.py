import os

#remove the current file on the current path
from django.core.exceptions import ValidationError

from functions.image_exist_for_delete_validator import img_validator


def clean_up_files(path):
    if img_validator(path) not in path:
        #need to apply the validator to the site page
        raise ValidationError('File does not exist pls go back and contact us!')

    os.remove(path)


