import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Carregar os dados
def draw_plot():
    # Ler o arquivo
    df = pd.read_csv('epa-sea-level.csv')

    # Criar o gráfico de dispersão
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Ajuste de regressão linear para toda a série histórica
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    ax.plot(years_extended, res_full.intercept + res_full.slope * years_extended, 'r', label='Linha de ajuste completo')

    # Ajuste de regressão linear para dados a partir de 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    ax.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g', label='Linha de ajuste recente')

    # Configurações dos rótulos e título
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Configurar os ticks do eixo x
    ax.set_xticks([i for i in range(1850, 2100, 25)])

    # Adicionar legenda
    ax.legend()

    # Salvar a figura
    fig.savefig('sea_level_plot.png')
    return ax
