from django.contrib import admin
from .models import(
    About,
    Contact,
    Biodata,
    Testimonial,
    Education,
    Experience,
    Skill,
    Com_Skill,
    Service,
    Clints,
    FunFact,
    WorKTime
)

# Register your models here.

@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','designation','basic_talent','company_name','about_me','company_url','resume_image']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','get_in_touch','address','email','phone_number']

@admin.register(Biodata)
class BiodataModelAdmin(admin.ModelAdmin):
    list_display = ['id','pdf']

@admin.register(Testimonial)
class TestiModelAdmin(admin.ModelAdmin):
    list_display = ['id','tesi_name','testi_des','testi_image']

@admin.register(Education)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ['id','edu_date','title','versity','description']

@admin.register(Experience)
class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = ['id','ex_date','title','company','description']    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','subject','title','parcent']

@admin.register(Com_Skill)
class Com_SkillModelAdmin(admin.ModelAdmin):
    list_display = ['id','subject','title','parcent']


@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','sv_image']

@admin.register(Clints)
class ClintsModelAdmin(admin.ModelAdmin):
    list_display = ['id','company_url','clint_image',]

@admin.register(FunFact)
class FunFactModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','ff_number','ff_image']

@admin.register(WorKTime)
class WorKTimeModelAdmin(admin.ModelAdmin):
    list_display = ['id','total_year']    
