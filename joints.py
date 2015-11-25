#joint index

class Joint:
	length = None
	roation = None

#shoulder:
#pitch:
LSP = Joint()
LSP.length = [0, 0.24551, 0]
LSP.rotation = [0, 1, 0]
#roll:
LSR = Joint()
LSR.length = [0,0,0]
LSR.rotation = [1,0,0]
#yaw:
LSY = Joint()
LSY.length = [0,0,0]
LSY.rotation = [0,0,1]

#elbow: 
LEP = Joint()
LEP.length = [0,0,-0.282575]
LEP.rotation = [0,1,0]

#wrist:
#yaw:
LWY = Joint()
LWY.legnth = [0,0,-0.3127375]
LWY.rotation = [0,0,1]
#roll:
LWR = Joint()
LWR.length = [0,0,0]
LWR.rotation = [1,0,0]

#end effector:
LE = Joint()
LE.length = [0,0,-0.0635]
LE.rotation = [0,1,0]
