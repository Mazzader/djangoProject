from django.db import models


class Equipment_type(models.Model):
    mask = models.CharField(unique=True, max_length=10)
    name_of_type = models.TextField()

    def __str__(self):
        return self.name_of_type

    class Meta:
        verbose_name = "Типы оборудывания"
        verbose_name_plural = "Типы оборудывания"

class Equipment(models.Model):
    code_of_type = models.ForeignKey(Equipment_type,on_delete=models.CASCADE,related_name='equpment')
    serial_number = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name = "Оборудывание"
        verbose_name_plural = "Оборудывание"