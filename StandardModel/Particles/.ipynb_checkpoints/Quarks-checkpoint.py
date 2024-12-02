# Seccion correspondiente a los leptones y sus propiedades 
# creados como objetos a traves de la clase particle
class particle:
	def __init__(self, name,
				 type, mass,
				 charge, spin,
				 straflavor, enchflavor,
				 bottflavor,topflavor
				):
		
		self.name = name  # Nombre de la partícula
		self.type = type      # Tipo de partícula
		self.mass = mass     # Masa de la partícula en [MeV/c²]
		self.charge = charge # Carga eléctrica de la partícula [e]
		self.spin = spin
		self.straflavor = straflavor
		self.enchflavor = enchflavor
		self.bottflavor = bottflavor
		self.topflavor = topflavor
		
	def description(self):
		# Método para describir la partícula
		print("Particula: ", self.name,)
		print("Tipo: ", self.type)
		print("Masa: ", self.mass,"MeV/c²")
		print("Carga: ", self.charge," e" )
		print("Spin: ", self.spin)
		print("Sabor Extraño: ", self.straflavor)
		print("Sabor Encantado: ", self.enchflavor)
		print("Sabor inferior: ", self.bottflavor)
		print("Sabor superior: ", self.topflavor)
		
		
quark_up = particle("Quark Up","Quark",2.16,2/3,1/2,0,0,0,0)

quark_down = particle("Quark Down","Quark",4.70,-1/3,1/2,0,0,0,0)

quark_strange = particle("Quark Strange","Quark",93.5,-1/3,0,-1,0,0,0)

quark_charm = particle("Quark Charm","Quark",1273.0,2/3,0,0,1,0,0)

quark_bottom =particle("Quark Bottom","Quark",4183.0,-1/3,0,0,0,-1,0)

quark_top = particle("Quark Top","Quark",172.57,2/3,0,0,0,0,1)
