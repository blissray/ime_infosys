from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from member.models import User


def home(request):
    template = loader.get_template('home/home.html')
    context = RequestContext(request, {
    'foo': 'bar'})
    return HttpResponse(template.render(context))

def start_page(request):
    template = loader.get_template('home/start_page.html')
    context = RequestContext(request, {
    'foo': 'bar'})
    return HttpResponse(template.render(context))

def login_process(request):
    if request.method == 'POST':

        email = request.POST.get("student_id")
        password = request.POST.get("password")

        try:

            user_object = User.objects.get(email=email)

            if password == user_object.password:
                template = loader.get_template('home/start_page.html')

                request.session["member_email"] = email

                context = RequestContext(request, {'student_id': email})
                return HttpResponse(template.render(context))
            else:
                return HttpResponse("Error Error")
        except:
            return HttpResponse("Error Error")

    # template = loader.get_template('home/registration.html')
    # context = Context()
