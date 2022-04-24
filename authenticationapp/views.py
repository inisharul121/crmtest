from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.shortcuts import render
from .form import CreateUserForm

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method=='POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Ask query"

            message = request.POST.get('message') #"\n".join(form.values())
            username = request.POST.get('username')
            email = request.POST.get('email')
            fields= ('User Name: '+ username + '\n'+ 'Email Address: '+ email +'\n'+ 'Message: '+ message )

            #try:
            send_mail(subject,fields, 'inisharul1640@gmail.com', ['inisharul1640@gmail.com'])
            #except BadHeaderError:
                #return HttpResponse('Invalid header found.')
            return redirect("register")

    context={'form':form}
    return render(request,'register.html', context)

