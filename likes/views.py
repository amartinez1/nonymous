# Create your views here.
from django.http import HttpResponse
from django.db.models import Sum
from confess.models import Post
from .middleware import retrieve_token
from .models import Like, MtmLike2Conf
from django.views.generic import TemplateView
import logging
from django.core import serializers
import json

logging.basicConfig()
logger = logging.getLogger(__name__)
VOTE = +1

''' This Class handles the like feature, if an user likes first time it creates a token, if an user has alredy liked a Post
it wil be unliked or downvoted '''


class like(TemplateView):

    def get(self, request, *args, **kwargs):
    	logger.info('Entry')
    	count = 0
        label = 'Unlike'
        post_id = request.GET['confession_id']
        user_token = retrieve_token(request)
        posts = Post.objects.get(id=int(post_id))

        # check if user has liked specified post
        if Like.objects.filter(post=posts, user_token=user_token).exists():
            user_like = Like.objects.get(post=posts, user_token=user_token)

            if int(user_like.post.id) == int(post_id) and user_like.user_token == user_token:
                if user_like.liked == False:
                    user_like.vote = VOTE
                    user_like.liked = True
                    user_like.label = label
                    user_like.save()

                    posts.liked = True
                    posts.total_likes = posts.total_likes + 1
                    posts.save()

                    data = {
                        'count': posts.total_likes,
                        'label': label,
                        'user_token': user_token
                    }

                    result = json.dumps(data)

                    print result

                    return HttpResponse(result, content_type='application/json')

                else:

                    label = 'Like'
                    user_like.label = label
                    user_like.save()
                    count = unlike(request, posts, user_token)
                    data = {
                        'count': count,
                        'label': label,
                        'user_token': user_token
                    }
                    result = json.dumps(data)
                    return HttpResponse(result, content_type='aplication/json')

        else:
            # "create  the like object..."
            like = Like(post=Post.objects.get(id=post_id),
                        user_token=user_token, vote=VOTE, liked=True)
            like.label = label
            like.save()

            posts.liked = True
            posts.total_likes = posts.total_likes + 1
            posts.save()

            # update many to many reference object
            print("creating many to many relashionship obj")
            mtm_like_2_conf = MtmLike2Conf(confession=posts, like=like)
            mtm_like_2_conf.save()
            print("mtm created [%s]"% mtm_like_2_conf)

            print like.post, like.user_token, like.vote, like.id
            like = like.id

            print "saved!!!"
            count = posts.total_likes
            data = {
                'count': count,
                'label': label,
                'user_token': user_token
            }
            result = json.dumps(data)
            return HttpResponse(result, content_type='aplication/json')


def unlike(request, posts, user_token):
	'''This metod downvotes or unlikes a post, sparams: request, post Object , user_token'''
	down_vote = 0

	post_obj = Post.objects.get(id=posts.id)
	post_obj.total_likes = post_obj.total_likes - 1
	post_obj.save()

	like = Like.objects.get(post=post_obj, user_token=user_token)
	like.vote = down_vote
	like.liked = False
	like.save()

	# count = like_count(request, post_obj)
	count = post_obj.total_likes
	return count

def like_count(request, post):

    like = Like.objects.filter(post=post)
    likes = 0
    # prueba--contando likes 
    if like.exists():
        likes = like.aggregate(Sum('vote'))['vote__sum'] or 0
        post.total_likes = likes
        post.save()
        return likes
    else:
        post.total_likes = likes
        post.save()
        return likes

class fill_modal(TemplateView):

    def get(self, request, *args, **kwargs):

        post_id = request.GET['id']
        post = Post.objects.get(id=post_id)

        data = serializers.serialize(
            'json', [post, ], fields=('pk', 'title', 'text', 'posted', 'total_likes'))
        struct = json.loads(data)

        data = json.dumps(struct[0])
        return HttpResponse(data, content_type='application/json')

class user_like(TemplateView):

    def get(self, request, *args, **kwargs):

        token = retrieve_token(request)

        post_id = request.GET['id']

        like_obj = Like.objects.get(post=post_id, user_token=token)

        data = {'label': like_obj.label}
        result = json.dumps(data)
        return HttpResponse(result, content_type='aplication/json')
