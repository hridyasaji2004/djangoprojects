from django.shortcuts import render
from django.template.context_processors import request


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
#     if(request.method=="POST"):
#         print(request.POST)
#         weight = float(request.POST["weight"])
#         height = float(request.POST["height"])
#         bmi = weight / (height ** 2)
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
#         context = {'result':bmi}
#         return render(request,'addition.html',context)

def addition(request):
    if (request.method == "POST"):
        print(request.POST)
        weight = float(request.POST["weight"])
        height = float(request.POST["height"])
        height_in_meters = height / 100 
        bmi = weight / (height_in_meters ** 2)


        if (bmi <= 18.4):
            print("Underweight")
        elif (18.5 <= bmi <= 24.9):
            print("normal")
        elif (25.0 <= bmi <= 39.9):
            print("overweight")
        elif (bmi >= 40):
            print("obese")
        else:
            print("invalid")

        context = {'result': bmi}
        return render(request, 'addition.html',context)

    return render(request, 'addition.html')



# n=int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(fact)






