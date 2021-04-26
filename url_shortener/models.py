from django.db import models
from django.contrib.auth.models import User
from extensions.utils import datetime_to_jalali_str
from django.urls import reverse

# Create your models here.

class URL(models.Model):
    address = models.URLField(max_length=512, verbose_name="آدرس لینک", name="جواد زاهدی")
    visits = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدیدها")
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    def jcreated(self):
        return datetime_to_jalali_str(self.created)

class Code(models.Model):
    slug = models.SlugField(max_length=6, verbose_name="کلید")
    target = models.OneToOneField(URL, on_delete=models.CASCADE, related_name='code', verbose_name='مقصد')

    def __str__(self):
        return reverse('url_shortener') + self.code
