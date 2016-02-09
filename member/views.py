from django.http import HttpResponse
from django.template import loader, RequestContext
from member.models import User

# Create your views here.


def registration(request):
    template = loader.get_template('member/registration.html')
    context = RequestContext(request, {
        'foo': 'bar'})

    return HttpResponse(template.render(context))

def registration_process(request):
    user_name = request.POST.get("username")
    user_email = request.POST.get("email")
    user_password = request.POST.get("password")
    # result = user_name + "/" + user_email + "/" +user_password
    user_object = User.objects.create()

    user_object.email= user_email
    user_object.user_name = user_name
    user_object.password = user_password

    user_object.save()

    return HttpResponse(user_object.email)
    # return HttpResponse(template.render(context))

def logout_process(request):
    request.session.pop("member_email")

    template = loader.get_template('home/home.html')
    context = RequestContext(request, {
    'foo': 'bar'})
    return HttpResponse(template.render(context))

