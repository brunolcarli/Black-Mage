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


class CreatePortal(graphene.relay.ClientIDMutation):
    '''
        Creates a portal
    '''
    portal = graphene.Field(
        PortalType,
        description='Created portal data response.'
    )

    class Input:
        name = graphene.String(description='Portal title.')

    # @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        name = _input.get('name')

        try:
            portal = Portal.objects.create(
                name=name,
            )
            portal.save()

            return CreatePortal(portal)

        except Exception as exception:
            raise(exception)


class Mutation:
    create_portal = CreatePortal.Field()
