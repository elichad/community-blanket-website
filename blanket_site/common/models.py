from io import BytesIO
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image


class ThumbnailGenerator(models.Model):
    """Model which generates thumbnails from uploaded images on save."""

    image = models.ImageField(
        upload_to="uploads/%Y/%m/%d/",
        help_text="An image uploaded by the user.",
    )
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        help_text="A thumbnail generated automatically from the uploaded image.",
        null=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # generate thumbnail automatically
        # 1. create thumbnail of image
        imag = Image.open(self.image)
        output_size = (100, 100)
        imag.thumbnail(output_size)
        # 2. create file buffer
        buffer = BytesIO()
        imag.save(fp=buffer, format="PNG")
        pillow_image = ContentFile(buffer.getvalue())
        # 3. save to thumbnail field
        imag_name = f'{self.image.name.replace("/","_")}-thumbnail.png'
        self.thumbnail.save(
            imag_name,
            InMemoryUploadedFile(
                pillow_image,  # file
                None,  # field_name
                imag_name,  # file name
                "image/png",  # content_type
                pillow_image.tell,  # size
                None,  # content_type_extra
            ),
            save=False,
        )

        # now save the whole instance
        super().save(*args, **kwargs)
