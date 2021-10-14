from string import Template
a = 'Albin K Rajan'
b = 'Pythonista'
c = 'Machine Learning'
d = 'Self Learned Programmer'

#modulo % method
print('The name is %s'% (a))

#f string support
print(f'I am a {b}')

#str.format
print('I love {c}'.format(c = c))

#Template format
t =  Template('I am a $d')
print(t.substitute(d = d))


#template method
