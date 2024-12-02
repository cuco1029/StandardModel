# Seccion correspondiente a algunas operaciones básicas para conocer la masa total de un sistema de partículas
# la carga y el spin

def total_mass(system):
	sum = 0
	for i in range(0,len(system)):
		sum += system[i].mass
	return sum

def total_charge(system):
	sum = 0
	for i in range(0,len(system)):
		sum += system[i].charge
	return sum

def total_spin(system):
	sum = 0
	for i in range(0,len(system)):
		sum += system[i].spin
	return sum
	