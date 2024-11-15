
import google.generativeai as genai

genai.configure(api_key="") # Sua KEY aqui entre parenteses

model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

def duvidar():
    print("--------------------------------------------------------------------------")
    print("Qual a sua dúvida? ou digite 'sair'")
    while True:
        print("--------------------------------------------------------------------------")
        texto = input("Conversar...ou 'sair': ")
        if texto.lower() == "sair":
            break
        response = chat.send_message(texto)
        print("Personal Treinner: ", response.text, "\n")
    biotipo =  input("Qual seu Biotipo? Ectomorfo/ Mesomorfo/ Endomorfo: ")
    return biotipo

print('--------------------------------------------------------------------------')
print("Bem vindo ao seu Personal Treinner personalizado! Vamos montar seu treino? ")
print("Para isso me responda algumas perguntas, caso tenha duvidas me pergunte(digite 'duvida')")
biotipo =  input("Qual seu Biotipo? Ectomorfo/ Mesomorfo/ Endomorfo: ")

if biotipo == "duvida":
    duvidar()

periodizacao = input("Quantidade de dias por semana? 1/ 3/ 5: ")
objetivo = input("Qual seu objetivo? Ganhar massa muscular/ Perder peso: ")

treino = f""" 
# Contexto
Você é um especialista personal trainer e vai me ajudar a montar um treino ideal,
baseado nas trê variáveis abaixo:
# Área de variáveis
{biotipo} 
{periodizacao}
{objetivo} 
tipo 
# Regras
Regra 1: biotipo
Identificar qual o tipo informado nas variáveis acima tipo corporal vai ser algum dos três tipos:
- Ectomorfo Corpo mais magro, difícil de ganhar massa muscular.
- Mesomorfo Corpo com músculos definidos, fácil de ganhar massa muscular.
- Endomorfo Corpo com mais gordura, fácil de ganhar massa muscular
# Regra 2: periodização
Dependento da quantidade miníma de dias informado na área de variáveis, criar uma das periodizações abaixo:
- 1 dia Treino full body
- 3 dias de treino ABC
- 5 dias de treino ABCDE
# Regra 3: tipo de treino
- Funcional: Exercícios que melhoram a funcionalidade do corpo, usando movimentos naturais do corpo.
- Maquinário: Exercicíos feitos em maquínas, com foco em isolar grupos musculares.
- Peso Livre: Exercícios voltados a peso livre, como haleres e barras, para trabalhar os músculos simultaneamente.
- Cardio: Exercícios voltados para melhorar a resistencia cardiovascular, como corridas, bicicletas, etc.
- HIIT: Exercícios e treinos intervalados de alta instensidade, ótimos para queima de gordura.
# Resultado esperado
Com base nos valores informados na área de variáveis e com as guidelines, crie um treino pessoal que corresponde a combinação desses 4 valores. """

response = chat.send_message(treino)
print("--------------------------------------------------------------------------")
print("Personal Treinner: ", response.text, "\n")
print("Fim do chat")
