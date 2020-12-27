from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (View, 
                                  ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView
)

# Create your views here.
#main.apps.Mianconfig done
#lists of dic posts

class PostListView(ListView):
    model = Post
    template_name = 'main/blog_main.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

# def blog_main (request):
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request, 'main/blog_main.html',context)


# filtering post per user imported user model and get_object_or_404()

class UserPostListView(ListView):
    model = Post
    template_name = 'main/userhomepage.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detailview.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['movie_name', 'review']
    template_name = 'main/createview.html'
    # setting the current user as author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['movie_name', 'review']
    template_name = 'main/createview.html'
    # setting the current user as author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #  checkin if the user is == author of the Post
    #  only then he can update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: 
            return True                                       
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'main/deleteview.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: 
            return True                                       
        else:
            return False
        
       
   

def about(request):
    return render(request, 'main/about.html',{'title' : 'About Me'})