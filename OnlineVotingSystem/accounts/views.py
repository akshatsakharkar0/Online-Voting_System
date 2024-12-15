

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from voting.models import Election, Voter


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Voter instance for the newly registered user
            #Voter.objects.create(user=user)
            print("Form is valid and Voter created")

            # Log the user in after registration
            login(request, user)  # Automatically log the user in after registration

            return redirect('base')  # Redirect to the base page after successful registration
    else:
        form = UserRegistrationForm()
        print(form.errors)  # Print form errors to debug

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')  # Redirect to homepage or dashboard
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('base')  # Redirect to homepage after logout

@login_required
def vote(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    voter, created = Voter.objects.get_or_create(user=request.user)


    if voter.has_voted:
        return render(request, 'voting/error.html', {
            'message': "You have already voted in this election."
        })

    if request.method == 'POST':
        # Logic for handling the vote
        voter.has_voted = True
        voter.save()
        return HttpResponseRedirect('/success/')

    return render(request, 'voting/vote.html', {'election': election})