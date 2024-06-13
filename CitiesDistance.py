from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radio de la Tierra en kilómetros

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distancia = R * c
    return distancia


class Coordenada:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
    
    def get_coordinates(self):
        return self.latitud, self.longitud   

class Ciudad:
    def __init__(self, nombrePais, nombreCiudad):
        self.nombrePais = nombrePais.capitalize()
        self.nombreCiudad = nombreCiudad.capitalize()
    
    def __str__(self):
        return f"Nombre de la ciudad: {self.nombreCiudad}"    


class ServicioCoordenadas:
    def obtener_coordenadas(self, ciudad):
        pass







class MockServicioCoordenadas(ServicioCoordenadas):
    def obtener_coordenadas(self, ciudad):
        return Coordenada(-12.0464, -77.0428).get_coordinates()  

def calcular_distancia(ciudad1, ciudad2, servicio_coordenadas):
    coords1 = servicio_coordenadas.obtener_coordenadas(ciudad1)
    coords2 = servicio_coordenadas.obtener_coordenadas(ciudad2)

    if not coords1:
        print(f"Fallo al obtener las coordenadas para la ciudad {ciudad1}")
        return None

    if not coords2:
        print(f"Fallo al obtener las coordenadas para la ciudad {ciudad2}")
        return None

    lat1, lng1 = coords1
    lat2, lng2 = coords2

    return haversine(lat1, lng1, lat2, lng2)


def main():
    csv_servicio = CSVServicioCoordenadas('worldcities.csv')
    api_servicio = API_ServicioCoordenadas()
    mock_servicio = MockServicioCoordenadas()

    servicios = {
        'csv': csv_servicio,
        'api': api_servicio,
        'mock': mock_servicio
    }

    nombrePais1 = input("Ingrese el país de la primera ciudad: ").strip()
    nombreCiudad1 = input("Ingrese el nombre de la primera ciudad: ").strip()
    nombrePais2 = input("Ingrese el país de la segunda ciudad: ").strip()
    nombreCiudad2 = input("Ingrese el nombre de la segunda ciudad: ").strip()

    ciudad1 = Ciudad(nombrePais1, nombreCiudad1)
    ciudad2 = Ciudad(nombrePais2, nombreCiudad2)

    metodo = input("Elija el método (csv/api/mock): ").strip().lower()

    if metodo in servicios:
        distancia = calcular_distancia(ciudad1, ciudad2, servicios[metodo])
        if distancia is not None:
            print(f"Distancia ({metodo}): {distancia:.2f} km")
        else:
            print("No se pudieron obtener las coordenadas de una o ambas ciudades.")
    else:
        print("Método no válido. Elija entre 'csv', 'api' o 'mock'.")

if __name__ == "__main__":
    main()
