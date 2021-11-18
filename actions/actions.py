# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionProcurarArtigo(Action):

    def name(self) -> Text:
        return "action_procurar_artigo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        materia = tracker.get_slot('materias')
        #faz a busca na api do william que retorna um JSON
        data = json.load(open('william.json'))
        for artigo in data['artigos']:
            titulo = artigo['title']


        return []
