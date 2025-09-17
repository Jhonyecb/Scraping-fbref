#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# caminho do arquivo
fp = "jogadores.csv"

# ler e limpar
df = pd.read_csv(fp)
df['Percentil'] = pd.to_numeric(df['Percentil'], errors='coerce')  # garante que seja numérico

# pivot: uma linha por jogador, colunas = Estatística, valores = Percentil
pivot = df.pivot_table(index='Jogador', columns='Estatística', values='Percentil', aggfunc='first')

# jogadores disponíveis (confira a grafia exata)
print("Jogadores disponíveis:", list(pivot.index))

# escolha os dois jogadores
jogador1 = "Facundo Colidio"
jogador2 = "Luciano Rodriguez"

if jogador1 not in pivot.index or jogador2 not in pivot.index:
    raise ValueError("Um dos jogadores não está no arquivo. Verifique a grafia.")

# pegar séries e considerar apenas estatísticas em comum (não-nulas nos dois)
s1 = pivot.loc[jogador1]
s2 = pivot.loc[jogador2]
common = s1.index[s1.notna() & s2.notna()]
v1 = s1[common].astype(float).values
v2 = s2[common].astype(float).values
labels = list(common)

# similaridade: cosseno => % (0..100)
dot = np.dot(v1, v2)
norms = np.linalg.norm(v1) * np.linalg.norm(v2)
similarity_pct = float(dot / norms * 100) if norms != 0 else 0.0

# preparar dados para radar
N = len(labels)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]
v1_plot = np.concatenate([v1, [v1[0]]])
v2_plot = np.concatenate([v2, [v2[0]]])

# plot radar
fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)

# linhas e preenchimento (cores diferentes para identificar)
ax.plot(angles, v1_plot, linewidth=2, label=jogador1)
ax.fill(angles, v1_plot, alpha=0.25)
ax.plot(angles, v2_plot, linewidth=2, label=jogador2)
ax.fill(angles, v2_plot, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
ax.set_ylim(0, 100)
ax.set_yticks([20,40,60,80,100])
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
ax.set_title(f"Comparação percentil: {jogador1} vs {jogador2}", size=14, pad=20)
ax.text(1.05, -0.15, f"Semelhança (cosseno): {similarity_pct:.1f}%", transform=ax.transAxes,
        fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="w", ec="0.6"))

plt.tight_layout()
plt.show()

# opcional: imprimir a tabela de percentis usados na comparação
table = pd.DataFrame({jogador1: v1, jogador2: v2}, index=labels)
print(table)

# %%
