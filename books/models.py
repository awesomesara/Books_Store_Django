from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Publishers(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, related_name='author',on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publishers, related_name='publisher', on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
