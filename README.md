# Semana 10 — E-mail com Flask no PythonAnywhere

Aplicação desenvolvida como continuação da Semana 09, utilizando **Flask**, **Flask-SQLAlchemy**, **SQLite** e a **Web API do SendGrid**.

A organização do envio de e-mail segue o padrão trabalhado na Aula 070: função `send_email(to, subject, template, **kwargs)`, template HTML separado e configurações de e-mail obtidas por variáveis de ambiente.

## Funcionalidades

- Associação do usuário a `Administrator`, `Moderator` ou `User`.
- Persistência em banco SQLite.
- Listagem de usuários e respectivas funções.
- Listagem de usuários agrupados por função.
- Contador de usuários.
- Contador de funções.
- Envio de e-mail a cada novo cadastro.
- Destinatários:
  - `flaskaulasweb@zohomail.com`
  - `p.taissa@aluno.ifsp.edu.br`
- Corpo do e-mail contendo:
  - Prontuário `PT3038084`;
  - Nome do aluno `Taissa Pieri`;
  - usuário cadastrado;
  - função escolhida.

## Estrutura de e-mail da Aula 070

O projeto utiliza:

```python
send_email(to, subject, template, **kwargs)
```

O corpo HTML fica em:

```text
templates/mail/new_user.html
```

As configurações são lidas de:

```text
API_URL
API_KEY
API_FROM
FLASKY_ADMIN
```

O arquivo `.env` real **não deve ser enviado ao GitHub**.

## 1. Configurar o SendGrid

1. Crie ou acesse uma conta no SendGrid.
2. Em **Settings > Sender Authentication**, verifique um remetente (*Single Sender Verification*) ou um domínio.
3. Crie uma API Key com permissão para envio de e-mail.
4. Guarde a chave. Não publique a chave no GitHub.

## 2. Instalar as dependências

No PythonAnywhere, dentro do ambiente virtual:

```bash
pip install -r requirements.txt
```

Além de Flask e SQLAlchemy, o projeto utiliza `requests` para a chamada HTTP da API e `python-dotenv` para carregar o arquivo `.env`.

## 3. Criar o arquivo `.env` no PythonAnywhere

O repositório possui apenas `.env.example`. No PythonAnywhere, copie-o:

```bash
cp .env.example .env
```

Depois edite `.env` e mantenha este formato:

```bash
export FLASKY_ADMIN=flaskaulasweb@zohomail.com
export API_URL=https://api.sendgrid.com/v3/mail/send
export API_KEY=SUA_CHAVE_DA_API_SENDGRID
export API_FROM=SEU_REMETENTE_VERIFICADO_NO_SENDGRID
```

`API_KEY` e `API_FROM` devem ser substituídos pelos seus dados reais do SendGrid.

## 4. Configurar o WSGI do PythonAnywhere

No arquivo WSGI real da aplicação (`/var/www/SEU_USUARIO_pythonanywhere_com_wsgi.py`), use:

```python
import sys

project_home = "/home/SEU_USUARIO/SEU_REPOSITORIO"

if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
```

As credenciais não precisam ser colocadas no WSGI porque `app.py` carrega o `.env` com `python-dotenv`.

Depois, salve e clique em **Reload** na aba Web.

## 5. Fluxo do cadastro

Quando o formulário recebe um novo usuário:

1. valida o nome e a função;
2. verifica se o usuário já existe;
3. cria o objeto `User`;
4. chama `send_email(...)` usando `templates/mail/new_user.html`;
5. envia o aviso para o e-mail da atividade e para o e-mail institucional;
6. confirma o cadastro no banco se o SendGrid aceitar o envio.

## Segurança

O `.gitignore` impede o envio de `.env`, banco SQLite, ambientes virtuais e caches para o GitHub.

**Nunca publique `API_KEY` no GitHub, no `app.py` ou no README.**
