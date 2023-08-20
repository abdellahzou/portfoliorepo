from django.shortcuts import render
from .models import Home, About, Category, Profile,ExperienceCategory, EducationCategory, Service, WorkCategory, Work, Socials

def index(request):
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    experiences = ExperienceCategory.objects.all()
    education = EducationCategory.objects.all()
    services = Service.objects.all()
    work_categories = WorkCategory.objects.all()
    works = Work.objects.all()
    socials=Socials.objects.all()
    context = {
        'home' : home,
        'about' : about,
        'profiles' : profiles,
        'categories' : categories,
        'experiences':experiences,
        'education' : education,
        'services' : services,
        'work_categories': work_categories,
        'works': works,
        'socials' : socials,
                }


    return render(request, 'index.html', context)