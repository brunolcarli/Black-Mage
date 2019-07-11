import graphene

# models
from users.schema import UserType
from civil_cultural.models import Portal, Topic

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


class TopicType(graphene.ObjectType):
    '''
        Defines a GraphQl Topic object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    description = graphene.String()
    scope = graphene.String()
    creation_datetime = graphene.DateTime()
    # TODO - add Tags
    # TODO - add Articles


class TopicConnection(graphene.relay.Connection):
    class Meta:
        node = TopicType


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
        return Portal.objects.all()

    topics = graphene.relay.ConnectionField(
        TopicConnection
    )

    # @access_required
    def resolve_topics(self, info, **kwargs):
        '''
            Returns all topics from civil cultural.
        '''
        return Topic.objects.all()


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
