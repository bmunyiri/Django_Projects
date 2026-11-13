from django.db import models

# Create your models here.
class Goal(models.Model):
    """A personal goal to achieve."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.description[:50] + "..." if len(self.description) > 50 else self.description
    
    
    
