from django.shortcuts import render
from django.http import HttpResponse
from .forms import DocumentForm 

# Create your views here.
# def index(request):
#     videos = Video.objects.all()[:10] #get first 10 videos 
#     ctx = { 
#         'videos' : videos 
#     }

#     return render(request, 'video_upload/index.html', ctx) #video_upload refers to the folder within templates

# def showvideo(request):
#     lastvideo = Video.objects.last()
#     videofile = lastvideo.videofile
#     form = VideoForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#             form.save()

#     ctx = {
#     'videofile':videofile,
#     'form':form
#     }

#     return render(request,'video_upload/videos.html', ctx)

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'video_upload/index.html') # placeholder for homepage/index
    else:
        form = DocumentForm()
    return render(request, 'video_upload/index.html', {
        'form': form
    })
