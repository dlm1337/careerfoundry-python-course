from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            # Redirect to a success page or login page after registration
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "customuser/register.html", {"form": form})

@login_required  # Require login to access this view
def your_profile(request):
    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            # Redirect to a success page or the profile page itself after successful update
            return redirect("your_profile")
    else:
        form = CustomUserUpdateForm(instance=request.user)  # Prefill the form with existing user data

    return render(request, "customuser/your_profile.html", {"form": form})
 
