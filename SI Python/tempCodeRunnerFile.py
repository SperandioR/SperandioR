import matplotlib.pyplot as plt

notas = pd.read_csv("ratings.csv")
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]
notas.nota.plot(kind = 'hist')
plt.show()