from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from client.models import Client
from client.serializer import UserSerializer
from rest_framework.decorators import api_view

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
            
@api_view(['POST'])
def reg_employee(request):
    location_list = Location.objects.all()
    msg = ""
    context = {
        'msg':msg,
        'location_list':location_list

    }
    try:
        if request.method =='POST':
            emp_name=request.POST['emp_name']
            emp_mob=request.POST['emp_mob']
            emp_email=request.POST['emp_email']
            emp_age=request.POST['emp_age']
            emp_gender=request.POST['emp_gender']
            emp_location_id=int(request.POST['work_location'])
            emp_location = Location.objects.get(id = emp_location_id).location
            emp_loc_id = Location.objects.get(id = emp_location_id).id
            emp_address=request.POST['emp_address']
            emp_photo = request.FILES['emp_photo']
            emp_jdate=request.POST['emp_jdate']
            emp_pword=request.POST['emp_pword']
            # print(emp_location_id)


            new_employee = employee(
                emp_name=emp_name,
                emp_phone=emp_mob,
                emp_email=emp_email,
                emp_age=emp_age,
                emp_gender=emp_gender,
                emp_location=emp_location,
                emp_Address=emp_address,
                emp_photo=emp_photo,
                emp_jdate=emp_jdate,
                emp_password=emp_pword,
                location_id = emp_loc_id
            )
            new_employee.save()
             
            msg="New employee added"
            
        
    except Exception as e:
        print(e)
        msg = e

    context = {
        'msg':msg,
        'location_list':location_list

    }


def register_work(request):
    
    
    msg = ""
    client_data = Client.objects.get(id=request.session['client'])
    location_list = Location.objects.all()
    category_list = work_category.objects.all()
    
    context={
        'location_list':location_list,
        'msg':msg,
        'category_list':category_list,
       
    } 
    if request.method =='POST':
        try:
            
            client_name=request.POST['client_name']
            client_phone1=request.POST['client_phone']
            client_phone2=request.POST['client_phone']
            client_email=request.POST['client_email']
            client_address=request.POST['client_address']
            work_location_id = int(request.POST['work_location'])
            
            work = request.POST['work']
            cost = request.POST['cost']
            location = Location.objects.get(id=work_location_id)



            productcategory = Product_category.objects.get(id=product_category_id)
            model=Product_models.objects.get(id=product_model_id)
            location_id = location.id
            location_name = location.location
            workcategory_id = productcategory.id
            workcategory_name = productcategory.category
          



            technicians = Technician.objects.filter(location_id=location_id)
            technician = random.choice(technicians)
            technician_id = technician.id
            technician_name = technician.tec_name
          
            status ='new'
          
            day = date.today()
            # t=day - pd
            y = day.strftime("%Y")
            m= day.strftime("%m")
            d= day.strftime("%d")
            today_works = Work.objects.filter(complaint_date = day).count()
            w = today_works+1
            c=str(w).zfill(3)
            complaint_number= d+m+y[2]+y[3]+c
           
          
           
            # date1 = datetime.strptime(purchase_date, '%d/%m/%Y')
            date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
           
            d= day-date_object
          


            
            complaint_data = {'cus_name':cus_name,'cus_phone1':cus_phone1,'cus_phone2':cus_phone2,'cus_email':cus_email,'cus_address':cus_address,'location_name':location_name,'product_category_id':product_category_id,'product_model_id':product_model_id,'complaint':complaint,'purchase_date':purchase_date,'productcategory_name':productcategory_name,'model_name':model_name,'technician_name':technician_name,'warrenty':warrenty,'physical_damage':physical_damage,'day':day,'complaint_number':complaint_number,'status':status}
            

            new_work = Work(
                client_name = client_name,
                client_phone1 = client_phone1,
                client_phone2 = client_phone2,
                client_email =client_email,
                client_address = client_address,
                client_location = location_name,
                location_id = location_id,
                category_name = productcategory_name,
                category_id  = productcategory_id,
                model_name =model_name,
                model_id = model_id,
                complaint_des = complaint,
                purchase_date = purchase_date,
                complaint_date =day,
                warrenty = warrenty,
                physical_damage = physical_damage,
                technician_name = technician_name,
                technician_id = technician_id,
                
                cce_id = cce_data.id,
                complaint_name = complaint_number,
            )
           
            new_work.save()
            
            
            message = "Your complaint registerd with complaint number " +complaint_number+".Our technician will contact you soon"
            msg = "Work assigned to " + technician_name + " with complaint number " + complaint_number
          
            
    

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
