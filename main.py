from interpolacao_vizinho import InterpolacaoVizinho

def main():

    arquivo_matriz = 'matriz.txt'
    interpolador = InterpolacaoVizinho(arquivo_matriz)
    matrizes_reduzidas, matrizes_ampliadas = interpolador.processar_matrizes()
    arquivo_saida = 'matrizes.txt'
    interpolador.salvar_matrizes_em_arquivo(matrizes_reduzidas, matrizes_ampliadas, arquivo_saida)

if __name__ == "__main__":
    main()