from django.views.generic import FormView, DetailView, ListView
from django.shortcuts import render_to_response
from .models import Post
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from .forms import ConfessForm
from likes.middleware import retrieve_token
from endless_pagination.decorators import page_template
from likes.models import Like, MtmLike2Conf


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):

        user_token = retrieve_token(self.request)

        print "User like token has [%s]" % user_token

        print ("creating dic to containg a post and if current user has liked the posts")
        post2tokns = {}
        has_ever_liked = True
        for post in Post.objects.all():
            token_list = []
            likes = Like.objects.filter(post= post)
            print("likes list[%s]"%likes)
            if likes is not None and len(likes) is not 0:
                for like in likes:
                    token_list.append(like.user_token)
                if token_list is not None and len(token_list) is not 0:
                    if user_token not in token_list:
                        print("user token [%s] not in list"%user_token)
                        has_ever_liked = False 
                        post2tokns[post] = has_ever_liked
                    else:
                        print("user token [%s] is in list"%user_token)
                        has_ever_liked = True
                        post2tokns[post] = has_ever_liked
            else:
                has_ever_liked = False
                post2tokns[post] = has_ever_liked   


        print("ref dictionary is [%s]"% post2tokns)
        print("posts[%s]"%Post.objects.all())

        # Call the base implementation first to get the context
        context = super(PostListView, self).get_context_data(**kwargs)

        # Add in a QuerySet of all the books
        context['likes'] = Like.objects.all()

        # add the user token also
        context['user_token'] = retrieve_token(self.request)

        # add post2tokens dict
        context['post2tokens'] = post2tokns

        return context


@page_template('post_page.html')  # just add this decorator
def postList(request, template='confess.html', extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)

    obj = Post.objects.all()
    userLike = Like.objects.all()

    context['objects'] = obj
    context['likes'] = userLike
    print("likes objects : [%s]", context['likes'])
    return render_to_response(
        template, context, context_instance=RequestContext(request))


@page_template('post_page.html')  # just add this decorator
def popularList(
        request, template='confess.html', extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)

    obj = Post.objects.filter(category='PO')
    context['objects'] = obj
    return render_to_response(
        template, context, context_instance=RequestContext(request))


@page_template('post_page.html')  # just add this decorator
def newList(
        request, template='confess.html', extra_context=None):

    context = {}
    if extra_context is not None:
        context.update(extra_context)

    obj = Post.objects.filter(category='NE')
    context['objects'] = obj
    return render_to_response(
        template, context, context_instance=RequestContext(request))


class ConfessForm(FormView):
    template_name = "post_form.html"
    form_class = ConfessForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        category = 'NE'
        post = Post()
        post.title = form.cleaned_data['title']
        post.text = form.cleaned_data['text']
        post.category = category
        post.save()

        return super(ConfessForm, self).form_valid(form)


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
