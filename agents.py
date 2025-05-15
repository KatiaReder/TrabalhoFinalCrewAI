from crewai import Agent
from tools import FetchStarWarsDataTool, FetchFunTranslationsAPITool, FetchSpaceflightNewsTool
from config import get_llm


def create_arquivista_jedi_agent():
    return Agent(
        role= "Arquivista Jedi",
        goal="Obter informações detalhadas de personagens, planetas e naves de Star Wars em no máximo 1000 caracteres",
        backstory="Um historiador galáctico com acesso aos arquivos Jedi, mestre em encontrar dados precisos usando a SWAPI.",
        tools=[FetchStarWarsDataTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
    
def create_narrador_historia_agent():
    return Agent(
        role="Narrador de História",
        goal="Criar histórias baseadas em personagens e locais do universo Star Wars em no máximo 1000 caracteres.",
        backstory="Narrador lendário treinado pelos Antigos Jedis para transformar dados em lendas épicas.",
        verbose=True,
        llm=get_llm(),
    )
    
def create_yoda_tradutor_agent():
    return Agent(
        role="Tradutor Yoda",
        goal="Converter textos normais em Yoda Speak usando Fun Translations API",
        backstory="Discípulo de Yoda, responsável por manter viva a linguagem peculiar dos Jedi.",
        tools=[FetchFunTranslationsAPITool()],
        verbose=True,
        llm=get_llm(),
    )
    
def create_analista_noticias_espaco_agent():
    return Agent(
        role="Analista de Notícias do Espaço",
        goal="Relacionar eventos do universo Star Wars com notícias espaciais reais, em no máximo 500 caracteres. o Título e resumo devem ser em português.",
        backstory="Analista que observa paralelos entre ficção e realidade usando a Spaceflight News API.",
        tools=[FetchSpaceflightNewsTool()],
        verbose=True,
        llm=get_llm(),
    )