import pandas as pd
from random import randint

print pd.DataFrame([(t1, t2, 'Yes' if 6 in {t1, t2} else '') 
              for t1 in range(1, 7)
              for t2 in range(1, 7)],                               
             columns=['Throw 1', 'Throw 2', 'Has 6'])

n = 10000
print(float(sum([1 for s in [{randint(1, 6) 
                        for _ in range(4)} 
                        for _ in range(n)] if 6 in s])) / n)

print(float(sum([1 for s in [{(randint(1, 6), randint(1, 6)) 
                        for _ in range(24)} 
                        for _ in range(n)] if (6, 6) in s])) / n)

