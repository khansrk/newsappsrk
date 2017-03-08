from django.shortcuts import render, redirect;
from django.contrib import auth;

def logout(request):
    auth.logout(request)
    return render(request,'newsapp/logout.html')

def login(request):
    if request.method == "GET":
        return render(request, "newsapp/login.html");
    elif request.method == "POST":
        username = request.POST['username'];
        password = request.POST['password'];

        # make sure the username & password is good
        user = auth.authenticate(username=username, password=password);

        if user is not None: # User was found & password matched
            if user.is_active:
                #associate the user with the session
                auth.login(request, user);

                return render(request,"newsapp/feeds_list.html")
            else:
                #account disabled
                return render(request, "newsapp/login.html", { "warning": "Your account is disabled" });
        else:
            # bad username and password
            return render(request, "newsapp/login.html", { "warning": "Invalid username and or password" });
    
def register(request):
    if request.method == "GET":
        return render(request, "newsapp/register.html");
    if request.method == "POST":
        username = request.POST["username"];
        password = request.POST["password"];
        email = request.POST["email"];
        if auth.models.User.objects.filter(username=username).exists() or auth.models.User.objects.filter(email=email).exists():
             return render(request,"auth/register.html",{ "warning": "Username or email Already exists" })
        else:  
            # call create_user from the ORM. Make sure you call save!
            auth.models.User.objects.create_user(username, email, password).save();
            #log the user in
            user = auth.authenticate(username = username, password = password);
            auth.login(request, user);
            return render(request, "newsapp/registered.html");
