from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True)
    description = models.CharField(max_length=500, null=False)
    document = models.FileField(upload_to='Books/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, null=False)