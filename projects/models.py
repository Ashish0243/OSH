from django.db import models
from organizations.models import Organisation
from users.models import Skill

# Create your models here.
class Project(models.Model):
    uid=models.CharField(max_length=100,unique=True,blank=False,null=False)
    organization=models.ForeignKey(Organisation, on_delete=models.CASCADE,related_name='projects')
    project_name=models.CharField(max_length=255,blank=False,null=False)
    code_url=models.URLField()
    proj_description=models.CharField(max_length=1000,blank=False,null=False)
    project_url=models.URLField()
    # craete a topic list as well tech_topic=models.ManyToManyField(Skill,related_name='projects')
    status=models.CharField(max_length=100,choices=[
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ], default='draft')
    mentors=models.ManyToManyField('Mentors',related_name='projects',blank=True)
    def __str__(self):
        return self.project_name
    
class ProjectRequirement(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    tech_tags=models.ManyToManyField(Skill,related_name='project_requirements')

class Mentors(models.Model):
    name=models.CharField(max_length=255,blank=False,null=False)
    linkedin=models.URLField(max_length=255,unique=True,blank=False,null=False)
   