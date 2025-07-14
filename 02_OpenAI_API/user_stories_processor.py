import json

# Carrega o arquivo correto de User Stories
user_stories = []
with open('C:/Users/chris/OneDrive/Documentos/Asimov_Academy/AI_Agents/02_OpenAI_API/requisitos_userstory_bdd_100.json', encoding="utf8") as f:
    user_stories = json.load(f)

print(f"Carregadas {len(user_stories)} User Stories")

# Cria arquivo JSONL com User Stories formatadas
with open('C:/Users/chris/OneDrive/Documentos/Asimov_Academy/AI_Agents/02_OpenAI_API/user_stories.jsonl','w', encoding='utf-8') as f:
    for entrada in user_stories:
        # Constrói o conteúdo no formato User Story + BDD
        resposta_formatada = (
            f"User Story:\n"
            f"Eu como {entrada['Eu como']},\n"
            f"Quero {entrada['Quero']},\n"
            f"Para {entrada['Para']}.\n\n"
            f"Cenário 1: {entrada['Cenário 1']}\n"
            f"Dado que {entrada['Dado que']},\n"
            f"Quando {entrada['Quando']},\n"
            f"Então {entrada['Então']},\n"
            f"E {entrada['E']}.\n\n"
            f"Cenário 2: {entrada['Cenário 2']}\n"
            f"Dado que {entrada['Dado que']},\n"
            f"Quando {entrada['Quando']},\n"
            f"Então {entrada['Então']}."
        )

        entrada_jsonl = {
            'messages': [
                {'role': 'user', 'content': f"Como implementar a funcionalidade: {entrada['User Story']}?"},
                {'role': 'assistant', 'content': resposta_formatada}
            ]
        }

        json.dump(entrada_jsonl, f, ensure_ascii=False)
        f.write('\n')

print(f"Arquivo user_stories.jsonl criado com {len(user_stories)} User Stories!") 