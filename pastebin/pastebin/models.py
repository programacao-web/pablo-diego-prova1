from django.db import models

class Pastebin(models.Model):
    
    title = models.CharField(max_length=50) 
    code = models.TextField()
    
    LANGUAGE_CHOICES = (
        ("PYTHON", "Python"),
        ("JS","Javascript"),
        ("OTHERS", "Outros"),
    )

    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=40
    )
