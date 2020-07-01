from django.urls import path
from . import views

urlpatterns = [
    # path('gen_otp',views.gen_otp, name="index"),
    # path('verif_email',views.verif_email, name="verif_otp"),
    # path("send_mail",views.send_email,name="send_mail"),
    path("",views.index,name="index"),
    path("byifsc",views.byifsc,name="byifsc"),
    path("bydetails",views.bydetalis,name="bydetails"),
    path("detail_api",views.detail_api,name="details_api"),
    path("upload",views.upload,name="upload"),
]