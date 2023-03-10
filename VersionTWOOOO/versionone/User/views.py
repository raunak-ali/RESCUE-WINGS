from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from User.forms import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pandas as pd
from  User.Recommendation_system import*
#from Recommendation_system import FORMING_DATAFRAME
from User.Hungarian import*

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
    print(P.Email)
    return render(request, 'users/detail.html',context={'P':P,'User':User})
def AssignView(request):
    Query=Profiles.objects.filter(Pair_Found=False).values()
    df = pd.DataFrame(list(Query))
    #df.to_csv('Users.csv')
    df.sort_values(by='Timestamp', inplace = True)
    df['Timestamp'] = df['Timestamp'].apply(lambda a: pd.to_datetime(a).date()) 
    df.to_excel('Users.xlsx')
    df = pd.DataFrame(pd.read_excel("Users.xlsx"))
    print(df.head())
    print(df.info())
    original = pd.DataFrame(pd.read_excel("Users.xlsx"))
    original.head()
    similarities=SIMILARITY_VECTOR(df)#Makig Our Similarity Matrix
    #print(similarities)
    df=FORMING_DATAFRAME(similarities,df,original)# Our final dataframe which will be used for assignment
    print(df)
    Assigned={}# The dictionary which will store all assignments
    Transform(df,Assigned)#Sending it to tthe  Hungarian Algorithms
    #Making a sperate list from our dicttionary
    Requests=Assigned.keys()
    Volunteers=Assigned.values()
    print(Volunteers)
    #print(Requests)
    df_final = pd.DataFrame(pd.read_excel("Users.xlsx"))
    Request=[]
    Volunteer=[]
    #Getting names per index of our keys
    for v in Volunteers:
        Volunteer.append(v)
    for r in Requests:
        Request.append(df_final.iloc[r]['Name'])
    print(Request)
    print(df)
    UPDATE_DB_VIEW(Request,Volunteer)
    return redirect("home")

def  UPDATE_DB_VIEW(Request,Volunteer):
    for r in range(0,4):
        REQ=Request[r]
        VOL=Volunteer[r]
        RR=Profiles.objects.get(Name=REQ)
        VOL=Profiles.objects.get(Name=VOL)
        RR.Pair_Found=True
        VOL.Pair_Found=True
        RR.Paired_with=VOL.Name
        VOL.Paired_with=RR.Name
        RR.save()
        VOL.save()
        
        print(RR)
        print(VOL)



