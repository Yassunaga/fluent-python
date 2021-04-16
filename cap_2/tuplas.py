import os

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s|%s' % passport)

for country, _ in traveler_ids:
    print(country)

latitude, longitude = lax_coordinates
print('%s, %s' % (latitude, longitude))

# Desempacotamento de tuplas:
a, b = 1, 2
b, a = a, b
print(a, b)

# RESULTADO = (QUOCIENTE, RESTO)
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

_, filename = os.path.split('home/yassunaga/.ssh/idrsa.pub')
print(filename)

# CAPTURANDO ITENS EXCEDENTES:
a, b, *rest = range(5)
print(a, b, rest)
print(*range(5))
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(a, body, c, d)


# DESEMPACOTAMENTO DE TUPLAS ANINHADAS
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:30} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:30} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
