matching = {
    'QUANDO?': ["em", "hoje", "já", "afinal", "logo",
                "agora", "amanhã", "amiúde", "antes",
                "ontem", "tarde", "breve", "cedo",
                "depois", "nunca", "sempre", "doravante",
                "primeiramente", "imediatamente",
                "antigamente", "provisoriamente",
                "sucessivamente", "constantemente",
                "na"],

    'ONDE?': ["debaixo", "em cima", "ali", "aqui",
              "além", "abaixo", "aquém", "lá",
              "fora", "dentro", "acima", "diante",
              "atrás", "longe", "perto", "defronte",
              "algures", "cá", "nenhures", "adentro",
              "aquém", "externamente", "em"],

    'A QUÊ?': ["a"],

    'O QUÊ?': ["é"],

    'DE QUÊ?': ["de","da"],

    'DE QUEM?': ["de"],

    'QUEM?': ["um","uma","o","os","a","as"],

    'DATA?': ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"],

    'A ONDE?': ["à"],

    'PARA O QUÊ?': ["para"],

    'DO QUÊ?': ["do"],

    'E QUEM?': ["e"],

    'COMO QUEM?': ["como"],

    'POR ONDE?': ["pela","pelo"],

    'OU O QUÊ?': ["ou"],

    'PELO QUÊ?': ["pela","pelo","por"],

    'EM QUÊ?': ["nas","nos","na","no"],

    'EM O QUÊ?': ["e"],

    "MAS O QUÊ?": ["mas"],

    "QUER O QUÊ?":  ["quer"],
}

def main():
    buildQuestion("Haus Laboratories: vem aí a marca de maquilhagem de Lady Gaga")


def buildQuestion(phrase):
    list_words = list(map(lambda x: x, phrase.split()))
    #print(list_words)
    results = {}
    counter = 0
    for i in list_words:
        if i in [x for v in matching.values() for x in v] or i in matching.values():
            for key, value in matching.items():
                for v in value:
                    question = ""
                    if v == i:
                        #print(key)
                        for u in range(counter):
                            question = question + " " + list_words[u]
                        question = question + " " + key.lower()
                        if question not in results.keys():
                            answer = ""
                            for q in range(len(list_words)-counter):
                                answer = answer + " " + list_words[q + counter]
                            #results[question] = matching[key][len(matching[key])-1]
                            results[question] = answer
        counter = counter+1
            #print("")

    for r in results.keys():
        print(r + ": " + results[r])

main()