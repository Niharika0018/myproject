from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import User, UserProfileModel

class AccountsView(View):
    def createUser(request):
        phone_number = request.GET['phone_number']
        name = request.GET['name']
        date_of_birth = request.GET['date_of_birth']
        gender = request.GET['gender']
        image = request.GET['image']
        
        user_one, created = User.objects.update_or_create(phone_number=phone_number, is_customer=True)
        user, created = UserProfileModel.objects.update_or_create(name=name, date_of_birth=date_of_birth, gender=gender, image=image, owner_id=user_one.id, 
                                                               defaults=dict(name=name,
                                                                            date_of_birth=date_of_birth,
                                                                            gender=gender,
                                                                            image=image))


        return HttpResponse(user)