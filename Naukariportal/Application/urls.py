from django.urls import path,include
from .views import Com,Qe,Re,App,Jo,Sk,Exp
from rest_framework import routers
router=routers.DefaultRouter()
router.register('Com',Com)


router.register('Re',Re)
router.register('Sk',Sk)

router.register('App',App)
router.register('Exp',Exp)
router.register('Qe',Qe)

urlpatterns =[
    path("",include(router.urls))
]
