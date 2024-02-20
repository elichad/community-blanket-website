from datetime import date

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from squares.models import Square
from contributors.models import Person, get_anonymous_user

# Create your tests here.


class TestSquare(TestCase):
    def test_create_square__known_creator(self):
        # Arrange
        person, _ = Person.objects.get_or_create(name="Jane Fakename")
        data = {
            "name": "Test Square",
            "image": SimpleUploadedFile("test.jpg", b"file data"),
            "creator": person,
            "date_created": date.today(),
            "description": "An empty square",
            "notes": "This square is a test.",
        }
        square = Square(**data)

        # Act & Assert
        square.full_clean()
        self.assertEqual(square.creator, person)

    def test_create_square__anonymous_creator(self):
        # Arrange
        data = {
            "name": "Test Square",
            "image": SimpleUploadedFile("test.jpg", b"file data"),
            "date_created": date.today(),
            "description": "An empty square",
            "notes": "This square is a test.",
        }

        # Act
        square = Square(**data)
        square.full_clean()

        # Assert
        self.assertEqual(square.creator, get_anonymous_user())
