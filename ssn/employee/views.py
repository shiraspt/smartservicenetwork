from django.shortcuts import render
from rest_framework.decorators import api_view
from Admin_.models import Location
from employee.models import Employee
# Create your views here.
def job_card():
  card_data=[
    {"job title":"ab","description":"hhtyyju","Budget":"69889","Date of Posting":"12-12-23","Expiary date":"1-3-24"},
             {"job title":"yry","description":"2ghyjy","Budget":"56787","Date of Posting":"15-12-23","Expiary date":"3-3-24"},
             {"job title":"ggh","description":"4467gdgd","Budget":"56787","Date of Posting":"15-12-23","Expiary date":"3-3-24"}
             ]
  return



# @api_view(['POST'])
# def reg_client(request):
#     msg = ""
#     try:
#         if request.method =='POST':
#             client_name=request.POST['client_name']
#             client_mob=request.POST['client_mob']
#             client_email=request.POST['client_email']
            
#             client_address=request.POST['client_address']
          
#             client_pword=request.POST['client_pword']


#             new_client = Client(
#                 client_name=client_name,
#                 client_phone=client_mob,
#                 client_email=client_email,
#                 client_Address=client_address,
#                 client_password=client_pword

#             )
#             new_client.save()
#             msg="New client added"
#             return JsonResponse({"success":"successfully registerd"})
        
#     except Exception as e:
#         return JsonResponse({"error": str(e) })
    


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


            new_employee = Employee(
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
