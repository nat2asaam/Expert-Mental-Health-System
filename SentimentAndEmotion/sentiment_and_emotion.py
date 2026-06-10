import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
def analyze_text(text):
    authenticator = IAMAuthenticator('tOBDn7-vZcZ4ufX4M7_IQDYREMN9QriSCCLVjmKCS57x')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator)

    natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/7ad57d0c-8559-4b2a-87c2-d2225d8b5fc4')

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                    limit=2))).get_result()

    return json.dumps(response, indent=2)