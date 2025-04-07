# models.py
from django.db import models
from django.core.cache import cache

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Invalidate the cache for this blog post when it is updated
        if self.pk:
            cache.delete(f'blog_post_{self.pk}')
        super().save(*args, **kwargs)
