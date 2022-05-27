"""relationalDataBaseManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from authen import views as app_views
from authen.forms import MyAuthForm

urlpatterns = [
    path('', app_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html', authentication_form=MyAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', app_views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('index/', views.index, name="index"),
    path('sent', views.sent),
    path('crudpage/',views.crud, name="crudpage"),
    path('create/',views.create,name = "create"),
    path('create/create_submit/',views.create_submit,name = "create_submit"),
    path('read/',views.read,name = "read"),
    path('read/read_submit/',views.read_submit,name = "read_submit"),
    path('update/',views.update,name = "update"),
    path('update/update_submit/',views.update_submit,name = "update_submit"),
    path('delete/',views.delete,name = "delete"),
    path('delete/delete_submit/',views.delete_submit,name = "delete_submit"),
    path('placement_status/', views.placement_status, name="placement_status"),
    path('add_company/', views.add_company, name="add_company"),
    path('add_company/add_company_submit/', views.add_company_submit, name="add_company_submit"),
    path('shortlist/', views.shortlist, name="shortlist"),
    path('shortlist/shortlist_submit/', views.shortlist_submit, name="shortlist_submit"),
    path('round_time/', views.round_time, name="round_time"),
    path('round_time/round_time_submit/', views.round_time_submit, name="round_time_submit"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('editprofile/update_profile/', views.update_profile, name="update_profile"),
    path('companies/', views.companies, name="companies"),
    path('resume/', views.resume, name="resume"),
    path('resume/resume_view/', views.resume_view, name="resume_view"),
    path('resume_view_pdf/', views.resume_view_pdf, name="resume_view_pdf"),
    path('calendar/', views.calendar, name="calendar"),
    path('view_reports/', views.view_reports, name="view_reports"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
