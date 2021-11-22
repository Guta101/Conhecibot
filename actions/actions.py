# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import json
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionProcurarArtigo(Action):

    def name(self) -> Text:
        return "action_procurar_artigo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        materia = tracker.get_slot('materias')
        list_artigos = []
        try:
            r = requests.get('linkdowilliam', headers={"most_claps": "true", "searching": materia})
            data = json.load(r.json())
            for artigo in data['artigos']:
                list_artigos.append(artigo)
        except:
            pass
        finally:
            return [SlotSet("artigos", list_artigos)]


class ActionImprimirArtigo(Action):

    def name(self) -> Text:
        return "action_imprimir_artigo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        materia = tracker.get_slot('materias')
        artigos = tracker.get_slot('artigos')
        if artigos:
            dispatcher.utter_message(text=f"Aqui está o que eu achei sobre {materia}: "
                                          f"{(artigos[0])['title']} \n"
                                          f"{(artigos[0])['description']} \n\n"
                                          f" http://blogsite.com/{(artigos[0])['id']}")
        else:
            dispatcher.utter_message(text=f"Desculpe, não encontrei nada sobre {materia} =(")
        return []
