from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authention.models import User

class UserResSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=['id','nom','prenom','email','is_active']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
        Le serializer de l'obtention de token avec les informations
        sur l'utilisateur authentifié
    """

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        data = {}
        per = {}
        for i in user.role.permission.all():
            if i.url_name not in per.keys():
                per[i.url_name]={i.http_method:True}
            else:
                per[i.url_name][i.http_method]=True
        data['nom']=user.nom 
        data['prenom']=user.prenom
        data['email']=user.email 
        data['role']={'nom':user.role.nom,'permission':per}
        token['user']=data

        return token
