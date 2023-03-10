from django.db import models
from django.contrib.auth.models import User
state=(
    ('Assam','Assam'),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
    ('',''),
)
city=(
    ('M','M'),
    ('A','A'),
    ('E','E'),
    ('R','R'),
)
type_of_user=(
    ('Volunteer','Volunteer'),
    ('Request','Request'),

)
type_of_disaster=(
    ('Agricultural diseases & pests','Agricultural diseases & pests'),
    ('Damaging Winds','Damaging Winds'),
    ('Drought and water shortage','Drought and water shortage'),
    ('Earthquakes','Earthquakes'),
    ('Emergency diseases (pandemic influenza)','Emergency diseases (pandemic influenza)'),
    ('Extreme heat','Extreme heat'),
    ('Floods and flash floods','Floods and flash floods'),
    ('Hail','Hail'),


)
service_domain=(

    ('Financial Aid','Financial Aid'),
    ('Medical Aid','Medical Aid'),
    ('Rehabilitation(Shelter) Aid','Rehabilitation(Shelter) Aid'),
    ('Resources Aid(Food,and other amenities)','Resources Aid(Food,and other amenities)'),
    ('Man-Power','Man-Power')
)
class Profiles(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name= models.CharField(max_length=100,default="DEFAULT")
    Email=models.CharField(max_length=100)
    State=models.CharField(max_length=500,choices=state)
    Ciity=models.CharField(max_length=500,choices=city)
    Incentive_Expected=models.IntegerField()
    Experience=models.IntegerField()
    Phone=models.CharField(max_length=10)
    Skill_certificates=models.FileField(upload_to='Skill_certificates/')
    ID_Proof=models.FileField(upload_to='ID_Proof/')
    Timestamp=models.DateTimeField(auto_now_add=True)
    Type_of_User=models.CharField(max_length=500,choices=type_of_user)
    Type_of_disaster=models.CharField(max_length=500,choices=type_of_disaster)
    Rehabilitation_Recovery_estimated_time_in_days=models.IntegerField()
    Service_Domain=models.CharField(max_length=500,choices=service_domain)
    Pair_Found=models.BooleanField(default=False)
    Paired_with=models.CharField(max_length=500,default=None,blank=True,null = True)




# Create your models here.
