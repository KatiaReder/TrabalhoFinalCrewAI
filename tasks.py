from crewai import Task

def personagem_data(agent):
    return Task(
        description=f"Buscar dados sobre Luke Skywalker, Tatooine e a Millennium Falcon usando a SWAPI.",
        agent=agent,
        expected_output="Informações dos personagens, naves e planetas.",
        output_file="output/arquivista_jedi.txt",
        verbose=True,
    )
    
def narrador_historia(agent):
    return Task(
        description="Criar uma história épica envolvendo Luke Skywalker, Tatooine e a Millennium Falcon.",
        agent=agent,
        expected_output="Uma narrativa envolvente.",
        output_file="output/narrador_historia.txt",
        verbose=True,
    )
    
def yoda_tradutor(agent):
    return Task(
        description="Traduzir a narrativa gerada para Yoda Speak com a API da Fun Translations.",
        agent=agent,
        expected_output="Arquivo traduzido para o estilo de Yoda.",
        output_file="output/yoda_tradutor.txt",
        verbose=True,
    )
    
def noticias_espaco(agent):
    return Task(
        description="Buscar uma notícia espacial real dos últimos dias e conectar com a temática da história Jedi criada.",
        agent=agent,
        expected_output="Arquivo com a notícia e a correlação sugerida.",
        output_file="output/noticias_espaco.txt",
        verbose=True,
    )