# TechVerso — PI-3

Plataforma comunitária desenvolvida como Projeto Integrador (PI-3) para a comunidade acadêmica da UNIVESP. Reúne em um só lugar cursos, vagas de emprego/estágio, networking e recursos úteis para estudantes de tecnologia.

---

## Funcionalidades

- **Autenticação** — cadastro, login/logout, login social com Google e GitHub
- **Cursos** — listagem com filtros, cadastro manual pela comunidade
- **Vagas (V.E.N.)** — Vagas, Estágios e Networking; cadastro manual + busca automática no LinkedIn e Indeed via scraping
- **FAQ** — perguntas frequentes da comunidade
- **Sobre** — informações sobre o projeto
- **Calculadora UNIVESP** — cálculo de nota bimestral

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.12 / Django 5.1 |
| Banco de dados | PostgreSQL |
| Autenticação social | django-allauth |
| Scraping de vagas | python-jobspy |
| Arquivos estáticos | WhiteNoise |
| Frontend | HTML, CSS, JavaScript |
| Formulários | django-widget-tweaks |

---

## Pré-requisitos

- Python 3.12+
- PostgreSQL 15+
- Git

---

## Instalação local

### 1. Clone o repositório

```bash
git clone https://github.com/martiveira/TechVerso-PI-3.git
cd TechVerso-PI-3
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

No PostgreSQL, crie o banco e o usuário:

```sql
CREATE DATABASE techverso;
CREATE USER techverso_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE techverso TO techverso_user;
\c techverso
GRANT ALL ON SCHEMA public TO techverso_user;
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=techverso
DB_USER=techverso_user
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

GOOGLE_CLIENT_ID=seu-google-client-id
GOOGLE_CLIENT_SECRET=seu-google-client-secret

GITHUB_CLIENT_ID=seu-github-client-id
GITHUB_CLIENT_SECRET=seu-github-client-secret
```

### 6. Rode as migrations

```bash
python manage.py migrate
```

### 7. Crie o superusuário

```bash
python manage.py createsuperuser
```

### 8. Inicie o servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

## Configuração do Login Social

### Google

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Crie um projeto → APIs & Services → Credentials → Create OAuth Client ID
3. Tipo: Web Application
4. Authorized redirect URIs: `http://127.0.0.1:8000/accounts/google/login/callback/`
5. Copie o Client ID e Client Secret para o `.env`

### GitHub

1. Acesse [github.com/settings/developers](https://github.com/settings/developers)
2. New OAuth App
3. Authorization callback URL: `http://127.0.0.1:8000/accounts/github/login/callback/`
4. Copie o Client ID e Client Secret para o `.env`

Após isso, acesse o Django Admin (`/admin`) e:
- Em **Sites**: configure `domain = 127.0.0.1:8000`
- Em **Social Applications**: cadastre Google e GitHub com as credenciais

---

## Estrutura do Projeto

```
TechVerso-PI-3/
├── accounts/          # Autenticação e cadastro de usuários
├── base/              # Templates base, navbar, homepage
├── cursos/            # App de cursos com listagem e cadastro
├── vagas/             # App de vagas com scraping externo
├── faq/               # Perguntas frequentes
├── sobre/             # Sobre o projeto
├── techverso/         # Configurações principais (settings, urls, wsgi)
├── templates/         # Templates globais
├── static/            # Arquivos estáticos
├── media/             # Uploads de mídia
├── requirements.txt
├── .env               # Variáveis de ambiente (não versionar)
└── manage.py
```

---

## Apps

### `accounts`
Gerencia registro, login, logout e integração com Google/GitHub via django-allauth.

### `cursos`
Lista cursos cadastrados pela comunidade com filtros por tipo (gratuito/pago) e certificado. Qualquer usuário pode cadastrar um curso.

### `vagas`
Exibe vagas manuais e busca automaticamente no **LinkedIn** e **Indeed** usando `python-jobspy`. A busca ao vivo é acionada quando o usuário pesquisa por um cargo.

### `faq`
Perguntas e respostas frequentes da comunidade.

---

## Deploy (Railway)

### Pré-requisitos

```bash
pip install gunicorn whitenoise dj-database-url
pip freeze > requirements.txt
```

Crie o `Procfile` na raiz:
```
web: gunicorn techverso.wsgi --log-file -
```

Crie o `runtime.txt`:
```
python-3.12.0
```

### Passos

1. Suba o código no GitHub
2. Acesse [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Adicione um serviço **PostgreSQL** e um serviço **Redis** (para Celery)
4. Configure as variáveis de ambiente no painel do Railway:

```
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=seu-app.railway.app
DATABASE_URL=<gerado automaticamente pelo Railway>
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GITHUB_CLIENT_ID=...
GITHUB_CLIENT_SECRET=...
```

5. Após o deploy, atualize as URLs de callback no Google Console e GitHub OAuth para o domínio de produção.
6. No Django Admin, atualize o **Site** para o domínio de produção.

---

## Variáveis de Ambiente

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django |
| `DEBUG` | `True` em desenvolvimento, `False` em produção |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por vírgula |
| `DB_NAME` | Nome do banco PostgreSQL |
| `DB_USER` | Usuário do banco |
| `DB_PASSWORD` | Senha do banco |
| `DB_HOST` | Host do banco (padrão: `localhost`) |
| `DB_PORT` | Porta do banco (padrão: `5432`) |
| `DATABASE_URL` | URL completa do banco (usado no Railway) |
| `GOOGLE_CLIENT_ID` | Client ID do OAuth Google |
| `GOOGLE_CLIENT_SECRET` | Client Secret do OAuth Google |
| `GITHUB_CLIENT_ID` | Client ID do OAuth GitHub |
| `GITHUB_CLIENT_SECRET` | Client Secret do OAuth GitHub |

---

## Contribuindo

1. Fork o repositório
2. Crie uma branch: `git checkout -b feature/minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: minha feature'`
4. Push para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos como Projeto Integrador da UNIVESP.
