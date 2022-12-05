from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from authention.views import MyObtainTokenPairView,get_all_client,updateclient,lockclient,get_all_employer,put_employer,lock_employer
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

router = routers.SimpleRouter()

#router.register('user',UserViewset,basename='user')


BASENAME="api/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASENAME+"login/", MyObtainTokenPairView.as_view(),name="token_obtain_pair"),
    #path(BASENAME+'login/',Connexion),
    path(BASENAME+'client/',get_all_client),
    path(BASENAME+'client/<int:uid>/',get_all_client),
    path(BASENAME+'client/update/<int:uid>/',updateclient),
    path(BASENAME+'client/<int:uid>/lock/',lockclient),
    path(BASENAME+'employer/',get_all_employer),
    path(BASENAME+'employer/<int:uid>/',get_all_employer),
    path(BASENAME+'employer/update/<int:uid>/',put_employer),
    path(BASENAME+'employer/<int:uid>/lock/',lock_employer),
]
