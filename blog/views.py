from django.shortcuts import render , get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Blog , Subscribtion , Category,Rate
from django.core.paginator import Paginator
from .forms import RateCommentForm

def index(request):
    query = request.GET.get('q')

    categories = Category.objects.all()
    banner_blogs = Blog.objects.all().order_by('-id')[:4]
    blogs = Blog.objects.all().order_by('?')
    top_rated = blogs.order_by('-rate_blogs__rate')[:3]
    top_commented = blogs.order_by('-rate_blogs')[:3]
    popular_posts = Blog.objects.all().order_by('-views')[:4]
    
    if query:
        blogs=blogs.filter(title_icontains=query)


    ctx = {
        'categories':categories,
        'banner_blogs': banner_blogs,
        'top_rated':top_rated,
        'blogs':blogs[:9],
        'blogs': blogs,
        'popular_posts': popular_posts,
        'top_commented':top_commented,

    } 
    return render(request , 'index.html' , ctx)


def single(request , slug):
    blog = get_object_or_404(Blog , slug=slug)
    relations = Blog.objects.filter(category=blog.category)[:3]
    comments = Rate.objects.filter( blog_id=blog.id).order_by('-id')
    form =  RateCommentForm(request.POST or None,request.FILES or None )
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
        return redirect(f'/single/{blog.slug}#comments')
    ctx = {
        'blog':blog,
        'form':form,
        'comments':comments,
        'relations':relations
    }

    return render(request , 'single.html' , ctx)

def category_wiew(request):
    category = request.GET.get('cat')
    page_number = request.GET.get('page')
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    if category:
        blogs = blogs.filter(category__title=category)

    paginator = Paginator(blogs,1)
    paginated_blogs=paginator.get_page(page_number)

    ctx = {
        'categories':categories,
        'blogs':paginated_blogs,
        'page_obj':paginated_blogs,
    }
    return render(request,'categories.html',ctx)