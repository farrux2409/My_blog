from django.views.generic import ListView

from blog.models import Post


class PostListViews(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'
