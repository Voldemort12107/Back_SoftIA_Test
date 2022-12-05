from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from authention.models import User,Role,Permission
from authention.serializers import UserResSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request ,*args, **kwargs):
        return super().post(request)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateclient(request,uid=None):
    p = Permission.objects.get(http_method='PUT',url_name='clients')
    if p in request.user.role.permission.all():
        try:
            r = Role.objects.get(nom='client')
            u = User.objects.get(id=uid,role=r.id)
            u.nom = request.POST['nom']
            u.prenom = request.POST['prenom']
            u.email = request.POST['email']
            u.save()
            return JsonResponse({'message':'Update'},status=200)
        except User.DoesNotExist:
            return JsonResponse({'message':'NOT FOUND',"code":404},status=404)
    return JsonResponse({'message':'Unauthorize',"code":401},status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_client(request,uid=None):
    if request.method=='GET' :
        p = Permission.objects.get(http_method='GET',url_name='clients')
        if p in request.user.role.permission.all():
            r = Role.objects.get(nom='client')
            data = []
            try:
                if uid==None:
                    u = User.objects.filter(role=r.id)
                    for a in u:
                        data.append({'id':a.id,'nom':a.nom,'prenom':a.prenom,'email':a.email,'is_active':a.is_active})
                else:
                    u = User.objects.get(id=uid,role=r.id)
                    data.append({'id':u.id,'nom':u.nom,'prenom':u.prenom,'email':u.email})
                return JsonResponse({"client":data})
            except User.DoesNotExist:
                return JsonResponse({'message':'NOT FOUND',"code":404},status=404)

        return JsonResponse({'message':'Unauthorize',"code":401},status=401)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lockclient(request,uid=None):
    p = Permission.objects.get(http_method='LOCK',url_name='clients')
    if p in request.user.role.permission.all():
        try:
            r = Role.objects.get(nom='client')
            u = User.objects.get(id=uid,role=r.id)
            u.is_active = not u.is_active
            u.save()
            return JsonResponse({'message':'lock'},status=200)
        except User.DoesNotExist:
            return JsonResponse({'message':'NOT FOUND',"code":404},status=404)
    return JsonResponse({'message':'Unauthorize',"code":401},status=401)

        


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_employer(request,uid=None):
    p = Permission.objects.get(http_method='GET',url_name='employer')
    if p in request.user.role.permission.all():
        r = Role.objects.get(nom='employer')
        data=[]
        if uid==None:
            u = User.objects.filter(role=r.id)
            for a in u:
                data.append({'id':a.id,'nom':a.nom,'prenom':a.prenom,'email':a.email,'is_active':a.is_active})
        else:
            u = User.objects.get(id=uid,role=r.id)
            data.append({'id':u.id,'nom':u.nom,'prenom':u.prenom,'email':u.email})
        
        return JsonResponse({"employer":data})

    return JsonResponse({'message':'Unauthorize',"code":401},status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def put_employer(request,uid=None):
    p = Permission.objects.get(http_method='PUT',url_name='employer')
    if p in request.user.role.permission.all():
        try:
            r = Role.objects.get(nom='employer')
            u = User.objects.get(id=uid,role=r.id)
            u.nom = request.POST['nom']
            u.prenom = request.POST['prenom']
            u.email = request.POST['email']
            u.save()
            return JsonResponse({'message':'Update'},status=200)
        except User.DoesNotExist:
            return JsonResponse({'message':'NOT FOUND',"code":404},status=404)
    return JsonResponse({'message':'Unauthorize',"code":401},status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lock_employer(request,uid=None):
    p = Permission.objects.get(http_method='LOCK',url_name='employer')
    if p in request.user.role.permission.all():
        try:
            r = Role.objects.get(nom='employer')
            u = User.objects.get(id=uid,role=r.id)
            u.is_active = not u.is_active
            u.save()
            return JsonResponse({'message':'lock'},status=200)
        except User.DoesNotExist:
            return JsonResponse({'message':'NOT FOUND',"code":404},status=404)
    return JsonResponse({'message':'Unauthorize',"code":401},status=401)
        


    
