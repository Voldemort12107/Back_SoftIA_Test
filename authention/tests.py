from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from authention.models import User,Role,Permission

class TestUser(APITestCase):

    def test_list(self):
        r = Role.objects.create(nom='client')
        user = User.objects.create_user(nom='Testeur',email='Testeur@gmail.com',password='L@fouine12')
        user.role = r
        user.email = 'Testeur@gmail.com'
        user.save()
        reponse = self.client.post(reverse_lazy('token_obtain_pair'),data={'email':'Testeur@gmail.com','password':'L@fouine12'})
        self.assertEqual(reponse.status_code,200)

    def test_getClient(self):
        p = Permission.objects.create(name='consulter employer',http_method='GET',url_name='client')
        r = Role.objects.create(nom='employer')
        r.permission.set([p])
        r.save()
        user = User.objects.create_user(nom='Testeur',email='Testeur@gmail.com',password='L@fouine12')
        user.role = r
        user.email = 'Testeur@gmail.com'
        user.save()
        res= self.client.post(reverse_lazy('token_obtain_pair'),data={'email':'Testeur@gmail.com','password':'L@fouine12'})

        getuser = User.objects.create_user(nom='Client',email='client@gmail.com',password='L@fouine12')
        getuser.role = Role.objects.create(nom='client')
        getuser.email = 'Client@gmail.com'
        getuser.save()
        reponse = self.client.get("/api/client/"+str(getuser.id)+'/',headers={'Authorization':'Bearer '+res.json()['access']})
        excepted = [
            {
                'id':getuser.id,
                'nom':getuser.nom,
                'prenom':getuser.prenom,
                'email':getuser.email,
            }
        ]
        self.assertEqual(reponse.json()['client'],excepted)
    
    