import unittest
from CitiesDistance import Ciudad, Coordenada, CSVServicioCoordenadas, API_ServicioCoordenadas, MockServicioCoordenadas, calcular_distancia

class TestCiudad(unittest.TestCase):
    def test_ciudad_initialization(self):
        ciudad = Ciudad("Peru", "Lima")
        self.assertEqual(ciudad.nombrePais, "Peru")
        self.assertEqual(ciudad.nombreCiudad, "Lima")

class TestCoordenada(unittest.TestCase):
    def test_get_coordinates(self):
        coord = Coordenada(-12.0464, -77.0428)
        self.assertEqual(coord.get_coordinates(), (-12.0464, -77.0428))

class TestServicios(unittest.TestCase):
    def test_csv_servicio(self):
        servicio = CSVServicioCoordenadas('worldcities.csv')
        coords = servicio.obtener_coordenadas(Ciudad("Peru", "Lima"))
        self.assertIsNotNone(coords)

    def test_api_servicio(self):
        servicio = API_ServicioCoordenadas()
        coords = servicio.obtener_coordenadas(Ciudad("Peru", "Lima"))
        self.assertIsNotNone(coords)

    def test_mock_servicio(self):
        servicio = MockServicioCoordenadas()
        coords = servicio.obtener_coordenadas(Ciudad("Peru", "Lima"))
        self.assertEqual(coords, (-12.0464, -77.0428))

class TestCalcularDistancia(unittest.TestCase):
    def test_calcular_distancia(self):
        mock_servicio = MockServicioCoordenadas()
        ciudad1 = Ciudad("Peru", "Lima")
        ciudad2 = Ciudad("Chile", "Santiago")
        distancia = calcular_distancia(ciudad1, ciudad2, mock_servicio)
        self.assertIsNotNone(distancia)

class TestCasosExtremos(unittest.TestCase):
    def test_ciudad_no_existe(self):
        mock_servicio = MockServicioCoordenadas()
        ciudad1 = Ciudad("Ficticio", "CiudadFalsa")
        ciudad2 = Ciudad("Chile", "Santiago")
        distancia = calcular_distancia(ciudad1, ciudad2, mock_servicio)
        self.assertIsNone(distancia, "La distancia debe ser None si una de las ciudades no existe.")

    def test_ciudades_iguales(self):
        mock_servicio = MockServicioCoordenadas()
        ciudad1 = Ciudad("Peru", "Lima")
        ciudad2 = Ciudad("Peru", "Lima")
        distancia = calcular_distancia(ciudad1, ciudad2, mock_servicio)
        self.assertEqual(distancia, 0, "La distancia debe ser 0 si las dos ciudades son iguales.")

if __name__ == '__main__':
    unittest.main()
