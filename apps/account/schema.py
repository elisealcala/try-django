import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from account.models import Account

class AccountNode(DjangoObjectType):
    class Meta:
        model = Account

class AccountQuery(ObjectType):
    accounts = graphene.List(AccountNode)
    account = graphene.Field(AccountNode, id=graphene.Int())

    def resolve_account(self, info, **kwargs):
        account = None
        if kwargs.get('id') is not None:
            try:
                return Account.objects.get(id=kwargs.get('id'))
            except Account.DoesNotExist:
                return account
        return account

    def resolve_accounts(self, info, **kwargs):
        return Account.objects.all()