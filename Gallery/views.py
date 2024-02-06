from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View,generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from Gallery.forms import LoginForm,SignupForm,UploadImageForm
from .models import Images
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def Index(request):
    if request.user.is_authenticated:
        return redirect('gallery')

    return render(request, 'Gallery/index.html')

class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = 'Gallery/signup.html'
    success_url = reverse_lazy("login")
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(SignupView, self).dispatch(request)
   

    

class Login(LoginView):
    form_class = LoginForm
    template_name = 'Gallery/login.html'
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(Login, self).dispatch(request)

@login_required
def gallery(request):
    user_images= Images.objects.filter(user=request.user)
    context={"images":user_images}
    return render(request, 'Gallery/gallery.html', context)

@login_required
def UploadImage(request):
    post_form = UploadImageForm()
    if request.method == 'POST':
        post_form = UploadImageForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(to='gallery')
    else:
        post_form = UploadImageForm()
    return render(request, 'Gallery/upload_image.html', context={'post_form': post_form})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Images
    
    fields = ['description', 'image','title']
    template_name = 'Gallery/edit_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return redirect('gallery')
        return False

@login_required
def delete_image(request, id):
    post = Images.objects.get(id=id)
    post.delete()

    return redirect('gallery')