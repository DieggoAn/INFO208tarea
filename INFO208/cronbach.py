import pandas as pd
import pingouin as pg

df = pd.DataFrame({'Q1': [1, 2, 2, 3, 2, 2, 3, 3, 2, 3],
                   'Q2': [1, 1, 1, 2, 3, 3, 2, 3, 3, 3],
                   'Q3': [1, 1, 2, 1, 2, 3, 3, 3, 2, 3]})



print(pg.cronbach_alpha(data=df))

print(pg.cronbach_alpha(data=df, ci=.99))