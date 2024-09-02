import os
import uuid
from uuid import uuid1


class FileService:

    @staticmethod
    def upload_car_photo(instance, file: str) -> str:
        if '.' in file:
            extension = file.split('.')[-1]
        else:
            extension = ''

        filename = f'{uuid.uuid4()}.{extension}' if extension else f'{uuid.uuid4()}'
        return os.path.join('cars_photo', filename)
