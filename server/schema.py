import graphene
import graphql_jwt

# import chatbot.schema as chatbot
import users.schema as users
import black_mage.schema as black_mage

queries = (
    graphene.ObjectType,
    # chatbot.Query,
    users.Query,
    black_mage.Query,
)

mutations = (
    graphene.ObjectType,
    # chatbot.Mutation,
    users.Mutation,
    black_mage.Mutation,
)

class Query(*queries):
    pass


class Mutation(*mutations):
    log_in = graphql_jwt.ObtainJSONWebToken.Field()
    validate_user_token = graphql_jwt.Verify.Field()
    refresh_user_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
