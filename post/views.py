from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Project,Comments,Rating
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,NewProfileForm,CommentForm,VotingForm
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
# from .models import  MoringaMerch
from .serializers import ProfileSerializer,ProjectSerializer
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    # ones_project = Project.objects.all()
    # all_projects = Project.get_all_projects()
    return render(request, 'welcome.html', {"date": date})

@login_required(login_url='/accounts/login/')
def index(request):
    ones_project = Project.objects.all()
    all_projects = Project.get_all_projects()
    return render(request, 'index.html', {"all_projects": all_projects,"ones_project":ones_project})


@login_required(login_url='/accounts/login/')
def upload_project(request):

    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'upload_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def my_profile(request):

    current_user = request.user
    my_projects = Project.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"my_projects":my_projects, "my_profile":my_profile})

@login_required(login_url='/accounts/login/') 
def one_project(request,id):

    ones_project = Project.objects.filter(id = id)

    all_ratings = Rating.objects.filter(project = id) 
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = id
            rate.save()
        return redirect('oneproject',id)
        
    else:
        form = VotingForm() 

    calculate = Rating.objects.filter(project = id)
    usability = []
    design = []
    content = []
    average_usability = 0
    average_design = 0
    average_content = 0

    for x in calculate:
        usability.append(x.usability)
        design.append(x.design)
        content.append(x.content)

        if len(usability)>0 or len(design)>0 or len(content)>0:
            average_usability+= round(sum(usability)/len(usability))
            average_design+= round(sum(design)/len(design))
            average_content+= round(sum(content)/len(content))
        else:
            average_usability = 0.0
            average_design = 0.0
            average_content = 0.0
    
    return render(request,'project.html',{"ones_project":ones_project,"all_ratings":all_ratings,"form":form,"usability":average_usability,"design":average_design,"content":average_content})


@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'project_name' in request.GET and request.GET["project_name"]:
        search_term = request.GET.get("project_name")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, "search.html",{"message":message,"project": searched_project})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def add_comment(request, proj_id):
    current_user = request.user
    project_item = Project.objects.filter(id = proj_id).first()
    profiless = Profile.objects.filter(user = current_user.id).first()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = profiless
            comment.commented_project = project_item
            comment.save()
            return redirect('index')

    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {"form": form, "proj_id": proj_id})

@login_required(login_url='/accounts/login/')
def comment(request, id):
    mycomments = Comments.objects.filter(commented_project = id).all()
    return render(request, 'comments.html', {"mycomments":mycomments})


class ProfileList(APIView):
    def get(self, request, format=None):
        all_users = Profile.objects.all()
        serializers = ProfileSerializer(all_users, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)