import re
from collections import defaultdict

class SistemaEspecialistaFloraisCompleto:
    def __init__(self):
        self.base_florais = {
            "agrimony": {
                "nome": "Agrimony",
                "grupo": "1 - Para os que sentem Medo",
                "descricao": "Esconder tormentos interiores atrás de uma fachada alegre",
                "indicacoes": ["ansiedade mascarada", "tortura mental oculta", "vícios"],
                "peso": 1.2
            },
            "aspen": {
                "nome": "Aspen",
                "grupo": "1 - Para os que sentem Medo",
                "descricao": "Medos e pressentimentos vagos e desconhecidos",
                "indicacoes": ["medos inexplicáveis", "apreensão", "pesadelos"],
                "peso": 1.1
            },
            "beech": {
                "nome": "Beech",
                "grupo": "2 - Para os que sofrem de Incerteza",
                "descricao": "Intolerância e julgamento excessivo",
                "indicacoes": ["crítica excessiva", "perfeccionismo", "rigidez mental"],
                "peso": 1.0
            },
            "centaury": {
                "nome": "Centaury",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Dificuldade em dizer não e estabelecer limites",
                "indicacoes": ["submissão", "falta de assertividade", "esgotamento"],
                "peso": 1.0
            },
            "cerato": {
                "nome": "Cerato",
                "grupo": "2 - Para os que sofrem de Incerteza",
                "descricao": "Dúvida constante nas próprias decisões",
                "indicacoes": ["indecisão", "busca excessiva por conselhos", "desconfiança na intuição"],
                "peso": 1.1
            },
            "cherry_plum": {
                "nome": "Cherry Plum",
                "grupo": "6 - Desespero",
                "descricao": "Medo de perder o controle mental e emocional",
                "indicacoes": ["medo da perda de controle", "pensamentos obsessivos", "comportamento explosivo"],
                "peso": 1.3
            },
            "chestnut_bud": {
                "nome": "Chestnut Bud",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Dificuldade em aprender com experiências passadas",
                "indicacoes": ["repetição de erros", "dificuldade de aprendizado", "desatenção"],
                "peso": 1.0
            },
            "chicory": {
                "nome": "Chicory",
                "grupo": "7 - Preocupação Excessiva com Outros",
                "descricao": "Amor possessivo e necessidade de controlar",
                "indicacoes": ["ciúmes", "manipulação emocional", "carência excessiva"],
                "peso": 1.1
            },
            "clematis": {
                "nome": "Clematis",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Sonhar acordado e falta de concentração",
                "indicacoes": ["desatenção", "escapismo mental", "desligamento da realidade"],
                "peso": 1.0
            },
            "crab_apple": {
                "nome": "Crab Apple",
                "grupo": "5 - Hipersensibilidade",
                "descricao": "Remédio de limpeza e purificação",
                "indicacoes": ["sentimento de impureza", "obsessão por limpeza", "baixa autoestima física"],
                "peso": 1.0
            },
            "elm": {
                "nome": "Elm",
                "grupo": "6 - Desespero",
                "descricao": "Sobrecarga momentânea de responsabilidades",
                "indicacoes": ["esgotamento temporário", "sentimento de incapacidade", "perfeccionismo"],
                "peso": 1.1
            },
            "gentian": {
                "nome": "Gentian",
                "grupo": "2 - Incerteza",
                "descricao": "Desânimo e pessimismo após contratempos",
                "indicacoes": ["desencorajamento", "ceticismo excessivo", "dúvidas"],
                "peso": 1.0
            },
            "gorse": {
                "nome": "Gorse",
                "grupo": "6 - Desespero",
                "descricao": "Desesperança e sentimento de derrota",
                "indicacoes": ["desespero profundo", "falta de esperança", "resignação"],
                "peso": 1.2
            },
            "heather": {
                "nome": "Heather",
                "grupo": "4 - Solidão",
                "descricao": "Necessidade excessiva de atenção e companhia",
                "indicacoes": ["egocentrismo", "falta de empatia", "tagarelice"],
                "peso": 1.0
            },
            "holly": {
                "nome": "Holly",
                "grupo": "5 - Hipersensibilidade",
                "descricao": "Sentimentos negativos como ciúme e raiva",
                "indicacoes": ["inveja", "desconfiança", "hostilidade"],
                "peso": 1.2
            },
            "honeysuckle": {
                "nome": "Honeysuckle",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Viver no passado e nostalgia excessiva",
                "indicacoes": ["saudades paralisantes", "incapacidade de seguir em frente", "luto prolongado"],
                "peso": 1.0
            },
            "hornbeam": {
                "nome": "Hornbeam",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Cansaço mental e falta de motivação",
                "indicacoes": ["procrastinação", "desânimo matinal", "cansaço mental"],
                "peso": 1.0
            },
            "impatiens": {
                "nome": "Impatiens",
                "grupo": "7 - Preocupação com Outros",
                "descricao": "Impaciência e irritação com lentidão alheia",
                "indicacoes": ["impaciência", "tensão nervosa", "estresse por pressa"],
                "peso": 1.1
            },
            "larch": {
                "nome": "Larch",
                "grupo": "2 - Incerteza",
                "descricao": "Falta de confiança e expectativa de fracasso",
                "indicacoes": ["complexo de inferioridade", "antecipação de fracasso", "auto-desvalorização"],
                "peso": 1.1
            },
            "mimulus": {
                "nome": "Mimulus",
                "grupo": "1 - Medo",
                "descricao": "Medos específicos e conhecidos",
                "indicacoes": ["timidez", "medo do dentista", "ansiedade social"],
                "peso": 1.2
            },
            "mustard": {
                "nome": "Mustard",
                "grupo": "6 - Desespero",
                "descricao": "Tristeza profunda sem causa aparente",
                "indicacoes": ["melancolia", "depressão sazonal", "tristeza súbita"],
                "peso": 1.1
            },
            "oak": {
                "nome": "Oak",
                "grupo": "7 - Preocupação com Outros",
                "descricao": "Excesso de responsabilidade e resistência ao cansaço",
                "indicacoes": ["esgotamento persistente", "workaholic", "teimosia"],
                "peso": 1.0
            },
            "olive": {
                "nome": "Olive",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Esgotamento total físico e mental",
                "indicacoes": ["burnout", "fadiga crônica", "exaustão profunda"],
                "peso": 1.2
            },
            "pine": {
                "nome": "Pine",
                "grupo": "6 - Desespero",
                "descricao": "Culpabilidade excessiva e auto-recriminação",
                "indicacoes": ["sentimento de culpa", "auto-punição", "perfeccionismo moral"],
                "peso": 1.1
            },
            "red_chestnut": {
                "nome": "Red Chestnut",
                "grupo": "7 - Preocupação com Outros",
                "descricao": "Preocupação excessiva com entes queridos",
                "indicacoes": ["medo por outros", "superproteção", "ansiedade parental"],
                "peso": 1.0
            },
            "rock_rose": {
                "nome": "Rock Rose",
                "grupo": "1 - Medo",
                "descricao": "Terror e pânico extremo",
                "indicacoes": ["ataques de pânico", "traumas", "pesadelos aterrorizantes"],
                "peso": 1.3
            },
            "rock_water": {
                "nome": "Rock Water",
                "grupo": "7 - Preocupação com Outros",
                "descricao": "Autodisciplina rígida e repressão",
                "indicacoes": ["perfeccionismo", "rigidez emocional", "negligência das próprias necessidades"],
                "peso": 1.0
            },
            "scleranthus": {
                "nome": "Scleranthus",
                "grupo": "2 - Incerteza",
                "descricao": "Dificuldade em escolher entre alternativas",
                "indicacoes": ["indecisão", "mudanças de humor", "instabilidade emocional"],
                "peso": 1.1
            },
            "star_of_bethlehem": {
                "nome": "Star of Bethlehem",
                "grupo": "6 - Desespero",
                "descricao": "Consequências de choques e traumas",
                "indicacoes": ["traumas não resolvidos", "luto", "experiências chocantes"],
                "peso": 1.2
            },
            "sweet_chestnut": {
                "nome": "Sweet Chestnut",
                "grupo": "6 - Desespero",
                "descricao": "Angústia mental extrema e desespero existencial",
                "indicacoes": ["crise existencial", "sofrimento insuportável", "sentimento de abandono divino"],
                "peso": 1.3
            },
            "vervain": {
                "nome": "Vervain",
                "grupo": "7 - Preocupação com Outros",
                "descricao": "Excesso de entusiasmo e tensão por ideais",
                "indicacoes": ["fanatismo", "hiperatividade mental", "incapacidade de relaxar"],
                "peso": 1.0
            },
            "vine": {
                "nome": "Vine",
                "grupo": "7 - Preocupação com Outros",
                "descricao": "Tendência a dominar e controlar os outros",
                "indicacoes": ["autoritarismo", "manipulação", "ambição excessiva"],
                "peso": 1.0
            },
            "walnut": {
                "nome": "Walnut",
                "grupo": "5 - Hipersensibilidade",
                "descricao": "Proteção durante transições e mudanças",
                "indicacoes": ["mudanças de vida", "influências externas", "adaptação"],
                "peso": 1.1
            },
            "water_violet": {
                "nome": "Water Violet",
                "grupo": "4 - Solidão",
                "descricao": "Isolamento por orgulho e reserva excessiva",
                "indicacoes": ["isolamento emocional", "dificuldade de intimidade", "orgulho excessivo"],
                "peso": 1.0
            },
            "white_chestnut": {
                "nome": "White Chestnut",
                "grupo": "5 - Hipersensibilidade",
                "descricao": "Pensamentos circulares e indesejados",
                "indicacoes": ["mente tagarela", "insônia por pensamentos repetitivos", "diálogo mental excessivo"],
                "peso": 1.2
            },
            "wild_oat": {
                "nome": "Wild Oat",
                "grupo": "2 - Incerteza",
                "descricao": "Incerteza sobre direção e propósito de vida",
                "indicacoes": ["indecisão vocacional", "sentimento de estagnação", "crise de meia-idade"],
                "peso": 1.0
            },
            "wild_rose": {
                "nome": "Wild Rose",
                "grupo": "3 - Desinteresse pelo Presente",
                "descricao": "Resignação e apatia existencial",
                "indicacoes": ["desinteresse pela vida", "fatalismo", "falta de motivação"],
                "peso": 1.1
            },
            "willow": {
                "nome": "Willow",
                "grupo": "6 - Desespero",
                "descricao": "Ressentimento e vitimização crônica",
                "indicacoes": ["amargura", "sentimento de injustiça", "auto-piedade"],
                "peso": 1.0
            },
            "rescue": {
                "nome": "Rescue Remedy",
                "grupo": "Combinação de Emergência",
                "descricao": "Primeiros socorros para crises emocionais",
                "indicacoes": ["emergências", "choques emocionais", "estresse agudo"],
                "peso": 0.9
            }
        }
        
        self._preprocessar_base()

    def _preprocessar_base(self):
        """Cria índice invertido para busca rápida"""
        self.indice_invertido = defaultdict(list)
        for floral, dados in self.base_florais.items():
            texto = ' '.join([
                dados['descricao'],
                ' '.join(dados.get('indicacoes', [])),
                dados['grupo']
            ]).lower()
            palavras = set(re.findall(r'\w+', texto))
            for palavra in palavras:
                self.indice_invertido[palavra].append(floral)

    def _calcular_pontuacao(self, sintomas):
        """Calcula a relevância de cada floral"""
        scores = defaultdict(float)
        palavras = re.findall(r'\w+', sintomas.lower())
        
        for palavra in palavras:
            if palavra in self.indice_invertido:
                for floral in self.indice_invertido[palavra]:
                    peso = self.base_florais[floral].get('peso', 1.0)
                    scores[floral] += peso
        
        return scores

    def _obter_recomendacoes(self, sintomas):
        """Retorna recomendações ordenadas por pontuação"""
        scores = self._calcular_pontuacao(sintomas)
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    def executar(self):
        """Interface de interação com o usuário"""
        print("\nSistema Especialista em Florais de Bach - 38 Remédios")
        print("Descreva seus sintomas emocionais ou físicos:")
        print("Exemplo: 'Estou me sentindo sobrecarregado e com medo de falhar'")
        print("Digite 'sair' para encerrar\n")

        while True:
            entrada = input("\nDescreva sua situação: ")
            if entrada.lower() == 'sair':
                print("\nSempre consulte um profissional para orientação detalhada.")
                break

            recomendacoes = self._obter_recomendacoes(entrada)
            
            if not recomendacoes:
                print("\nRecomendação Geral: Rescue Remedy")
                print("Indicação: Situações de crise e emergência emocional")
                continue

            print("\nTop Recomendações:")
            for i, (floral_id, score) in enumerate(recomendacoes[:3], 1):
                floral = self.base_florais[floral_id]
                print(f"\n{i}. {floral['nome']} ({score:.1f} pts)")
                print(f"   Grupo: {floral['grupo']}")
                print(f"   Descrição: {floral['descricao']}")
                if 'indicacoes' in floral:
                    print(f"   Indicações: {', '.join(floral['indicacoes'])}")

            print("\nDica: Florais podem ser combinados para tratamentos mais específicos")

if __name__ == "__main__":
    sistema = SistemaEspecialistaFloraisCompleto()
    sistema.executar()