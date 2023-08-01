from django.shortcuts import render


def index(request):
    last_login_time = request.user.last_login_time
    return render(request, 'index.html', {'last_login_time': last_login_time})
