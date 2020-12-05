from ibm_watson import CompareComplyV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('85b7a821-fdff-4dfa-b066-57bcc6f74f0f')
compare_comply = CompareComplyV1(
    version='2018-10-15',
    authenticator=authenticator
)

compare_comply.set_service_url('https://api.us-south.compare-comply.watson.cloud.ibm.com')
