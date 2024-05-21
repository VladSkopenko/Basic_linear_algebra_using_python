import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20])
plt.show()
