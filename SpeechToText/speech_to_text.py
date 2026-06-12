from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from os.path import join, dirname
from ibm_watson.websocket import RecognizeCallback, AudioSource
api_key = 'J4NH_JCeh4DJNjAfBfaVPtyvn02EWXSiSAquLLbHM3BX'
authenticator = IAMAuthenticator(api_key)
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/04e11b95-7933-477b-85df-55f5c6ef070e'
speech_to_text.set_service_url(url)

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

def transcribe_audio(path_to_audio):
    myRecognizeCallback = MyRecognizeCallback()
    with open(join(dirname(__file__), './.', path_to_audio),
                'rb') as audio_file:
        audio_source = AudioSource(audio_file)
        response=speech_to_text.recognize_using_websocket(
            audio=audio_source,
            content_type='audio/mp3',
            recognize_callback=myRecognizeCallback,
            model='en-US_BroadbandModel',
            keywords=['patriotism', 'oppose', 'patriots'],
            keywords_threshold=0.5,
            max_alternatives=3)
    return response
