from collections import *
#namedtuple
a = namedtuple('Cars','Sedan, Suv')
b= a('City', 'Xuv700')
c = (['Vento','Scorpio'])
print(b)
#deque
c = [1, 2, 3, 4, 5, 6, 7]
d = deque(c)
d.insert(2,8)
d.append('10')
d.appendleft('12')
print(d)
d.remove(1)
print(d)
print(d.pop())
print(d.popleft())
print(d)
#chainmap
e = {'a':'1,2'}
f = {'b':'4,5'}
cm = (ChainMap(e, f))
print(cm)
#counter
g = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5,6]
h = (1, 2, 3 ,4, 5 ,6, 7, 1 ,2 ,4, 5)
i = Counter(g)
j = Counter(h)
print(i)
print(j)
#defaultdict
k = defaultdict(int)
k[1]= "Albin"
k[2]= "python"
print(k[3])

