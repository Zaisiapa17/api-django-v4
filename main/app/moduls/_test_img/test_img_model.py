from django.db import models

class Picture(models.Model):
    class Meta:
        db_table = '_picture'
    img_name = models.CharField(max_length=100)

    def __str__(self):
        return self.img_name