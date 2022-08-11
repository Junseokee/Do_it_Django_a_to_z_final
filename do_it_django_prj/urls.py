
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', include('single_pages.urls'))
]
# {% for p in post_list %}
#     </hr>
#     <h2><a href="{{ p.get_absolute_url }}">{{ p.title }}</a></h2>
#     <h4>{{ p.created_at }}</h4>
#     <p>{{ p.content }}</p>
# {% endfor %}