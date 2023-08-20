from django.db import models
from PIL import Image
# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=25)
    logo1 = models.CharField(max_length=20)
    logo2 = models.CharField(max_length=20)

    greetings_1 = models.CharField(max_length= 20)
    greetings_2 = models.CharField(max_length= 255)
    greetings_3 = models.CharField(max_length= 255)
    greetings_4 = models.CharField(max_length= 255)
    greetings_5 = models.CharField(max_length= 255)

    
    picture = models.ImageField(upload_to='picture/')
    picturephone = models.ImageField(upload_to='picture/')

    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.picture:
            self.compress_and_optimize_image(self.picture)

        if self.picturephone:
            self.compress_and_optimize_image(self.picturephone)

    def compress_and_optimize_image(self, image_field):
        img = Image.open(image_field.path)
        img.save(image_field.path, quality=20, optimize=True)

    def __str__(self):
        return self.logo1
    

class About(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank = False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_and_optimize_image()

    def compress_and_optimize_image(self):
        img = Image.open(self.profile_img.path)
        img.save(self.profile_img.path, quality=20, optimize=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete = models.CASCADE)
class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    skill_description = models.TextField(blank=False)

class ExperienceCategory(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Experience Category'
        verbose_name_plural = 'Experience Categories'

    def __str__(self):
        return self.name

class Experience(models.Model):
    experiencecategory = models.ForeignKey(ExperienceCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
class EducationCategory(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Education Category'
        verbose_name_plural = 'Education Categories'

    def __str__(self):
        return self.name
class Education(models.Model):
    educationcategory = models.ForeignKey(EducationCategory, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    graduation_date = models.DateField()

    def __str__(self):
        return self.degree
    
class Service(models.Model):
    logo = models.TextField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name
    

class WorkCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Work(models.Model):
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='works/')
    link = models.URLField()

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.compress_and_optimize_image()

    def compress_and_optimize_image(self):
        img = Image.open(self.image.path)
        img.save(self.image.path, quality=50, optimize=True)

class Socials(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    email = models.EmailField()
    Facebook = models.URLField()
    Instagram = models.URLField()
    LinkedIn = models.URLField()

    def __str__(self):
        return self.name