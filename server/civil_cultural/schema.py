import graphene

# models
from users.schema import UserType
from civil_cultural.models import Portal

# resolvers

# other stuff
from users.utils import access_required
from graphql_relay import from_global_id


class PortalType(graphene.ObjectType):
    '''
        Defines a GraphQl Portal object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    founding_datetime = graphene.DateTime()
    # TODO - add Topics
    # TODO - add News
    # TODO - add Rules
    # TODO - add Chat
    # TODO - add Users
    # TODO - add Tags


class PortalConnection(graphene.relay.Connection):
    class Meta:
        node = PortalType


class Query(object):
    '''
        Queries for civil_cultural.
    '''
    node = graphene.relay.Node.Field()

    portals = graphene.relay.ConnectionField(
        PortalConnection
    )

    # @access_required
    def resolve_portals(self, info, **kwargs):
        '''
            Returns all portals from civil cultural.
        '''
        # portals = Portal.objects.all()
        # return [portal for portal in portals]
        return Portal.objects.all()
