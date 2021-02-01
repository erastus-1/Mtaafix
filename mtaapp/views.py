from .models import *
from . forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url = '/accounts/login')
def home(request):
    hoods = Neighbourhood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()

    return render(request,'home.html',locals())



@login_required(login_url = '/accounts/login')
def all_hoods(request):

    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Neighbourhood.objects.get(pk=request.user.join.hood_id.id)
            businesses = Business.objects.filter(hood=request.user.join.hood_id.id)
            posts = Post.objects.filter(hood=request.user.join.hood_id.id)
            comments = Comments.objects.all()

            return render(request, "hood/hood.html", locals())
        else:
            neighbourhoods = Neighbourhood.objects.all()
            return render(request, 'hood/hood.html', locals())
    else:
        neighbourhoods = Neighbourhood.objects.all()

        return render(request, 'hood/hood.html', locals())




@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)

    return render(request,'profile/profile.html',locals())



def create_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()
            redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/new_profile.html', locals())



@login_required(login_url='/accounts/login/')
def join(request, hoodId):
    neighbourhood = Neighbourhood.objects.get(pk=hoodId)
    if Join.objects.filter(user_id=request.user).exists():

        Join.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
    else:

        Join(user_id=request.user, hood_id=neighbourhood).save()

    messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('hoods')



def create_business(request):
    current_user = request.user
    print(Profile.objects.all())
    owner = Profile.get_by_id(current_user)
    
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_biz=form.save(commit=False)
            new_biz.user = current_user
            new_biz.save()
            return redirect('hoods')
    else:
        form = BusinessForm()
    return render(request,"business/new_business.html",locals())



def display_business(request):
    user = request.user
    owner = Profile.get_by_id(user)
    businesses = Business.objects.all()

    return render (request, 'business/business.html', locals())



@login_required(login_url='/accounts/login/')
def createHood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.user = request.user
            hood.save()
            messages.success(request, 'You Have succesfully created a hood.You may now join your neighbourhood')
            return redirect('home')
    else:
        form = CreateHoodForm()
        return render(request,'hood/create_hood.html',{"form":form})



@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if Join.objects.filter(user_id = request.user).exists():
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit = False)
                post.user = current_user
                post.hood = current_user.join.hood_id
                post.save()
                messages.success(request,'You have succesfully created a Forum Post')
                return redirect('hoods')
        else:
            form = PostForm()
            return render(request,'hood/new_post.html',locals())
    else:
        messages.error(request, 'Error! You can only create a forum post after Joining/Creating a neighbourhood')
        return redirect(request,'newpost.html',locals())



def comment(request,post_id):
    current_user=request.user
    post = Post.objects.get(id=post_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comments.objects.all()
    print(comments)
    if Join.objects.filter(user_id=request.user).exists():
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = current_user
                comment.save()
            return redirect('hoods')

        else:
            form = CommentForm()

        return render(request, 'business/comment.html', locals())



def search(request):
    if request.GET['hoods']:
        search_term = request.GET.get("hoods")
        hoods = Neighbourhood.search_hood(search_term)
        message = f"{search_term}"

        return render(request,'search.html',locals())

    else:
        message = "You Haven't searched for any item"
        return render(request,'search.html',locals())




