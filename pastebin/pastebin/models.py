from django.db import models

class Paste(models.Model):
    
    title = models.CharField(max_length=50) 
    code = models.TextField()
    
    LANGUAGE_CHOICES = (
        ("PYTHON", "Python"),
        ("JS","Javascript"),
        ("OUTROS", "Outros"),
    )

    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=40
    )
