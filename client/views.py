from datetime import date
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from client.models import Client, Work,Job_type
from Admin_.models import Location
from client.serializer import UserSerializer
from rest_framework.decorators import api_view
from datetime import datetime
def login(request):
    # return render(request,"login.html")


    return HttpResponse('fdgfdh')

@api_view(['POST'])
def reg_client(request):
    msg = ""
    try:
        if request.method =='POST':
            print("fdsds")
            client_name=request.POST['client_name']
            client_mob=request.POST['client_mob']
            client_email=request.POST['client_email']
            
            client_address=request.POST['client_address']
          
            client_pword=request.POST['client_pword']


            new_client = Client(
                client_name=client_name,
                client_phone=client_mob,
                client_email=client_email,
                client_Address=client_address,
                client_password=client_pword

            )
            new_client.save()
            msg="New client added"
            return JsonResponse({"success":"successfully registerd"})
        
    except Exception as e:
        return JsonResponse({"error": str(e) })
    

@api_view(['POST'])
def client_login(request):
    msg=""
    if request.method == 'POST':
        client_email1=request.POST["client_username"]
        client_pass=request.POST["client_password"]
        print(client_email1)
        try:
             client  = Client.objects.get(client_email=client_email1,client_password=client_pass)
             
             serialized_data= UserSerializer(client)
             return JsonResponse({"success":"successfully loged",'user':serialized_data.data})
         
        except Exception as e:
             return JsonResponse({"error":str(e)})
            



def register_work(request):
    
    
    msg = ""
    client_data = Client.objects.get(id=request.session['client'])
    location_list = Location.objects.all()
    category_list = Job_type.objects.all()
    
    context={
        'location_list':location_list,
        'msg':msg,
        'category_list':category_list,
       
    } 
    if request.method =='POST':
        try:
            
            location_id = int(request.POST['work_location'])
            
            description = request.POST['work']
            work_duration=request.POST['duration']
            work_cost = request.POST['cost']
            jobtype_id = int(request.POST['jobtype'])
            work_location_id = int(request.POST['loc'])

            location = location.objects.get(id=work_location_id)



            
            
            location_id = location.id
            category=Job_type.objects.get(id=jobtype_id)
            workcategory_id = category.id
            
        
          
            status ='new'
          
            day = date.today()
            
            y = day.strftime("%Y")
            m= day.strftime("%m")
            d= day.strftime("%d")
            today_works = Work.objects.filter(complaint_date = day).count()
            w = today_works+1
            c=str(w).zfill(3)
            work_number = (d+m+y[2]+y[3]+c)
            client=client_data.id
           
           
            # date1 = datetime.strptime(purchase_date, '%d/%m/%Y')
            date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
           
            today= day-date_object
          


            
            # complaint_data = {'cus_name':cus_name,'cus_phone1':cus_phone1,'cus_phone2':cus_phone2,'cus_email':cus_email,'cus_address':cus_address,'location_name':location_name,'product_category_id':product_category_id,'product_model_id':product_model_id,'complaint':complaint,'purchase_date':purchase_date,'productcategory_name':productcategory_name,'model_name':model_name,'technician_name':technician_name,'warrenty':warrenty,'physical_damage':physical_damage,'day':day,'complaint_number':complaint_number,'status':status}
            
            work_number = (d+m+y[2]+y[3]+c)
            new_work = Work(
               
                location = location_id,
                date = today,
                worknumber=int(work_number),
                work_details=description,
                status=status,
                work_duration=work_duration,
                
                cost=work_cost,
                client=client
            )
           
            new_work.save()
            
            
            
          
            
    

        #     send_mail(
        #     'complaint registerd',
            
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [cus_email],
        #     fail_silently = False 
        # )


            return render (request,"added_data.html",{'complaint_data':complaint_data})

        except Exception as e:
            print(e)
                 

        
    else:
        return render (request,"register_work.html",context)
