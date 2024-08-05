from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.
import logging
import os
from .models import Register

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir,"ekyc_logs.log"), level=logging.INFO, format=logging_str, filemode="a")



def Home(request):
    if request.method == "POST":
        logging.info("Your request is post is succesfull lanuch ")

        first_name = request.POST['first_name']
        # print(first_name)
        last_name = request.POST['last_name']
        mobile_number = request.POST['mobile_number']
        pan_card = request.POST['pan_card']
        logging.info("Your All data is get !")
        if Register.objects.filter(pan_card=pan_card).exists():
            logging.info("This User Already present please show the login page")
            return HttpResponse("This is Login page beacuse you are alrady account")
        else:


            curr_data = Register( first_name=first_name, last_name =last_name ,mobile_number=mobile_number, pan_card=pan_card)
            curr_data.save()
            logging.info("Your Info save in this Tabkle Refistation   :"f"{first_name}{pan_card}")
            return render(request , 'home.html')
    else:
        logging.info("without post method call your page will we like this ")
        return render(request , 'home.html')

