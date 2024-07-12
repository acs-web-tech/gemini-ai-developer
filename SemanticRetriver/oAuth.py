from google.oauth2 import service_account
from scopes import SEMANTIC_RETRIVER_SCOPE
service_account_file_name = "./secrets/semantic-retriver-service-account.json"
credentials = service_account.Credentials.from_service_account_file(service_account_file_name)
scoped_credentials = credentials.with_scopes(SEMANTIC_RETRIVER_SCOPE)

def init_Oauth():
    import google.ai.generativelanguage as glm
    generative_service_client = glm.GenerativeServiceClient(credentials=scoped_credentials)
    retriever_service_client = glm.RetrieverServiceClient(credentials=scoped_credentials)
    permission_service_client = glm.PermissionServiceClient(credentials=scoped_credentials)
    return [generative_service_client,retriever_service_client,permission_service_client]