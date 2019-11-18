# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from companyapp.models import Company
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    return render(request, 'home.html', {})


def company_registration(request):
    if request.method == "POST":
        import pdb;pdb.set_trace()
        Company.objects.create(

            email=request.POST['email'],
            name=request.POST['name'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            phno=request.POST['phno'],
            dob=request.POST['dob'],
            profile_pic=request.FILES['image'],
            designation=request.POST['designation'],
        )
        return HttpResponseRedirect('/companyapp/')

    return render(request, 'com_registration.html', {})


def emp_registration(request):
    if request.method == "POST":
        Company.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            dob=request.POST['dob'],

            phno=request.POST['phno'],
            designation=request.POST['designation'],
            profile_pic=request.FILES['image'],

        )
        return HttpResponseRedirect('/companyapp/')

    return render(request, 'emp_registration.html', {})


# @login_required(login_url='/companyapp/com_login')
def count(request):
    # return HttpResponse("redirect" )
    # import pdb
    # pdb.set_trace()
    # return render(request, 'count.html', {})
    a = Company.objects.all()
    l = []
    data = {}
    for i in a:
        # l.append(i.designation)
        if i.designation not in l:
            l.append(i.designation)
    for i in l:
        # import pdb; pdb.set_trace()
        count = Company.objects.filter(designation=i).count()
        # print count
        data[i] = count

        # return render(request, 'count.html', {'i': count})
    return render(request, 'count.html', {'obj': data})


def count_list(request, company_designation):
    # import pdb;pdb.set_trace()
    count_list = Company.objects.filter(designation=company_designation)
    return render(request, 'count list.html', {'obj': count_list})
    # return HttpResponse('/roja/')


def details(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'details.html', {"obj": company})


def com_login(request):
    if request.method == "POST":
        import pdb;pdb.set_trace()
        username = request.POST['username'],
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # import pdb;pdb.set_trace()
            # return HttpResponse("success")
            return HttpResponseRedirect('/companyapp/count/')
        else:
            # import pdb;pdb.set_trace()
            return render(request, 'login_emp.html', {"error": "Invalid credentials"})
    return render(request, "login_emp.html", {})
