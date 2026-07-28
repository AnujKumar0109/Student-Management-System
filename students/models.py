from django.db import models
from django.conf import settings


class Student(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="students"
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    date_of_birth = models.DateField()

     # Student Photo
    image = models.ImageField(
        upload_to="student_photos/",
        blank=True,
        null=True
    )



    def __str__(self):
        return f"{self.first_name} {self.last_name}"