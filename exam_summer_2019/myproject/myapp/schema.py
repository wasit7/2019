import graphene

from graphene import Node, Connection, ConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from myapp.models import Customer


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        filter_fields = ['firstname']
        interfaces = (Node, )

class CustomerQuery(object):
    all_customer = DjangoFilterConnectionField(CustomerType)

    def resolve_all_customer(self, info, **kwargs):
        return Customer.objects.all()

class Query(CustomerQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)