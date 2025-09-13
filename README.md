# Poké Trainer - Fábrica UniPE 25.2

**Poké Trainer** é um projeto web em **Django** desenvolvido para a **Fábrica da UniPE 25.2**. O sistema permite que usuários criem seus próprios **treinadores**, capturem **Pokémons** e gerenciem suas coleções de forma completa.

O projeto combina **CRUD completo**, integração com **MySQL**, **templates Django** para interface web e uma **API REST** com Django REST Framework para exibir dados em formato JSON.

---

## Tecnologias Utilizadas

- **Backend:** Python 3 + Django  
- **Banco de Dados:** MySQL  
- **ORM:** Django ORM (com ForeignKey para relacionar treinadores e pokémons)  
- **Frontend:** Templates Django (HTML)  
- **API:** Django REST Framework (DRF)  
- **Ambiente Virtual:** venv  

---

## Estrutura do Projeto

- **Apps:**
  - `treinadores` → CRUD completo para criar, atualizar, visualizar e deletar treinadores.
  - `pokemons` → CRUD para adicionar, listar e remover pokémons dos treinadores.
- **Relacionamento:** Cada Pokémon está vinculado a um treinador através de **ForeignKey**.
- **Templates:** Interface web para visualização de treinadores e seus pokémons.
- **API (DRF):** Endpoint para mostrar os dados dos pokémons em JSON.

---

## Funcionalidades

- Criar **Treinadores**.
- Adicionar **Pokémons** aos treinadores.
- Visualizar **perfil de cada treinador** com seus pokémons capturados.
- Atualizar dados dos treinadores.
- Deletar treinadores ou deletar **pokémons individualmente**.
- API que retorna dados dos pokémons em **JSON**.

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

- Configure o settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'poke_trainer_db',
        'USER': 'root',
        'PASSWORD': 'SUA_SENHA',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
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
