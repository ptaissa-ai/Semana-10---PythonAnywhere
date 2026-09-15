"""Modelo do WSGI para o PythonAnywhere.

As credenciais de e-mail NÃO ficam neste arquivo. A aplicação carrega
as variáveis API_URL, API_KEY, API_FROM e FLASKY_ADMIN a partir do .env.
"""

import sys

project_home = "/home/SEU_USUARIO/SEU_REPOSITORIO"

if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
