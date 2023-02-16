from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('loginPage/', views.loginPage, name= "loginPage"),
    path('logout/', views.logoutUser, name= "logout"),
    path('viewDB/', views.viewDB, name= "viewDB"),
    re_path('eval', views.eval, name="eval"),
    re_path('submit_form', views.submit_form, name="submit_form"),
    path('insertDetails/', views.insertDetails, name="insertDetails"),
    path('dashboard/', views.dashboard, name="dashboard"),    
    path('viewInfo/<int:id>', views.viewInfo, name="viewInfo"),
    path('updateDB/<int:id>', views.updateDB, name="updateDB"),
    path('delete/<int:id>', views.delete, name="delete"),

]

urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
