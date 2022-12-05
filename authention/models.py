from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

class Permission(models.Model):

    METHODE = (
        ('LOCK','lock'),
        ('GET','get'),
        ('PUT','put'),
    )

    name = models.CharField(max_length=300)
    http_method = models.CharField(max_length=10,choices=METHODE, verbose_name='Methode')
    url_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    
    nom = models.CharField(max_length=300)
    permission = models.ManyToManyField(Permission,symmetrical=False,blank=True)

    def __str__(self):
        return self.nom


class UserManager(BaseUserManager):

    def create_user(self,nom,email,password=None,is_active=True,staff=False,admin=False):
        if not email:
            raise ValueError('User must have an email address')
        
        email_g = self.model(email=self.normalize_email(email))
        user = self.model(email=email_g,nom=nom,is_active=is_active,staff=staff,admin=admin)
        user.set_password(password)
        user.save()
        return user
    
    def create_staffuser(self,nom,email,password):
        user = self.create_user(nom,email,password,staff=True)
        return user

    def create_superuser(self,nom,email,password):    
        user = self.create_user(nom,email,password=password,staff=True,admin=True)
        return user

class User(AbstractBaseUser,PermissionsMixin):

    nom = models.CharField(max_length=300)
    prenom = models.CharField(max_length=300)
    email = models.EmailField(max_length=300,unique=True)
    is_active=models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom']

    role = models.ForeignKey(Role,on_delete=models.PROTECT,null=True,blank=True)

    objects=UserManager()

    def __str__(self):
        return str(self.email)
    
    def get_full_name(self):
        return self.nom

    def get_short_name(self):
        return self.nom
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        if self.admin:
            return True
        return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        if self.admin:
            return True
        return False

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
