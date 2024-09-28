from django.db import models

# Create your models here.

class Post(models.Model):
    tittle = models.CharField(max_length = 200)
    body = models.TextField()
    author = models.ForeignKey(
        "auth.user",
        on_delete = models.CASCADE
    )

    def __str__(self) -> str:
        return self.tittle