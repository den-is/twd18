from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
import json

from .models import Category, Page, UserProfile
from .forms import CategoryForm, PageForm, UserProfileForm
from .bing_search import run_query

import logging
logger = logging.getLogger(__name__)

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {'top5categories': category_list, 'top5pages': pages_list}

    visits = request.session.get('visits', 1)
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')

    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], '%Y-%m-%d %H:%M:%S')

        if (datetime.now() - last_visit_time).days > 0:
            visits += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits

    context_dict['visits'] = visits

    return render(request, 'rango/index.html', context_dict)

def about(request):
    if request.session.get('visits'):
        count = request.session.get('visits')
    else:
        count = 0

    return render(request, 'rango/about.html', {'visits': count})

def category(request, category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            context_dict['result_list'] = run_query(query)
            context_dict['query'] = query

    category = get_object_or_404(Category, slug=category_name_slug)
    context_dict['category_name'] = category.name
    pages = category.page_set.order_by('-views')
    context_dict['pages'] = pages
    context_dict['category'] = category

    if not context_dict['query']:
        context_dict['query'] = category.name

    return render(request, 'rango/category.html', context_dict)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            newcat = form.save()

            logger.info('Category "{}" created by user "{}"'.format(newcat.name, request.user.username))

            return redirect(reverse('rango:index'))
        else:

            logger.warning('Unsuccessful category creation attempt')

            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                newpage = page.save()

                logger.info('Page "{}" created by user "{}"'.format(newpage.title, request.user.username))

                return redirect(reverse('rango:category', args=(category_name_slug, )))
        else:
            logger.warning('Unsuccessful page creation attempt')
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'rango/add_page.html', context_dict)

@login_required
def search(request):

    if request.method == 'POST':
        result_list = []
        query = request.POST['query'].strip()

        if query:
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})

def track_url(request):
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = int(request.GET['page_id'])
            page = get_object_or_404(Page, pk=page_id)
            page.views += 1
            page.save()

            return redirect(page.url)

    return redirect(reverse('rango:index'))

def register_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            messages.success(request, 'Profile details updated')

            return redirect(reverse('rango:index'))
        else:
            logger.warning('Unsuccessful registration atempt')
            messages.error(request, 'Fill in all required fields')
    else:
        form = UserProfileForm()

    return render(request, 'rango/profile_registration.html', {'form': form})

@login_required
def edit_profile(request):

    profile = UserProfile.objects.get(user_id=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)

        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)

            if 'picture' in request.FILES:
                new_profile.picture = request.FILES['picture']

            new_profile.save()

            logger.info('Profile updated. user: {}'.format(request.user.username))
            messages.success(request, 'Profile details updated')

            return redirect(reverse('rango:index'))
        else:
            logger.warning('Unsuccessful profile edition atempt')
            messages.error(request, 'Fill in all required fields')
    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'rango/profile.html', {'profile_form': profile_form})

@login_required
def user_area(request, user_name):
    users = UserProfile.objects.all().exclude(user_id=1).exclude(user_id=request.user.id)

    user = get_object_or_404(User, username=user_name)
    profile = get_object_or_404(UserProfile, user_id=user)#.id

    return render(request, 'rango/user_area.html', {'users': users, 'profile': profile})

@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()

    return HttpResponse(likes)

def get_category_list(max_results=0, starts_with=''):
    cat_list = []

    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if cat_list.count() > max_results:
            cat_list = cat_list[:max_results]

    return cat_list

def suggest_category(request):

    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']

    cat_list = get_category_list(8, starts_with)

    return render(request, 'rango/cats.html', {'cats': cat_list})

@login_required
def auto_add_page(request):
    if request.method == 'GET':
        cat_id = request.GET.get('category_id', False)
        url = request.GET.get('url', False)
        title = request.GET.get('title', False)
        if cat_id and url and title:
            category = get_object_or_404(Category, id=int(cat_id))
            page = Page.objects.get_or_create(category=category, title=title, url=url)
            if page[1]:
                response_data = {'page_id': page[0].id}
                return HttpResponse(json.dumps(response_data))
