from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.views.generic import CreateView
from .forms import DocumentForm, TelevisionForm, ConfigForm, EditForm
from .models import Document, Television, Config
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time
import shutil
import subprocess
from celery import task

def index(request):
    username = request.user.username
    responses = []
    #ping
    for tv in Television.objects.all():
        response = os.system("ping " + str(tv.tv_ip) +  " -n 1 -w 1") 
        name = tv.tv_name
        try:
            #query for latest entry of document sort by tv name 
            date = Document.objects.filter(tv__tv_name=name).latest('upload_date').upload_date
            print(date)
            responses.append([tv.tv_id, tv.tv_name, response, date])
        except Document.DoesNotExist: #error handling for tv not with no document uploaded 
            date = str('TV has no video')
            responses.append([tv.tv_id, tv.tv_name, response, date])

    print(responses)

    form = DocumentForm()
    args = {
        "form": form,
        "responses": responses,
    }

    if request.method == 'POST':
        for response in responses:   
            tv_id = response[0]
            tv_name = response[1]
            tv_status = response[2]
            try:
                date = respose[3]
            except:
                pass
            if str(tv_id) == str(request.POST.get('tv')):
                form = DocumentForm(request.POST, request.FILES)           
                if tv_status == 0: #check ping response
                    print(tv_name, 'is up!')
                    if form.is_valid(): 
                        TVName = Television.objects.get(tv_id = tv_id).tv_name
                        print(TVName)
                        print('valid form')
                        form.save()
                        print("saved")
                        src = r"../BCTC/media/videos/" + TVName + r".mp4"
                        dst = r"C:/RemoteVids/" + TVName + r".mp4"
                        shutil.copy(src, dst, follow_symlinks=True)
                        print('moved')
                        messages.success(request,'Video was uploaded')
                        return redirect(index)
                    else:
                        test = Television.objects.get(id= request.POST.get('tv'))
                else:
                    print(tv_name, 'is down!')
                    messages.error(request, 'TV is offline')
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
            messages.success(request,'Success')
        else:
            print(form.non_field_errors)
            print("form error")
            messages.error(request,'Error')

        return render(request, 'video_upload/add_tv.html',{"form": form})

def config_tv(request):
    if request.method =='GET':
        form = ConfigForm
        return render(request, 'video_upload/config_tv.html',{"form":form})
    elif request.method =='POST':
        #check for delete/edit 
        if '_delete_tv' in request.POST:
            tv1 = request.POST.get('TV')
            TVNAME = Television.objects.get(tv_id=tv1).tv_name
            Television.objects.get(tv_id=tv1).delete()
            messages.error(request,'TV was deleted')
            try:
                src = r"../BCTC/media/videos/" + TVNAME + r".mp4"
                dst = r"C:/RemoteVids/" + TVNAME + r".mp4"
                os.remove(src)
                os.remove(dst)
            except:
                pass
            return redirect(config_tv)

        elif '_edit_tv' in request.POST:
            #store tv choice in session 
            request.session['tv2'] = request.POST['TV']
            return redirect(edit_tv)
    

def edit_tv(request):
    if request.method == 'GET':
        #get tv choice from session to update IP
        edit = Television.objects.get(tv_id=request.session['tv2'])
        form = EditForm(instance=edit)
        args = {
            'edit':edit,
            'form':form
            }
        return render(request,'video_upload/edit_tv.html',args)

    elif request.method == 'POST':
        edit = Television.objects.get(tv_id=request.session['tv2'])
        form = EditForm(request.POST,instance=edit)

        if form.is_valid:
            form.save()
            messages.info(request,'IP was updated')
            args = {
                'edit':edit,
                'form':form
                }
        return redirect(edit_tv)
 





