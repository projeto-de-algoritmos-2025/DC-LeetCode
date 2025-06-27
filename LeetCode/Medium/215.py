class Solution:
    def findKthLargest(self, nums, k):
        def selecionar(lista, posicao):
            if len(lista) <= 5:
                return sorted(lista)[posicao]

            grupos = [lista[i:i+5] for i in range(0, len(lista), 5)]
            medianas = [sorted(grupo)[len(grupo) // 2] for grupo in grupos]
            pivo = selecionar(medianas, len(medianas) // 2)

            menores = [x for x in lista if x < pivo]
            iguais = [x for x in lista if x == pivo]
            maiores = [x for x in lista if x > pivo]

            if posicao < len(menores):
                return selecionar(menores, posicao)
            elif posicao < len(menores) + len(iguais):
                return pivo
            else:
                return selecionar(maiores, posicao - len(menores) - len(iguais))

        posicao_alvo = len(nums) - k
        return selecionar(nums, posicao_alvo)