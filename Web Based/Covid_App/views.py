from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
from datetime import date, timedelta

from django.core import mail
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Patient
from .machine_learning_model import evaluate


#     DB_row = Patient.objects.count() + 1

def PatientID():
    list = Patient.objects.all()
    idList = []

    for l in list:
        idList.append(int(l.PatientID[1:]))

    if len(idList) >0:    
        newID = max(idList) + 1
    else: 
        newID = 1

    if(newID <=9):
        PID = "P000" + str(newID)

    elif(newID>=10 & newID<=99):
        PID = "P00" + str(newID)

    elif(newID >=100 & newID<=999):
        PID = "P0" + str(newID)   

    else:
        PID = "P" + str(newID)

    return PID

def dashboard(request):
    list = Patient.objects.all()
    babies, children, youngAdult, middleAgedAdult, oldAdult = 0,0,0,0,0

    for l in list:
        if (l.PatientAge >= 0 and l.PatientAge <= 2):
            babies +=1

        elif(l.PatientAge >= 3 and l.PatientAge <=16):
            children +=1

        elif(l.PatientAge >=17 and l.PatientAge <=30):
            youngAdult +=1

        elif(l.PatientAge >=31 and l.PatientAge <=45):
            middleAgedAdult +=1
        else:
            oldAdult +=1

    R_status_num = Patient.objects.filter(PatientStatus="RECOVERED").count()
    A_status_num = Patient.objects.filter(PatientStatus="ACTIVE").count()
    S_status_num = Patient.objects.filter(PatientStatus="SAFE").count()
    D_status_num = Patient.objects.filter(PatientStatus="DECEASED").count()

    male_num = Patient.objects.filter(PatientGender="M").count()
    female_num = Patient.objects.filter(PatientGender="F").count()

    covid_num = Patient.objects.filter(PatientPredictedLabel = "COVID").count()
    pneumonia_num = Patient.objects.filter(PatientPredictedLabel = "PNEUMONIA").count()
    normal_num = Patient.objects.filter(PatientPredictedLabel = "NORMAL").count()

    gender_number = [int(male_num), int(female_num)]
    label_number = [int(covid_num), int(pneumonia_num), int(normal_num)]
    age_group = [babies, children, youngAdult, middleAgedAdult, oldAdult]
    status_number = [S_status_num, A_status_num, R_status_num, D_status_num]
    

    context = {'gender_number': gender_number,
               'label_number' : label_number,
               'age_group'    : age_group,
               'status_number': status_number}
               

    return render(request, "Pneumonia_App/dashboard.html", context)

def insertDetails(request):
    context = {'PID' : PatientID(),
               'insert_path': request.get_full_path()}

    return render(request, "Pneumonia_App/insert.html", context)

# Create your views here.
# def insertDetails3(request):
#     context = {'PID': PatientID()}

#     return render(request, "Pneumonia_App/insert.html", context)

def eval(request):
    print(request)
    print(request)
    
    global fileObj
    global result
    fileObj = request.FILES['filePath']
    result,label = evaluate(fileObj)

    context = {'result' : result,
               'label'  : label,
               'PID'    : PatientID()}

    
    return render(request, "Pneumonia_App/insert.html", context)

def submit_form(request):
    if request.method == "POST":
        p = Patient()
        p.PatientID = request.POST.get('insertPID')
        p.PatientName = request.POST['insertName']
        p.PatientAge = request.POST['insertAge']
        p.PatientGender = request.POST['insertGender']
        p.PatientPhone = request.POST['insertPhone']
        p.PatientPredictedLabel = request.POST.get('label')
        p.Patient_X_Ray_Heatmap = str(fileObj)
        p.PatientRemark = request.POST['remark']
        p.PatientStatus = request.POST.get('status')

        p.save()

        messages.success(request, f'Patient ID: {p.PatientID} Had Been Uplodaded')


    context = {'PID' : PatientID()}

    return render(request, "Pneumonia_App/insert.html", context)


def viewDB(request):
    list = Patient.objects.all()
    context = {'list': list}
    return render(request, 'Pneumonia_App/viewDB.html', context)

def viewInfo(request, id):
    patient = Patient.objects.get(id = id)
    context = {'patient':patient}
    
    return render(request, 'Pneumonia_App/viewInfo.html', context)

def updateDB(request, id): 
    patient = Patient.objects.get(id = id)
    context = {'patient':patient,
               'current_path3': request.get_full_path()}

    if request.method == "POST":
        patient.PatientPhone = request.POST['phone']
        patient.PatientRemark = request.POST['remark']
        patient.PatientStatus = request.POST['status']


        patient.save()

        messages.success(request, 'Information Had Been Updated')

    return render(request, 'Pneumonia_App/update.html', context)

def delete(request, id): 
    patient = Patient.objects.get(id = id)
    pid = patient.PatientID

    patient.delete()

    messages.success(request, f'Patient ID: {pid} Had Been Successfully Deleted')
    return redirect('viewDB')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password= password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, 'Username OR Password is incorrect')

    context = {'current_path2': request.get_full_path()}
    return render(request, 'Pneumonia_App/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('homePage')

def homePage(request):
    data = True
    result = None
    globalSummary = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True

    today = date.today()
    yesterday = today - timedelta(days=1)

    context  = {'globalSummary' : globalSummary,
                'countries' : countries,
                'yesterday' : yesterday,
                'current_path': request.get_full_path()}

    if request.method == "POST":

        name = request.POST.get('name')
        pNumber = request.POST.get('Pnumber')
        email = request.POST.get('email')

        subject = "New Appointment had Been Requested!"
        message = "Name: " + name + "\nPhone Number: " + pNumber + "\nEmail: " + email
        recipient = "hadrianchong74@gmail.com"

        context = {"name" : name,
                   "pNumber" : pNumber,
                   "email" : email}

        html_message = render_to_string("Pneumonia_App/email.html", context)
        plain_message = strip_tags(html_message)

        from_email = settings.EMAIL_HOST_USER
        to = "hadrianchong74@gmail.com"

        mail.send_mail(subject, plain_message, from_email, [to], html_message = html_message)

        messages.success(request, f'Hey {name}, Your Booking Appointment Had Been Successfully Sent! The Admin Will Contact You Soon!')

        # send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)

        # send_mail('The contact form subject', "This is the messages", "hadrianchong74@gmail.com",["hadrianchong74@gmail.com"])
        return redirect("homePage")

    return render(request, "Pneumonia_App/home.html", context)