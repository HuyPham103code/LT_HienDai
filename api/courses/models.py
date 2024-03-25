from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

class User(AbstractUser):
    avatar = CloudinaryField(null=True)

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    icon = models.CharField(max_length=20, default='tag')

    def __str__(self):
        return self.name

class Course(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = CloudinaryField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = CloudinaryField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.subject
    
class Interaction(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

        #   tất cả các lớp đều được kế thừa, riêng meta thì không =))

class Comment(Interaction):
    content = models.CharField(max_length=255)

class Like(Interaction):
    class Meta:
        unique_together = ('lesson', 'user')
    


