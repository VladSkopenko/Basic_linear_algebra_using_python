import numpy as np

a = np.array([1, 2, 3, 4, 5, 0 ])
print(a.min())
print(a.max())
print(a.sum())
print(a.prod())
print(a.std())
print(a.all())
print(a.var())
#print(a.median()) # Стандартный пайтон не может
print("-" * 100)
print(np.min(a))
print(np.max(a))
print(np.sum(a))
print(np.prod(a))
print(np.std(a))
print(np.all(a))
print(np.var(a))
print(np.median(a))


