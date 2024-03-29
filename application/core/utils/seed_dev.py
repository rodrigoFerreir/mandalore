import os
import logging
from accounts.models import User
from app.models import *


logger = logging.getLogger(__name__)


class SeedDevInitial():
    def __init__(self) -> None:
        self.USERNAME_ADMIN = os.getenv('USER_ADMIN_EMAIL')
        self.USERNAME_EMAIL = os.getenv('USER_ADMIN_USERNAME')
        self.USERNAME_PASSWORD = os.getenv('USER_ADMIN_PASSWORD')

    def create_super_users(self):
        User.objects.create_superuser(
            username=self.USERNAME_ADMIN,
            email=self.USERNAME_EMAIL,
            password=self.USERNAME_PASSWORD
        )

    def create_normal_users(self):
        User.objects.create(username="teste_user", email="teste_user@teste.com", password='teste12340')

    def create_entity_categories(self):
        try:
            EntityCategory.objects.create(name="EMPRESA")
            EntityCategory.objects.create(name="CLIENTE")
            EntityCategory.objects.create(name="USUARIO")
            EntityCategory.objects.create(name="FORNECEDOR")
        except:
            logger.info("Categorias de entidades já foram cadastradas")

    def execute(self):
        logger.info('INICIANDO CARGA DE DADOS')
        try:
            self.create_super_users()
            self.create_normal_users()
        except:
            logger.info("Usuarios já foram criados")
        
        self.create_entity_categories()
        logger.info("CARGA DE DADOS FINALIZADA")
