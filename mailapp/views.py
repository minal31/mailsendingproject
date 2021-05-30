from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings


# Create your views here.
def home(request):
    if request.method=='POST':
        #fetched form data 
        sub=request.POST.get('subject')
        msg=request.POST.get('body')
        # Example 1
        #send_mail(subject, message, from_email, recipient_list)
        message=send_mail(sub,msg, settings.EMAIL_HOST_USER,['mak31396@gmail.com',])
        
        #example 2
        msg='Welcome to online learning!!!'
        msg = EmailMultiAlternatives(sub, msg,settings.EMAIL_HOST_USER ,['poonambadgujar29@gmail.com','sarikakakulate@gmail.com','pableashwini610@gmail.com','mak31396@gmail.com','pableashwini610@gmail.com','tdmonika97@gmail.com'])
        msg.attach('ruby.jpg','/images')
        msg.send()

              
    return render(request,'mail.html')

# Create your views here.
