from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import ProfileChangeFrom, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required 

from . import forms

class SignUp(CreateView):
    form_class = forms.ProfileCreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("myapp/register")


# class ProfileUpdate(UpdateView):
#     # form = ProfileChangeFrom(instance="username")
#     form_class = forms.ProfileChangeFrom
#     success_url = reverse_lazy("home")
#     template_name = "accounts/profile.html"
# below is the new user. 
# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })