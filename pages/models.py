from django.db import models

# Create your models here.


class GetInTouch(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=120)
    phone_number = models.IntegerField(null=True , blank=True)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.full_name