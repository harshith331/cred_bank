from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import *
from decouple import config
from django.core import serializers
import csv,json

# Create your views here.
def index(request):
    return render(request,"index.html",{'data':{} ,"error":False})

def upload(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        upload_code="upload123"
        if body["code"] == upload_code : 
            with open(r'C:\Users\svsha\OneDrive\Desktop\proj2\bank_det\main\bank_branches.csv','r', encoding="utf8") as csv_file:
                csv_reader=csv.reader(csv_file)
                for i in csv_reader:
                    bank_now=bank.objects.filter(ifsc=i[0])[0]
                    if not bank_now :
                        print(i)
                        bank.objects.create(
                        ifsc=i[0],
                        bank_id=i[1],
                        branch=i[2],
                        address=i[3],
                        city=i[4],
                        district=i[5],
                        state=i[6],
                        bank_name=i[7],
                        )
                return JsonResponse({"success":True})
        else:
            return JsonResponse({"success":False , "message":"invalid upload code"})

def byifsc(request):
    if request.method == 'POST':
        ans = request.POST.get('ans')
        try:
            cur_user=bank.objects.get(ifsc=ans)
            data={}
            data["ifsc"]=cur_user.ifsc
            data["bank_id"]=cur_user.bank_id
            data["branch"]=cur_user.branch
            data["address"]=cur_user.address
            data["city"]=cur_user.city
            data["district"]=cur_user.district
            data["state"]=cur_user.state
            data["bank_name"]=cur_user.bank_name

            data_total=[]
            data_total.append(data)
            return render(request,"index.html",{'data':data ,"error":False})
        except:
            data={}
            return render(request,"index.html",{'data':data,"error":True})


def bydetalis(request):
    if request.method == 'POST':
        City= request.POST.get('city').upper()
        Name=request.POST.get('bank_name').upper()
        data_total=[]
        try:
            bank_found=bank.objects.filter(bank_name=Name,city=City)
            for bank_i in bank_found:
                data={}
                data["ifsc"]=bank_i.ifsc
                data["bank_id"]=bank_i.bank_id
                data["branch"]=bank_i.branch
                data["address"]=bank_i.address
                data["city"]=bank_i.city
                data["district"]=bank_i.district
                data["state"]=bank_i.state
                data["bank_name"]=bank_i.bank_name
                data_total.append(data)
            if(data_total):
                return render(request,"bank_det.html",{'data_total':data_total,'num':len(data_total),'error':False})
            else:
                return render(request,"bank_det.html",{'data_total':data_total,'error':True})
        except:
            return render(request,"bank_det.html",{'data_total':data_total,'error':True})

def detail_api(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if body["method"]== '1':
            try:
                ifsc_code=body["ifsc"].upper()
                cur_user=bank.objects.get(ifsc=ifsc_code)
                data={}
                data["ifsc"]=cur_user.ifsc
                data["bank_id"]=cur_user.bank_id
                data["branch"]=cur_user.branch
                data["address"]=cur_user.address
                data["city"]=cur_user.city
                data["district"]=cur_user.district
                data["state"]=cur_user.state
                data["bank_name"]=cur_user.bank_name
                return JsonResponse(data,safe=False)
            except:
                return JsonResponse({"error":"invalid credentials"})
        else:
            try:
                bank_found=bank.objects.filter(bank_name=body["bank_name"].upper(),city=body["city"].upper())
                data_total=[]
                for bank_i in bank_found:
                    data={}
                    data["ifsc"]=bank_i.ifsc
                    data["bank_id"]=bank_i.bank_id
                    data["branch"]=bank_i.branch
                    data["address"]=bank_i.address
                    data["city"]=bank_i.city
                    data["district"]=bank_i.district
                    data["state"]=bank_i.state
                    data["bank_name"]=bank_i.bank_name
                    data_total.append(data)
                return JsonResponse(data_total,safe=False)
            except:
                return JsonResponse({"error":"invalid credentials"})


        