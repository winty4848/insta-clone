from django.urls import path

from .views import (
    AuthViewSet,
)

# 포스트 요청이 오면 AuthViewSet의 signup 메소드를 실행하겠다.
signup = AuthViewSet.as_view({
    'post': 'signup'
})

urlpatterns = [
    path('/signup', signup),
]