"""versionone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formsubmit/', user_views.home, name='home'),
    path('', user_views.DetailView, name='detail'),
    path('Result/', user_views.AssignView, name='Result'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.loginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

