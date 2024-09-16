from django.db import models 
from django.contrib.auth.models import User
from django.utils.text import slugify
class Company(models.Model):
    name=models.TextField()
    ac=models.TextField()
    web=models.CharField(max_length=78) 
    contact=models.TextField(max_length=200,blank=True)
    em=models.EmailField(max_length=50,blank=True)
    def __str__(self):
        return self.name
class Jobpost(models.Model):
    choices=(('I','internship'),('F','freelancing'))
    level_choices=(('i','internship'),('j','junior'),('s','senior'))
    remote_choices=(('f','full time'),('c','contract'),('p','part time'))
    job=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True)
    salary=models.IntegerField()
    slug=models.SlugField(max_length=150,blank=True)
    iorf=models.CharField(max_length=1,choices=choices)
    job_description=models.TextField()
    req=models.TextField()
    img=models.ImageField(null=True,blank=True,upload_to="images/")
    level=models.CharField(max_length=1,choices=level_choices)
    remote=models.CharField(max_length=1,choices=remote_choices)
    url=models.TextField()
    Company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    def save(self, *args, **kwargs):
        super(Jobpost, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.job) + "-" + str(self.id)
            self.save()
    def __str__(self):
        return self.job
