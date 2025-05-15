from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv
import time

load_dotenv()

arquivista_jedi_agent = create_arquivista_jedi_agent()
narrador_historia_agent = create_narrador_historia_agent()  
yoda_tradutor_agent = create_yoda_tradutor_agent()
analista_noticias_espaco_agent = create_analista_noticias_espaco_agent()

task1 = personagem_data(arquivista_jedi_agent)
task2 = narrador_historia(narrador_historia_agent)
task3 = yoda_tradutor(yoda_tradutor_agent)
task4 = noticias_espaco(analista_noticias_espaco_agent)

crew = Crew(
  agents=[arquivista_jedi_agent, narrador_historia_agent, yoda_tradutor_agent, analista_noticias_espaco_agent],
    tasks=[task1, task2, task3, task4], 
    verbose=True,
)

print("Iniciando a missão Jedi...")
resultado = crew.kickoff()
time.sleep(4)
print("\n=== RESULTADOS ===")
print(resultado)
