from django.shortcuts import render
from app1.forms import AdditionForm,BmiForm,calorieForm

def addition(request):
    if (request.method == "POST"):
        print(request.POST)  #submitted data
        # creating form_instance using submitted data
        form_instance = AdditionForm(request.POST)
        # check whether the data is valid
        if form_instance.is_valid():
            #proces data
            data = form_instance.cleaned_data #valiated data
            print(data)
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}
            return render(request, 'addition.html',context)


    if(request.method=="GET"):
        form_instance=AdditionForm()    #empty form obj created
        context={'form':form_instance}
        return render(request,'addition.html',context)



def bmi(request):
    if (request.method == "POST"):
        print(request.POST)  #submitted data
        # creating form_instance using submitted data
        form_instance = BmiForm(request.POST)
        # check whether the data is valid
        if form_instance.is_valid():
            #proces data
            data = form_instance.cleaned_data #valiated data
            print(data)
            w=data['weight']
            h=data['height']
            b=int(w/((int(h)/100)**2))
            context={'result':b,'form':form_instance}
            return render(request, 'bmi.html',context)


    if(request.method=="GET"):
        form_instance=BmiForm()    #empty form obj created
        context={'form':form_instance}
        return render(request,'bmi.html',context)



def Signup(request):
    if (request.method == "POST"):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            return render(request, 'Signup.html')



    if(request.method=="GET"):
        form_instance = SignupForm()
        context={'form':form_instance}
        return render(request,'Signup.html',context)




def calorie(request):
    if (request.method == "POST"):
        form_instance = calorieForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            print(data)
            w=int(data['weight'])
            h=int(data['height'])
            a=int(data['age'])
            g=data['gender']
            al=float(data['activity_levels'])
            print(w,h,a,g,al)
            if g=="male":
                bmr=10*w*6.25*h-5*a-5    #for men
            else:
                bmr=10*w+6.25*h-5*a-161  #for women
                print(bmr)
            c=bmr*al
            context={'result':c,'form':form_instance}




            return render(request, 'calories.html',context)



    if(request.method=="GET"):
        form_instance = calorieForm()
        context={'form':form_instance}
        return render(request,'calories.html',context)




















# def addition(request):
#     if(request.method=="POST"):
#         print(request.POST)
#         n1=int(request.POST['n1'])
#         n2=int(request.POST['n2'])
#         s=n1+n2
#         context={'result':s}
#         return render(request,'addition.html',context)

# def addition(request):
#     if(request.method=="POST"):
#         print(request.POST)
#         n1=int(request.POST['n1'])
#         fact=1
#         for i in range(1,n1+1):
#             fact=fact*i
#             print(fact)
#
#         context={'result':fact}
#         return render(request,'addition.html',context)
#


# def addition(request):
#     if (request.method == "POST"):
#         print(request.POST)
#         weight = float(request.POST["weight"])
#         height = float(request.POST["height"])
#         height_in_meters = height / 100
#         bmi = weight / (height_in_meters ** 2)
#
#
#         if (bmi <= 18.4):
#             print("Underweight")
#         elif (18.5 <= bmi <= 24.9):
#             print("normal")
#         elif (25.0 <= bmi <= 39.9):
#             print("overweight")
#         elif (bmi >= 40):
#             print("obese")
#         else:
#             print("invalid")
#
#         context = {'result': bmi}
#         return render(request, 'addition.html',context)
#
#     return render(request, 'addition.html')
#







