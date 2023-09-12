from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 200)
    basic_talent=models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 300)
    about_me = models.TextField()
    company_url=models.CharField(max_length = 2000)
    resume_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    

class Contact(models.Model):
    get_in_touch = models.TextField()
    address = models.CharField(max_length = 1000)
    email = models.EmailField(max_length = 254)
    phone_number = models.CharField(max_length = 50)
    

    def __str__(self):
        return str(self.id)

class Biodata(models.Model):
    pdf = models.FileField(upload_to='resume/')
    
    def __str__(self):
        return str(self.id)
    
class Testimonial(models.Model):
    tesi_name = models.CharField(max_length = 100)
    testi_des = models.TextField()
    testi_image = models.ImageField(upload_to='productimg')
    
    def __str__(self):
        return str(self.id)

class Education(models.Model):
    edu_date = models.CharField(max_length = 100)
    title = models.CharField(max_length = 600)
    versity = models.CharField(max_length = 300)
    description = models.TextField()
    
    
    def __str__(self):
        return str(self.id)


class Experience(models.Model):
    ex_date = models.CharField(max_length = 100)
    title = models.CharField(max_length = 600)
    company = models.CharField(max_length = 300)
    description = models.TextField()
    
    
    def __str__(self):
        return str(self.id)

class Skill(models.Model):
    subject = models.CharField(max_length = 100)
    title = models.CharField(max_length = 300)
    parcent = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.id)

class Com_Skill(models.Model):
    subject = models.CharField(max_length = 100)
    title = models.CharField(max_length = 300)
    parcent = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.id)

class Service(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    sv_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Clints(models.Model):
    company_url = models.CharField(max_length = 900)
    clint_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class FunFact(models.Model):
    title = models.CharField(max_length = 100)
    ff_number = models.TextField()
    ff_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class WorKTime(models.Model):
    total_year = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.id)
                
    
            

