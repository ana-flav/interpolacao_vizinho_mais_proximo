import numpy as np

class InterpolacaoVizinho:
    def __init__(self, arquivo_matriz):
        self.matrizes = self.ler_matrizes(arquivo_matriz)

    def ler_matrizes(self, arquivo):
        matrizes = []
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            matrizes_txt = conteudo.strip().split('\n\n')

            for mariz_txt in matrizes_txt:
                linhas = mariz_txt.split('\n')
                matriz = [list(map(int, linha.split())) for linha in linhas]
                matrizes.append(np.array(matriz))
        return matrizes

    def reduzir(self, matriz):
        nova_matriz_reduzida = matriz[::2, ::2]
        return nova_matriz_reduzida

   
    def ampliar(self, matriz):
        linhas, colunas = matriz.shape
        linhas_novas = (linhas * 2) - 1
        colunas_novas = (colunas * 2) - 1
        nova_matriz = np.zeros((linhas_novas, colunas_novas), dtype=matriz.dtype)
        nova_matriz[::2, ::2] = matriz

        for i in range(1, linhas_novas, 2):
            nova_matriz[i] = nova_matriz[i - 1]

        for j in range(1, colunas_novas, 2):
            nova_matriz[:, j] = nova_matriz[:, j - 1]

        return nova_matriz


    def processar_matrizes(self):
        # parte responsavek por chamar os outros metodos da classe para relaizar a interpolação
        
        resultados_reduzidos = []
        resultados_ampliados = []

        for matriz in self.matrizes:
            matriz_reduzida = self.reduzir(matriz)
            matriz_ampliada = self.ampliar(matriz)
            resultados_reduzidos.append(matriz_reduzida)
            resultados_ampliados.append(matriz_ampliada)
        return resultados_reduzidos, resultados_ampliados

    def salvar_matrizes_em_arquivo(self, matrizes_reduzidas, matrizes_ampliadas, arquivo_saida):
    
        with open(arquivo_saida, 'w') as f:
            for i, (matriz_reduzida, matriz_ampliada) in enumerate(zip(matrizes_reduzidas, matrizes_ampliadas)):
               
                matriz_reduzida_str = '\n'.join(' '.join(map(str, linha)) for linha in matriz_reduzida)
                f.write(f"Matriz {i} reduzida:\n")
                f.write(matriz_reduzida_str)
                f.write('\n\n')
                
                matriz_ampliada_str = '\n'.join(' '.join(map(str, linha)) for linha in matriz_ampliada)
                f.write(f"Matriz {i} ampliada:\n")
                f.write(matriz_ampliada_str)
                f.write('\n\n')  

        print(f"Todas as matrizes reduzidas e ampliadas salvas em {arquivo_saida}")
