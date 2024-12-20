from django.shortcuts import render, redirect, get_object_or_404
from .models import init_img, post, comment, Key
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm, CommentForm, SignUpForm, LoginForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        if request.POST.get('key') == Key.objects.get(id=1).key:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('Posts')
        else:
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'Auth/Sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request.POST)
        # open('text.txt', 'w').write(f'{request.POST}')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('Posts')
    else:
        form =  AuthenticationForm()
    return render(request, 'Auth/Login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('Posts')
            
class PostEditView(UpdateView):
    model = post
    fields = ['title', 'content', 'image']
    template_name = 'Posts/Post_edit.html'

    def get_queryset(self):
        return post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('Post', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = post
    template_name = 'Posts/Post_delete.html'
    success_url = reverse_lazy('Posts')

    def get_queryset(self):
        return post.objects.filter(author=self.request.user)

@login_required

def Posts(request):
    init_imgs = init_img.objects.all()
    posts = post.objects.all().order_by('-date')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('Posts')
    else:
        form = PostForm()

    return render(request, 'Posts/Posts.html', {'init_imgs': init_imgs, 'posts': posts, 'form': form, 'user': request.user})

def Post(request, pk):
    init_imgs = init_img.objects.all()
    Post = get_object_or_404(post, pk=pk)
    comments = Post.solutions.all().order_by('-date')
    return render(request, 'Posts/Post.html', {'init_imgs': init_imgs, 'Post': Post, 'comments': comments,})

def add_comment(request, pk):
    Post = get_object_or_404(post, pk=pk)
    if request.method == 'POST':
        Comment = comment(Post=Post, title=request.POST['title'], content=request.POST['solutions'], author=request.user)
        Comment.save()
        return redirect('Post', pk=pk)
    return redirect('Post', pk=pk)
