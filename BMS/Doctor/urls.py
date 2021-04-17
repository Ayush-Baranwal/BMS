from django.conf.urls import url
from Doctor import views
from django.urls import path

app_name='Doctor'

urlpatterns=[
    path('Login/',views.doclogin,name='doclogin'),
    path('Register/',views.docregister,name='docregister'),
    path('Panel/',views.docpanel,name='docpanel'),
    path('Panel/Request',views.docpanelrequest,name='docpanelrequest'),
    path('Panel/Donor',views.docpaneldonor,name='docpaneldonor'),
]