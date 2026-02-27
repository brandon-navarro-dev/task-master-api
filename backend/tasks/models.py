from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_image(file):
    max_size = 2 * 1024 * 1024  # 2MB

    if file.size > max_size:
        raise ValidationError("La imagen no puede superar 2MB.")

    valid_extensions = ['image/jpeg', 'image/png', 'image/webp']
    if file.content_type not in valid_extensions:
        raise ValidationError("Formato no permitido. Solo JPG, PNG o WEBP.")


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    image = models.ImageField(upload_to='tasks/', validators=[validate_image], null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title