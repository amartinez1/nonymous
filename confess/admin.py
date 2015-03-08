from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "posted"
	fields = ("title", "text",'slug','total_likes','category')
	list_display = ["title", "posted","total_likes"]
	list_display_links = ["title"]
	list_filter = ["title"]
	search_fields = ["title"]
	

admin.site.register(Post, PostAdmin)
