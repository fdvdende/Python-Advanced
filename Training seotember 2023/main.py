from militair import Militair, OPCOs, GENDERs

p1 = Militair('LTZ1', 'van der Rijk', 'HTD', OPCOs.CZSK, GENDERs.m)

print(p1)

print(p1.name)

p1.function = 'OpperHTD'
print(p1)

