from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.views.generic import CreateView
from .forms import DocumentForm, TelevisionForm, DeleteTvForm
from .models import Document, Television, DeleteTv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
import shutil
import subprocess

def index(request):

    # hostname = "10.30.125.20" #long shing
    # hostname2 = "10.30.125.125" #york
    # hostname3 = "10.30.125.130" #ashley
    # hostname4 = " 10.30.126.6" #me

    if request.method == 'GET':
        responses = []
        #ping
        for tv in Television.objects.all():
            response = os.system("ping " + str(tv.tv_ip) +  " -n 1 -w 1") 
            responses.append([tv.tv_name,response])

        form = DocumentForm()
        args = {
            "form": form,
            "responses": responses,
        }
        return render(request, 'video_upload/index.html', args)

    elif request.method == 'POST':
        tv_id = request.POST.get('tv')
        print(tv_id)
        hostname = Television.objects.get(tv_id = tv_id).tv_ip
        print(hostname)
        response = os.system("ping " + hostname +  " -n 1 -w 1") # ping once at hostname
        print(response)

        form = DocumentForm(request.POST, request.FILES)    
        #check ping response
        if response == 0:
            print(hostname, 'is up!')
            
            if form.is_valid(): 
                TVName = Television.objects.get(tv_id = tv_id).tv_name
                print(TVName)
                print('valid form')
                form.save()
                print("saved")
                src = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/" + TVName + r".mp4"
                dst = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/RemoteVideos/" + TVName + r".mp4"
                shutil.copy(src, dst, follow_symlinks=True)
                print('moved')
                #src = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/TV1.mp4"
                #dst = r"C:/Users/Administrator/Desktop/Django Projects/BCTC/media/test/"
                upload_status = "success"
            else:
                test = Television.objects.get(id= request.POST.get('tv'))
                upload_status = "failed"
            # return render(request, 'video_upload/index.html',{"upload_status":upload_status,"form":form})
        else:
            print(hostname, 'is down!')
            upload_status = "offline"
        responses = []
        #ping
        for tv in Television.objects.all():
            response = os.system("ping " + str(tv.tv_ip) +  " -n 1 -w 1") 
            responses.append([tv.tv_name,response])
        args = {
            "form": form,
            "upload_status":upload_status,
            "responses": responses,
        }     
        return render(request, 'video_upload/index.html',args)

def add_tv(request):
    if request.method == 'GET':
        form = TelevisionForm()
        return render(request, 'video_upload/add_tv.html',{"form": form})
    elif request.method == 'POST':
        form = TelevisionForm(request.POST)
        if form.is_valid(): 
            form.save()
            print("form saved")
            upload_status = "success"
        else:
            print(form.non_field_errors)
            print("form error")
            upload_status = "fail"
        return render(request, 'video_upload/add_tv.html',{'upload_status':upload_status, "form": form})

def delete_tv(request):
    if request.method =='GET':
        form = DeleteTvForm
        return render(request, 'video_upload/delete_tv.html',{"form":form})
    elif request.method =='POST':
        #action check for delete/edit 
        if '_delete_tv' in request.POST:
            tv1 = request.POST.get('TV')
            Television.objects.get(tv_id=tv1).delete()
            messages.info(request,'TV successfully deleted')
            return  redirect(delete_tv)
        #edit section to be worked on 
        elif '_edit_tv' in request.POST:
            tv2 = request.POST.get('TV')
            tv_edit = Television.objects.get(tv_id=tv2)
            return  redirect(index)



