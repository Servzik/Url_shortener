import string
import random
from django.db import models

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs):
        if not self.short_code:
            # Generate a unique short code
            characters = string.ascii_letters + string.digits
            while True:
                short_code = ''.join(random.choice(characters) for _ in range(6))
                if not URL.objects.filter(short_code=short_code).exists():
                    self.short_code = short_code
                    break
        super(URL, self).save(*args, **kwargs)
