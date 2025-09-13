# Poké Trainer - Fábrica Unipe 25.2

**Poké Trainer** é um projeto web desenvolvido em **Django** para a **Fábrica da Unipe 25.2**, que permite aos usuários criar seus próprios **treinadores Pokémon**, capturar e gerenciar suas coleções de forma completa, tanto via interface web quanto via **API REST**.  

O sistema integra-se com a **PokeAPI**, uma API pública da internet que fornece **dados completos sobre todos os Pokémons**, incluindo nome, tipo, habilidades, estatísticas e imagens oficiais. Assim, cada Pokémon adicionado ao projeto é enriquecido com informações reais da franquia.

---

## Tecnologias Utilizadas

- **Backend:** Python 3 + Django  
- **Banco de Dados:** MySQL
- **Python-Decouple:** Ocultar variáveis importantes  
- **ORM:** Django ORM (com ForeignKey para relacionar treinadores e pokémons)  
- **Frontend:** Templates Django (HTML)  
- **API:** Django REST Framework (DRF)  
- **API Externa:** PokeAPI (https://pokeapi.co)  
- **Ambiente Virtual:** venv
-   

---

## Estrutura do Projeto

- **Apps:**
  - `treinadores` → CRUD completo para criar, atualizar, visualizar e deletar treinadores.
  - `pokemons` → CRUD para adicionar, listar, buscar e remover Pokémons de cada treinador.
- **Relacionamento:** Cada Pokémon está vinculado a um treinador através de **ForeignKey**.
- **Templates:** Interface web para visualização de treinadores e seus Pokémons capturados.
- **API (DRF):** Endpoints que retornam dados dos Pokémons e treinadores em **JSON**, permitindo integração com outras aplicações.

---

## Funcionalidades Principais

- **Criar Treinadores:** Cada usuário pode criar seu próprio perfil de treinador Pokémon.
- **Atualizar Treinador:** Depois de criado, é possível atualizar as informações do seu próprio treinador.  
- **Deletar Treinador:** O usuário pode remover seu treinador do sistema, junto com todos os Pokémons associados.  
- **Capturar Pokémons:** É possível adicionar Pokémons à coleção do treinador. Os dados são buscados automaticamente na **PokeAPI**, retornando informações detalhadas como:
  - Nome oficial
  - Tipos (ex.: Fogo, Água, Elétrico)
  - Estatísticas (HP, Ataque, Defesa, etc.)
  - Habilidades
  - Imagens oficiais  
- **Consultar Pokémons:** Visualize detalhes completos de cada Pokémon capturado.  
- **Gerenciar Coleção:** Atualize, remova ou adicione Pokémons à coleção do treinador.  
- **Visualizar Perfil:** Veja todos os Pokémons capturados por cada treinador em uma interface organizada.  
- **API REST:** Através da API, você pode consultar os dados de treinadores e Pokémons em formato JSON, possibilitando integração com outras aplicações ou frontends.  
- **Pesquisa Dinâmica:** Busque informações sobre qualquer Pokémon via PokeAPI, retornando dados confiáveis da franquia.  

---

## Como utilizar projeto (para DEVs)

1. **Clonar o repositório**
```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

2. **Criar e ativar ambiente virtual**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```


3. **Instalar dependências**
```bash
pip install -r requirements.txt
```

4. **Configurar o banco MySQL**

- Crie o banco no MySQL Workbench:
- ⚠️ Certifique-se de que o MySQL Server está rodando antes de criar o banco e rodar as migrações.

```sql
CREATE DATABASE poke_trainer_db CHARACTER SET utf8mb4;
```

- Em vez de colocar a senha diretamente no settings.py, use um arquivo .env para armazenar dados sensíveis:

```env
# .env
DB_NAME=poke_trainer_db
DB_USER=root
DB_PASSWORD=SUA_SENHA
DB_HOST=127.0.0.1
DB_PORT=3306
```

- Configure o settings.py para ler essas variáveis com python-decouple:

```python
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='3306'),
    }
}
```

- Adicione o arquivo .env no .gitignore para não subir sua senha no GitHub:

```bash
# .gitignore
.env
```

5. **Rodar migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Executar o servidor**

```bash
python manage.py runserver
```

- Acesse no navegador: http://127.0.0.1:8000
