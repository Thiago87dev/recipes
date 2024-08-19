from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404


def register(request):
    request.session['number'] = request.session.get('number') or 0
    request.session['number'] += 1
    register_form_data = request.session.get('register_form_data')
    form = RegisterForm(register_form_data)
    return render(
        request,
        'authors/pages/register.html',
        {'form': form}
    )


def register_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('authors:register')
