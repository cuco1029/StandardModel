# Seccion correspondiente a los leptones y sus propiedades 
# creados como objetos a traves de la clase particle

class particle:
	def __init__(self,name,
				 type, mass,
				 charge,spin,
				 magneticmoment,amagneticmoment,
				 halflife,maasshalflife
				):
		self.name = name  # Nombre de la partícula
		self.type = type      # Tipo de partícula
		self.mass = mass     # Masa de la partícula en [MeV/c²]
		self.charge = charge # Carga eléctrica de la partícula [e]
		self.spin = spin
		self.magneticmoment = magneticmoment
		self.amagneticmoment = amagneticmoment
		self.halflife = halflife
		self.maasshalflife = maasshalflife

		
	def description(self):
		# Método para describir la partícula
		print("Particula: ", self.name,)
		print("Tipo: ", self.type)
		print("Masa: ", self.mass,"MeV/c²")
		print("Carga: ", self.charge," e" )
		print("Spin: ", self.spin)
		print("Momento magnético: ", self.magneticmoment)
		print("Momento magnético anómalo: ", self.amagneticmoment)
		print("Vida media (mayor o igual): ", self.halflife,"s")
		print("Vida másica : ", self.maasshalflife ,"s/eV")

electron = particle("Electrón","Lepton",0.51099895000,-1,1/2,None,1159.65218062e-6,2.08e36,None)

muon = particle("Muón","Lepton",105.6583755,-1,1/2,None,11659205.9e-10,2.1969811e-6,None)

tau = particle("Tau","Lepton",1776.93,-1,1/2,None,"−0.057 a 0.024",290.3e-15,None)

electron_neutrino = particle("Neutrino Electrónico","Lepton","<0.8e-7",0,1/2,"< 0.064e-10",None,None,"> 300")

muon_neutrino = particle("Neutrino Muónico","Lepton","<0.8e-7",0,1/2,"< 0.064e-10",None,None,"> 7e9")

tau_neutrino = particle("Neutrino Tauónico","Lepton","<0.8e-7",0,1/2,"< 0.064e-10",None,None,"> 15.4")
