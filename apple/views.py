from django.shortcuts import render

# Create your views here.
def index(request):
    print("REQUEST METHOD:",request.method)
    print("PARAMS:",request.GET)
    data = request.GET.dict()
    #data = {"name":"Nischal Moktan","address":"Kamalbinayak"} 
    # data = {"students":[
    #     {
    #     "name":"Nischal Moktan",
    #     "address":"Kamalbinayak",
    #     "age":25,
    #     "course":"Csit",
    #     },
    #     {
    #     "name":"Krishal sangachhen",
    #     "address":"Dekocha",
    #     "age":30,
    #     "course":"Csit",
    #     },
    #      {
    #     "name":"Nishchaya Bhomi",
    #     "address":"Suryabinayak",
    #     "age":30,
    #     "course":"Csit",
    #     },
    #      {
    #     "name":"Samir KC",
    #     "address":"Dekocha",
    #     "age":30,
    #     "course":"Csit",
    #     },
    #      {
    #     "name":"Krishal sangachhen",
    #     "address":"Dekocha",
    #     "age":30,
    #     "course":"Csit",
    #     }
    # ]}
    return render(request,"index.html",context={"data":data})

def contact(request):
    data = {"students":[
        {
        "name":"Nischal Moktan",
        "address":"Kamalbinayak",
        "age":25,
        "course":"Csit",
        },
        {
        "name":"Krishal sangachhen",
        "address":"Dekocha",
        "age":30,
        "course":"Csit",
        },
        {
        "name":"Nishchaya Bhomi",
        "address":"Suryabinayak",
        "age":30,
        "course":"Csit",
        },
        {
        "name":"Samir KC",
        "address":"Dekocha",
        "age":30,
        "course":"Csit",
        },
        {
        "name":"Krishal sangachhen",
        "address":"Dekocha",
        "age":30,
        "course":"Csit",
        }
    ]}
    return render(request,"contact.html")

def about(request):
    data = {"students":[
        {
        "name":"Nischal Moktan",
        "address":"Kamalbinayak",
        "age":25,
        "course":"Csit",
        },
        {
        "name":"Krishal sangachhen",
        "address":"Dekocha",
        "age":30,
        "course":"Csit",
        },
         {
        "name":"Nishchaya Bhomi",
        "address":"Suryabinayak",
        "age":30,
        "course":"Csit",
        },
         {
        "name":"Samir KC",
        "address":"Dekocha",
        "age":30,
        "course":"Csit",
        },
         {
        "name":"Krishal sangachhen",
        "address":"Dekocha",
        "age":30,
        "course":"Csit",
        }
    ]}
    return render(request,"about.html")

