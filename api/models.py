from django.db import models

GENDERS = (
  ("f","Female"),
  ('m',"Male")
)

class Student(models.Model):
  name = models.CharField(max_length=200)
  roll_number = models.IntegerField(unique = True)
  email = models.EmailField(max_length=100)
  gender = models.CharField(max_length=1, choices=GENDERS)
  percentage = models.FloatField()
  
  institute = models.ForeignKey('Institute', on_delete=models.CASCADE, null=True, blank = True)
  
  def __str__(self):
    return self.name
  
class Institute(models.Model):
  
  TYPES = (
    ('c', 'college'), 
    ('h','highschool')
  )
  
  name = models.CharField(max_length=200)
  type_of_institute = models.CharField(max_length=1, choices= TYPES)
  
  def __str__(self):
    return self.name
