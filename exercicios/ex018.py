from math import radians, cos, sin, tan

ang = float(input('Digite um ângulo (entre 0° e 360°): '))

angR = radians(ang)

s = sin(angR)
c = cos(angR)
t = tan(angR)

print('Seno: {:.2f};\nCosseno: {:.2f};\nTangente: {:.2f}.'.format(s,c,t))