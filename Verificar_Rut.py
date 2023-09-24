
from itertools import cycle

def Verificar_rut(rut):
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]

	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
	
	if str(res) == dv:
		return True
	elif dv.upper()=="K" and res==10:
		return True
	else:
		return False
