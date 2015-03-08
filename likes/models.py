from django.db import models
from confess.models import  Post

VOTE_CHOICES=(
	(+1,'+1'),
	(-1,'-1'),
	(0,'0'),

)

class Like (models.Model):
	post = models.ForeignKey(Post)
	user_token = models.CharField(max_length=100)
	vote = models.SmallIntegerField(choices=VOTE_CHOICES)
	date = models.DateTimeField(auto_now_add=True)
	liked = models.BooleanField(default=False)
	label = models.CharField(max_length=30)

	class Meta:
		unique_together = (('user_token', 'post'),)
	def __unicode__(self):
		return unicode(self.post)

class MtmLike2Conf(models.Model):
	confession= models.ForeignKey(Post)
	like = models.ForeignKey(Like)