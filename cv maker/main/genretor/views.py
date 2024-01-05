from django.shortcuts import render
from.models import mani
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST.get("name", "")
        email=request.POST.get("email", "")
        phone=request.POST.get("phone", "")
        summary=request.POST.get("summary", "")
        degree=request.POST.get("degree", "")
        school=request.POST.get("school", "")
        university=request.POST.get("university", "")
        previous_work=request.POST.get("previous_work", "")
        skills=request.POST.get("skills", "")

        cvobj=mani(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        cvobj.save()
        
    return render(request, 'home.html')

def cv(request, id):
    user_profile=mani.objects.get(id=id)
    template = loader.get_template('cv.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response= HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename="resume.pdf"
    return response

def list(request):
    user_profile = mani.objects.all()
    return render(request,'list.html',{'user_profile':user_profile})

def update(request,id):
    user_profile=mani.objects.get(id=id)
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone",]
        summary=request.POST["summary"]
        degree=request.POST["degree"]
        school=request.POST["school"]
        university=request.POST["university"]
        previous_work=request.POST["previous_work"]
        skills=request.POST["skills"]
        
        user_profile.name=name
        user_profile.email=email
        user_profile.phone=phone
        user_profile.summary=summary
        user_profile.school=school
        user_profile.degree=degree
        user_profile.university=university
        user_profile.previous_work=previous_work
        user_profile.skills=skills
        user_profile.save() 
        

    return render(request,'update.html',{'user_profile':user_profile})
