from django.shortcuts import render,redirect
from Details.forms import Workshop_Details_Form, UploadImageForm,UserRegistratonForm
from django.http import HttpResponse
from Details.models import Workshop_Details,UploadImage

from django.contrib import messages
from django.core.mail import send_mail
from workshops import settings
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
	return render(request,'Details/home.html',{})

def workshopdetails(request):
	if request.method == 'POST':
		form  = Workshop_Details_Form(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponse('done')
			messages.success(request, 'New record added....')
			return redirect('display')


	form = Workshop_Details_Form()
	return render(request,'Details/workshopdetails.html',{'form':form})

def display(request):
	data = Workshop_Details.objects.all()
	return render(request,'Details/display.html',{'data':data})


def updateworkshopdetails(request,id):
	info = Workshop_Details.objects.get(id=id)
	if request.method=='POST':
		form = Workshop_Details_Form(request.POST,instance=info)
		if form.is_valid():
			form.save()
			#return HttpResponse('record updated........')
			messages.success(request,'record updated......')
			return redirect('display')
	form  = Workshop_Details_Form(instance = info)
	name='update'
	return render(request,'Details/workshopdetails.html',{'form':form,'name':name})


def delete(request,id):
	info = Workshop_Details.objects.get(id=id)
	if request.method=='POST':
		info.delete()
		messages.info(request,'record is deleted')
		return redirect('display')
	return render(request,'Details/confmsg.html',{'info':info})

def viewInfo(request,pk):
	data = Workshop_Details.objects.get(id=pk)
	return render(request,'Details/viewInfo.html',{'data':data})

def uploadImage(request):
	if request.method=='POST':
		form = UploadImageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse('Image Uploaded......')
	form = UploadImageForm()
	return render(request,'Details/uploadImage.html',{'form':form})

def showImages(request):
	data = UploadImage.objects.all()
	return render(request,'Details/showImages.html',{'data':data})


def sendMail(request):
	if request.method=='POST':
		sub = request.POST['subject']
		message = request.POST['msg']
		to = request.POST['receiver'].split(',')
		res = send_mail(sub, message, settings.EMAIL_HOST_USER, to)
		if res == 1:
			return HttpResponse('Mail Sent......')
		return HttpResponse('sorry,please try again......')

	return render(request,'Details/sendMail.html')

	# # subject = "hi"
	# # msg = "Congratulations for your success"
	# # receiver = "badullashaik507@gmail.com"
	# # rec1 = 'abdulla.sk@apssdc.in'
	# res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [receiver,rec1])
	# if(res == 1):
	# 	msg = "Mail Sent Successfuly"
	# else:
	# 	msg = "Mail could not sent"
	# return HttpResponse(msg) 


def register(request):
	if request.method=='POST':
		form = UserRegistratonForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Done...........')

	form  = UserRegistratonForm()
	return render(request,'Details/register.html',{'form':form}) 

