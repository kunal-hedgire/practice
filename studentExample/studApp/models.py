from django.db import models
'''
GENDER_CHOICES = (
    ('Male',  'Male'),
    ('Female','Female'),
    ('Other', 'Other')
ShreeNiketan@1997
)
'''
class studInfo(models.Model):
    FirstName=models.CharField(max_length=25)
    LastName=models.CharField(max_length=25)
    Age=models.IntegerField()
    mobile_number=models.BigIntegerField()
    #Gender=models.CharField(max_length=10)


    class Meta:
        db_table='studinfo'
