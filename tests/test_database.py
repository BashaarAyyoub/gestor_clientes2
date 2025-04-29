import unittest
import copy
from gestor import db
from gestor import database as db
from gestor import config
from gestor import helpers
import csv

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'),
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'García')
        ]
        db.Clientes.guardar()

    def test_buscar_cliente(self):
        self.assertIsNotNone(db.Clientes.buscar('15J'))
        self.assertIsNone(db.Clientes.buscar('99X'))

    def test_crear_cliente(self):
        cliente = db.Clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(cliente.dni, '39X')
        self.assertEqual(len(db.Clientes.lista), 4)

    def test_modificar_cliente(self):
        cliente_original = copy.copy(db.Clientes.buscar('28Z'))
        cliente_modificado = db.Clientes.modificar('28Z', 'Mariana', 'Pérez')
        self.assertNotEqual(cliente_original.nombre, cliente_modificado.nombre)

    def test_borrar_cliente(self):
        db.Clientes.borrar('48H')
        self.assertIsNone(db.Clientes.buscar('48H'))

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23223S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('15J', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.modificar('15J', 'Marta', 'Ríos')
        with open(config.DATABASE_PATH, newline="\n") as f:
            reader = csv.reader(f, delimiter=";")
            data = list(reader)
        self.assertIn(['15J', 'Marta', 'Ríos'], data)

if __name__ == "__main__":
    unittest.main()
