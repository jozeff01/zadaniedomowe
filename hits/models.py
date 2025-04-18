from django.db import models
import uuid

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Hit(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title_url = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.title_url:
            self.title_url = uuid.uuid4().hex[:10]  # Генерация случайного title_url
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
