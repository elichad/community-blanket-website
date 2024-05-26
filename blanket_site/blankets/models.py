import numpy as np

from django.db import models
from django.urls import reverse

from squares.models import Square

# Create your models here.


class Blanket(models.Model):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    description = models.TextField()
    num_cols = models.IntegerField()
    num_rows = models.IntegerField()

    def get_absolute_url(self):
        return reverse("blankets:blanket-detail", kwargs={"pk": self.pk})

    def get_blanket_items(self):
        # loop over rows and columns and get all items where they exist
        items = np.empty((self.num_rows, self.num_cols), dtype=Square)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                try:
                    item = BlanketItem.objects.get(blanket=self, row=row, column=col)
                    square = item.square
                    items[row, col] = square
                except BlanketItem.DoesNotExist:
                    continue
        return items

    def __str__(self):
        return self.name


class BlanketItem(models.Model):
    """Model to connect Squares and Blankets."""

    blanket = models.ForeignKey(Blanket, on_delete=models.CASCADE)
    square = models.ForeignKey(Square, on_delete=models.PROTECT)
    column = models.PositiveIntegerField()
    row = models.PositiveIntegerField()

    class Meta:
        constraints = [
            # Square can only be in one location
            models.UniqueConstraint("square", name="unique_square"),
            # Each blanket cell can only contain one square
            models.UniqueConstraint(
                "blanket", "column", "row", name="unique_blanket_column_row"
            ),
        ]

    def clean_column(self):
        if self.column >= self.blanket.num_cols:
            raise ValueError("Column number exceeds number of columns in blanket")

    def clean_row(self):
        if self.row >= self.blanket.num_rows:
            raise ValueError("Row number exceeds number of rows in blanket")

    def clean_fields(self, exclude=None):
        super().clean_fields()

        self.clean_column()
        self.clean_row()

    def __str__(self):
        return f"{self.blanket.name} ({self.column}, {self.row})"
