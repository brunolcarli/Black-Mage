import graphene

# models
from users.schema import UserType
from civil_cultural.models import Portal, Topic, Article

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
    topics = graphene.ConnectionField('civil_cultural.schema.TopicConnection')
    # TODO - add Topics
    # TODO - add News
    # TODO - add Rules
    # TODO - add Chat
    # TODO - add Users
    # TODO - add Tags

    def resolve_topics(self, info, **kwargs):
        return self.topic_set.all()


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
    portal = graphene.Field(
        PortalType
    )
    # TODO - add Tags
    # TODO - add Articles

    def resolve_portal(self, info, **kwargs):
        return self.topic_portal


class TopicConnection(graphene.relay.Connection):
    class Meta:
        node = TopicType


class ArticleType(graphene.ObjectType):
    '''
        Defines an Article GraphQl object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    title = graphene.String()
    publication_datetime = graphene.DateTime()
    post_author = graphene.Field(
        UserType,
        description='News author.'
    )
    article_authors = graphene.List(
        graphene.String
    )
    abstract = graphene.String()
    body = graphene.String()
    pro_votes = graphene.Int()
    cons_votes = graphene.Int()
    # TODO add questions
    # TODO add tags
    # TODO reports
    # TODO similar suggestions


class ArticleConnection(graphene.relay.Connection):
    class Meta:
        node = ArticleType


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

    articles = graphene.relay.ConnectionField(
        ArticleConnection
    )

    # @access_required
    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()



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


class CreateTopic(graphene.relay.ClientIDMutation):
    '''
        Creates a topic
    '''
    topic = graphene.Field(
        TopicType,
        description='Created topic data response.'
    )

    class Input:
        name = graphene.String(
            required=True,
            description='Topic title.'
        )
        description = graphene.String(
            description='Topic description.'
        )
        scope = graphene.String(
            description='Topic focus and scope.'
        )
        portal = graphene.ID(
            required=True,
            description='Topic portal ID.'
        )

    # @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        name = _input.get('name')
        description = _input.get('description', '')
        scope = _input.get('scope', '')
        portal_id = _input.get('portal')

        _, portal_id = from_global_id(portal_id)

        try:
            portal = Portal.objects.get(id=portal_id)
        except Portal.DoesNotExist:
            raise Exception(
                'Given portal does not exist!'
            )

        try:
            topic = Topic.objects.create(
                name=name,
                description=description,
                scope=scope,
                topic_portal=portal
            )
            topic.save()
            return CreateTopic(topic)

        except Exception as exception:
            raise(exception)


class Mutation:
    create_portal = CreatePortal.Field()
    create_topic = CreateTopic.Field()
