from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from User.forms import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def home(request):
    if request.method == "POST":
        Profile_form = ProfileForm(request.POST, request.FILES)
        Profile_form.User=request.user
        

        
        if Profile_form.is_valid():
            PF=Profile_form.save(commit=False)
            PF.User=request.user
            PF.User.User_id=request.user.id
            PF.save()
            messages.success(request, ('Your Profile was successfully updated!'))
            return redirect("detail")
        else:
            messages.error(request, 'Error saving form')
        return redirect("home")
    Profile_form = ProfileForm()
    Profile = Profiles.objects.all()
    return render(request=request, template_name="users/home.html", context={'Profile_form':Profile_form, 'Profiles':Profile})
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
# Create your views here.
def DetailView(request):
    User=request.user
    P=Profiles.objects.get(User=User)
    #print(P.Email)
    Query=Profiles.objects.filter(Pair_Found=False).values()
    df = pd.DataFrame(list(Query))
    print(P.Email)

    return render(request, 'users/detail.html',context={'P':P,'User':User})



