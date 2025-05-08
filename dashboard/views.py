from django.shortcuts import render,redirect

def view_401(request):
    return render(request, "dashboard/401.html")

def view_404(request):
    return render(request, "dashboard/404.html")

def view_500(request):
    return render(request, "dashboard/500.html")

def view_charts(request):
    return render(request, "dashboard/charts.html")

def view_index(request):
    return render(request, "dashboard/index.html")

def view_layout_sidenav_light(request):
    return render(request, "dashboard/layout_sidenav_light.html")

def view_layout_static(request):
    return render(request, "dashboard/layout_static.html")

def view_login(request):
    return render(request, "dashboard/login.html")

def view_password(request):
    return render(request, "dashboard/password.html")

def view_register(request):
    return render(request, "dashboard/register.html")

def view_tables(request):
    return render(request, "dashboard/tables.html")

def my_view(request):
    return render(request, 'base.html')  
    

