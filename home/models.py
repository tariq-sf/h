from django.db import models

# Create your models here.



'''
django models field :
 -html widget
 -validation
 -db size
 '''
JOB_TYPE = (
    ('Full time','Full time'),
    ('part time','part time'),
)
class home(models.Model):  #table
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=15,choices=JOB_TYPE) #column
    Description = models.TextField(max_length=1000) #column
    salary=models.IntegerField(default=0)
    published_at =models.DateTimeField(auto_now=True)
    experience=models.IntegerField(default=2)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)


    def __str__(self):
        return self.title
class Category (models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name 

 