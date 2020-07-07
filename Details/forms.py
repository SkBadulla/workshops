from Details.models import Workshop_Details,UploadImage
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Workshop_Details_Form(ModelForm):
	class Meta:
		model = Workshop_Details
		fields  = '__all__'
		#fields  = ['name_of_workshop','organized_by']

class UploadImageForm(ModelForm):
	class Meta:
		model = UploadImage
		fields = '__all__'

class UserRegistratonForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2']