import math

def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.sha256(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.sha256(str(newid).encode())
	return newid, hashid.hexdigest()


def calc(kordinatekoa):
	total = len(kordinatekoa)

	totaljeral = 0
	sura = 0 

	for i in   range(total) :
		sura = i + 1
		if sura < total :
			koko1 = kordinatekoa[i].split(",")
			koko2 = kordinatekoa[sura].split(",")

			somax = (float(koko1[0]) * 111.320) * 1000
			somay = (float(koko2[1]) * 111.320 ) * 1000


			soma = somax * somay

			totaljeral = totaljeral + soma
		else : 
		
			koko1 = kordinatekoa[i].split(",")
			koko2 = kordinatekoa[0].split(",")

		
			somax = (float(koko1[0]) * 111.320) * 1000
			somay = (float(koko2[1]) * 111.320 ) * 1000

			soma = somax * somay

			totaljeral = totaljeral + soma

	totaljeral2 = 0
	sura2 = 0 

	for i in  range(total) :
		sura2 = i + 1
		if sura2 < total :
			koko1 = kordinatekoa[i].split(",")
			koko2 = kordinatekoa[sura2].split(",")


			somay = (float(koko1[1]) * 111.320) * 1000
			somax = (float(koko2[0]) * 111.320 ) * 1000


			soma = somay * somax

			totaljeral2 = totaljeral2 + soma
		else : 
			
			koko1 = kordinatekoa[i].split(",")
			koko2 = kordinatekoa[0].split(",")

		
			somay = (float(koko1[1]) * 111.320) * 1000
			somax = (float(koko2[0]) * 111.320 ) * 1000

			soma = somay * somax

			totaljeral2 = totaljeral2 + soma


	if totaljeral < totaljeral2 :
		totaljeral2 = (totaljeral2 - totaljeral) / 2
	else :
		totaljeral2 = (totaljeral - totaljeral2) / 2
	

	km2 = totaljeral2

	hectar = km2 / 10000


	return km2, hectar
	# print("koko : " + str(km2) + "koko : " + str(hectar))