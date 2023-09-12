from django.shortcuts import render
from .models import About,Contact,Biodata,Testimonial,Education,Experience,Skill,Com_Skill,Service,Clints,FunFact,WorKTime

# Create your views here.
def home(request):
    all_about = About.objects.all()
    all_contact = Contact.objects.all()
    all_pdf_resume = Biodata.objects.all()
    all_testi = Testimonial.objects.all()
    all_edu = Education.objects.all()
    all_ex = Experience.objects.all()
    all_skill = Skill.objects.all()
    all_com_skill = Com_Skill.objects.all()
    all_service= Service.objects.all()
    all_clints = Clints.objects.all()
    all_fun_fact = FunFact.objects.all()
    all_worktime = WorKTime.objects.all()
    return render(request,'index.html',{'all_about': all_about,'all_contact':all_contact,"all_pdf_resume":all_pdf_resume,'all_testi':all_testi,'all_edu':all_edu,'all_ex':all_ex,'all_skill':all_skill,'all_com_skill':all_com_skill,'all_service':all_service,'all_clints':all_clints,'all_fun_fact':all_fun_fact,'all_worktime':all_worktime})