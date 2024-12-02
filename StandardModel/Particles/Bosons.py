# Seccion correspondiente a los bosones y sus propiedades 
# creados como objetos a traves de la clase particle
class particle:
	def __init__(self,name,
				 type,mass,
				 charge, spin
				):
		self.name = name  # Nombre de la partícula
		self.type = type      # Tipo de partícula
		self.mass = mass     # Masa de la partícula en [GeV/c²]
		self.charge = charge # Carga eléctrica de la partícula [e]
		self.spin = spin
		
	def description(self):
		# Método para describir la partícula
		print("Particula: ", self.name,)
		print("Tipo: ", self.type)
		print("Masa: ", self.mass," GeV/c²")
		print("Carga: ", self.charge," e" )
		print("Spin: ", self.spin)


foton = particle("Fotón","Bosón", "< e-27", 0, 1)

gluon = particle("Gluón","Bosón", 0, 0, 1)

W_plus = particle("Bosón W","Bosón", 80.3692, 1, 1)

W_less = particle("Bosón W","Bosón", 80.3692, -1, 1)

Z = particle("Bosón Z","Bosón", 91.1880, 0, 1)

Higgs = particle("Bosón de Higgs","Bosón", 125.20, 0, 0)