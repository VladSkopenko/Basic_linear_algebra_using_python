import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2024-05-21', freq='D', periods=7)
plt.plot(date, [22, 23, 24, 25, 24, 16, 20], color='red', marker='o')
plt.show()
# Графік погоди в Одесі починаючи з 2024-05-21