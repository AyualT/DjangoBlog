from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/',default='')
    title = models.CharField(blank=False, max_length=200)
    text = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(default=timezone.now)
    time_published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.time_published = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title