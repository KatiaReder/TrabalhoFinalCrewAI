# 🛰️ Analista de Notícias do Espaço

Este é um projeto em Python que utiliza a biblioteca [CrewAI](https://github.com/joaomdmoura/crewAI) para simular uma equipe de agentes inteligentes que exploram, narram, traduzem e analisam histórias do universo Star Wars, relacionando-as com eventos reais da exploração espacial.

---

## 🚀 Objetivo

O projeto visa:

- Integrar dados fictícios (Star Wars) e reais (notícias espaciais).
- Traduzir textos para o estilo de fala do Yoda.
- Criar narrativas épicas baseadas em dados coletados.
- Relacionar ficção com a realidade de forma educativa e divertida.

---

## 🧠 Tecnologias e Ferramentas

- **Python 3.12.9**
- **[CrewAI](https://github.com/joaomdmoura/crewAI)** – Coordenação de agentes LLM com tarefas especializadas.
- **[LiteLLM](https://github.com/BerriAI/litellm)** – Abstração de LLMs como LLaMA-3 via Groq.

---

## 🔌 APIs Utilizadas

| API                       | Uso                                                                 |
|---------------------------|----------------------------------------------------------------------|
| [SWAPI](https://swapi.dev/) | Dados do universo de Star Wars: personagens, naves, planetas etc.     |
| [Fun Translations](https://funtranslations.com/) | Tradução de frases para Yoda Speak (e outras línguas fictícias) |
| [Spaceflight News](https://spaceflightnewsapi.net/) | Notícias reais sobre exploração espacial                           |

---

## 👨‍🚀 Agentes do Projeto

### 🧾 Arquivista Jedi
- **Função**: Buscar dados detalhados de personagens, naves e planetas de Star Wars (máx. 1000 caracteres).
- **Ferramentas**: SWAPI.
- **Descrição**: Um historiador galáctico com acesso aos arquivos Jedi, mestre em encontrar dados precisos.

---

### 📜 Narrador de História
- **Função**: Criar histórias épicas baseadas nos dados coletados (máx. 1000 caracteres).
- **Ferramentas**: LLM.
- **Descrição**: Treinado pelos Antigos Jedis para transformar dados em lendas.

---

### 🗣️ Tradutor Yoda
- **Função**: Traduzir textos normais para o estilo de fala do Mestre Yoda.
- **Ferramentas**: Fun Translations API.
- **Descrição**: Discípulo de Yoda, responsável por manter viva sua linguagem peculiar.

---

### 🛰️ Analista de Notícias do Espaço
- **Função**: Relacionar eventos de Star Wars com acontecimentos espaciais reais (máx. 500 caracteres, título e resumo em português).
- **Ferramentas**: Spaceflight News API.
- **Descrição**: Analista atento a paralelos entre ficção e realidade.

---

## 📂 Estrutura do Projeto

