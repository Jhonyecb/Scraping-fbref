#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- carregar dados ---
df = pd.read_csv("jogadores.csv")
df['Percentil'] = pd.to_numeric(df['Percentil'], errors='coerce')
pivot = df.pivot_table(index='Jogador', columns='Estatística', values='Percentil', aggfunc='first')

# --- jogadores ---
jogador1 = "Kaio Jorge"
jogador2 = "Yuri Alberto"

s1 = pivot.loc[jogador1]
s2 = pivot.loc[jogador2]
common = s1.index[s1.notna() & s2.notna()]
v1 = s1[common].astype(float).values
v2 = s2[common].astype(float).values
labels = list(common)

# similaridade (Mean Absolute Difference)
v1_norm = v1 / 100
v2_norm = v2 / 100
diff_media = np.mean(np.abs(v1_norm - v2_norm))
similarity_pct = float((1 - diff_media) * 100)

# GRÁFICO DE BARRAS
x = np.arange(len(labels))  # posições das barras
largura = 0.4               # largura das barras

fig, ax = plt.subplots(figsize=(14, 7))

# barras lado a lado
bars1 = ax.bar(x - largura/2, v1, largura, label=jogador1, color="#FF8C00", edgecolor='k')
bars2 = ax.bar(x + largura/2, v2, largura, label=jogador2, color="#1E90FF", edgecolor='k')

# valores acima das barras
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'{int(height)}', ha='center', va='bottom', fontsize=9)

for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'{int(height)}', ha='center', va='bottom', fontsize=9)

# legendas eixo X
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=9)

# título
ax.set_title(f"{jogador1} vs {jogador2}\nSemelhança: {similarity_pct:.1f}%", fontsize=14, pad=15)

# eixos e legenda
ax.set_ylabel("Percentil")
ax.set_ylim(0, 110)
ax.legend(loc='lower right', bbox_to_anchor=(1, 1), ncol=1)
plt.tight_layout()
plt.show()

#%%
