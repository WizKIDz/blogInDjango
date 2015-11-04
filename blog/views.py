from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import blog


def index(request):
    blogs = blog.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
        'blogs': blogs,
    })
    return HttpResponse(template.render(context))
def detail(request, blog_id):
	blog_something = blog.objects.get(pk=blog_id)

	return render(request, 'blog/detail.html', {'blog': blog_something})
