class Activity1:
    #metodo inicializador de la clase 
    def __init__(self):
        self.editor_name = 'vsc'
        self.lenguage = 'python'
        self.version = 3.0 
    
    def show_info(self):
        print(f'name {self.editor_name}, lenguage {self.lenguage}, version {self.version}')
    
    def poblacion_pais():
        lista_paises = []
        while True:
            try:
                cantidad_paises = int(input('ingrese numero de paises: '))
                for contador in range(1, cantidad_paises+1):
                    nombre_pais = input('ingrese nombre de pais: ')
                    while True:
                        try:
                            poblacion_paises = int(input('ingrese poblacion del pais: '))
                            break
                        except:
                            print('ingrese valor numerico')
                        lista_paises.append((contador, nombre_pais, poblacion_paises))
                break    
            except:
                print('por favor, ingrese un valor numerico')
             
 