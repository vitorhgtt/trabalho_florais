class SistemaEspecialistaFlorais:
    def __init__(self):
        self.base_conhecimento = {
            'emergencia': 'Rescue Remedy (Floral de Emergência)',
            'medo': 'Mimulus',
            'ansiedade': 'Aspen',
            'estresse': 'Elm',
            'desespero': 'Sweet Chestnut',
            'indecisao': 'Scleranthus',
            'culpa': 'Pine',
            'depressao': 'Mustard',
            'isolamento': 'Water Violet',
            'ciumes': 'Holly',
            'cansaco_mental': 'Olive',
            'falta_confianca': 'Larch'
        }

    def obter_recomendacao(self, sintomas):
        sintomas = sintomas.lower().split(',')
        for sintoma in sintomas:
            sintoma = sintoma.strip()
            if sintoma in self.base_conhecimento:
                return self.base_conhecimento[sintoma]
        return None

    def executar(self):
        print("\n\nBem-vindo ao Sistema Especialista para Recomendação de Florais de Bach!")
        print("Por favor, descreva os sintomas ou situação do paciente separados por vírgula.")
        print("Exemplo: ansiedade, estresse, medo\n")

        while True:
            entrada = input("\nDigite os sintomas (ou 'sair' para encerrar): ")
            
            if entrada.lower() == 'sair':
                print("\nObrigado por utilizar o sistema!")
                break

            recomendacao = self.obter_recomendacao(entrada)

            if recomendacao:
                print(f"\nRecomendação de Floral: {recomendacao}")
            else:
                print("\nNenhum floral específico encontrado para esses sintomas. Recomendação geral: Rescue Remedy")

if __name__ == "__main__":
    sistema = SistemaEspecialistaFlorais()
    sistema.executar()