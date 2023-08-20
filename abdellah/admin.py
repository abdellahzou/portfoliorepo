from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, ExperienceCategory, Experience, EducationCategory, Education, Service, WorkCategory, Work, Socials

# Register your models here.
admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)

class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]
class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

@admin.register(ExperienceCategory)
class ExperienceCategoryAdmin(admin.ModelAdmin):
    inlines = [
        ExperienceInline,
    ]

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

@admin.register(EducationCategory)
class EducationCategoryAdmin(admin.ModelAdmin):
    inlines = [
        EducationInline,
    ]

admin.site.register(Service)
admin.site.register(WorkCategory)
admin.site.register(Work)
admin.site.register(Socials)
