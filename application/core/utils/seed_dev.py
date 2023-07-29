import os
import logging
from accounts.models import User
from organization.models import Organization


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

    def create_organization(self):
        Organization.objects.create(name='TESTE')

    def execute(self):
        logger.info('INICIANDO CARGA DE DADOS')
        self.create_super_users()
        self.create_normal_users()
        self.create_organization()
        logger.info("CARGA DE DADOS FINALIZADA")
