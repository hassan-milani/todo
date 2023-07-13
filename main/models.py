from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(verbose_name="الوصف")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "المهام"
    

