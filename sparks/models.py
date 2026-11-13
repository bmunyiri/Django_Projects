from django.db import models

class Spark(models.Model):
    """A short quote or thought."""
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  # Show first 50 characters
