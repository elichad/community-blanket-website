from datetime import date

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from squares.models import Square
from contributors.models import Person, get_anonymous_user

# Create your tests here.


class TestSquare(TestCase):
    def test_create_square(self):
        # Arrange
        data = {
            "name": "Test Square",
            "image": SimpleUploadedFile("test.jpg", b"file data"),
            "creator": "Jane Fakename",
            "date_created": date.today(),
            "description": "An empty square",
            "notes": "This square is a test.",
        }
        square = Square(**data)

        # Act & Assert
        square.full_clean()
