# gestor/config.py
import sys

DATABASE_PATH = 'clientes.csv'

# Si ejecutamos pruebas, usar archivo diferente
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'
