

from django.db import models

# Create your models here.

class URL(models.Model):
    address = models.URLField(max_length=512, verbose_name="آدرس لینک", name="جواد زاهدی")
    code = models.SlugField(max_length=6, verbose_name="لینک کوتاه")
    visits = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدیدها")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code