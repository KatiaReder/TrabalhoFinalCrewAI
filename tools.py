import requests
from crewai.tools import BaseTool
from typing import Optional
import os

class FetchStarWarsDataTool(BaseTool):
    name: str = "Fetch Star Wars Data Tool"
    description: str = "Busca informações fixas de Luke Skywalker na SWAPI."

    def _run(self, _: str = "") -> str:
        try:
            url = "https://swapi.dev/api/people/?search=Luke Skywalker"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["results"]:
                result = data["results"][0]
                return f"Nome: {result['name']}\nAltura: {result['height']}cm\nPlaneta natal: {result['homeworld']}\nFilmes: {result['films']}"
            else:
                return "Personagem não encontrado."
        except Exception as e:
            return f"Erro ao buscar na SWAPI: {e}"
          
class FetchFunTranslationsAPITool(BaseTool):
    name: str = "Fun Translation Tool"
    description: str = "Traduza textos para Yoda Speak usando a API do Fun Translations."

    def _run(self, text: str) -> str:
        try:
            url = "https://api.funtranslations.com/translate/yoda.json"
            payload = {"text": text}
            response = requests.post(url, data=payload)
            response.raise_for_status()
            translated = response.json()
            return translated["contents"]["translated"]
        except Exception as e:
            return f"Erro ao traduzir com Yoda Speak: {e}"
          
class FetchSpaceflightNewsTool(BaseTool):
    name: str = "Spaceflight News Tool"
    description: str = "Busca as últimas notícias espaciais reais."

    def _run(self, query: str = "") -> str:
        try:
            url = "https://api.spaceflightnewsapi.net/v4/articles/"
            params = {
                "limit": 1,
                "ordering": "-published_at"
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if data["results"]:
                article = data["results"][0]
                title = article["title"]
                summary = article["summary"]
                link = article["url"]
                return f"Título: {title}\nResumo: {summary}\nLink: {link}"
            else:
                return "Nenhuma notícia encontrada."
        except Exception as e:
            return f"Erro ao buscar notícias espaciais: {e}"