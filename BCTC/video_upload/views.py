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

    responses = []
    #ping
    for tv in Television.objects.all():
        response = os.system("ping " + str(tv.tv_ip) +  " -n 1 -w 1") 
        responses.append([tv.tv_name,response])

    print(responses)

    form = DocumentForm()
    args = {
        "form": form,
        "responses": responses,
    }

    if request.method == 'POST':
        tv_id = request.POST.get('tv')
        hostname = Television.objects.get(tv_id = tv_id).tv_ip
        response = os.system("ping " + hostname +  " -n 1 -w 1") # ping once at hostname
        form = DocumentForm(request.POST, request.FILES)    
        # print(responses[tv_id])
        #check ping response
        # if responses[tv_id[0]] == 0:
        if response == 0:
            print(hostname, 'is up!')
            if form.is_valid(): 
                TVName = Television.objects.get(tv_id = tv_id).tv_name
                print(TVName)
                print('valid form')
                form.save()
                print("saved")
                src = r"../BCTC/media/videos/" + TVName + r".mp4"
                dst = r"../BCTC/media/RemoteVideos/" + TVName + r".mp4"
                shutil.copy(src, dst, follow_symlinks=True)
                print('moved')
                upload_status = "success"
            else:
                test = Television.objects.get(id= request.POST.get('tv'))
                upload_status = "failed"
        else:
            print(hostname, 'is down!')
            upload_status = "offline"
    
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



