# -*- coding: utf-8 -*-
"""Chat bot Sherlock Holmes

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tq8_Y-do2VfQ9Ex2cRepSgkx9cRLybl-
"""

pontuacao = 0
resposta = 0
print("="*40)
print("O INTERROGATÓRIO DE SHERLOCK HOLMES")
print("="*40)
print("\nContexto:")
print("\nVocê é o principal suspeito do roubo da pintura valiosa de Sir Reginald Blackwell")
print("na galeria de arte. Sherlock Holmes está prestes a interrogá-lo.")
print("Você deve engana-lo pois você robou a pintura valiosa.\n")

# Mensagem dramática de entrada
print("\033[1;36m")
print("Sherlock Holmes entra na sala silenciosamente, seus olhos afiados escaneando você.")
print("Ele ajusta seu sobretudo e começa a falar com voz calma, porém penetrante:\n")
print("\033[0m")  # Resetar cor
print("\"Ah, nosso suspeito. Não costumo perder tempo com trivialidades, então vamos direto ao ponto.")
print("Uma pintura valiosa desapareceu exatamente quando você estava na galeria.")
print("Seus olhos piscam rápido demais, suas mãos estão inquietas... interessantíssimo.")
print("Você terá uma chance para explicar sua versão dos fatos. Mas cuidado - ")
print("eu detecto mentiras como você detecta o cheiro de café pela manhã.\"")


print("\n O que você estava fazendo na noite do crime?")
print("\n[1] Estava na galeria admirando as pinturas, sem perceber nada errado", "pontos")
print("[2] Estava em um restaurante próximo, jantando sozinho")
print("[3] Estava na galeria, mas saí antes do crime ocorrer")
resposta = input("\n ")
if resposta == "1":
  pontuacao += 5
elif resposta == "2":
  pontuacao += 3
else:
  pontuacao -= 5

print("\n Hmm, interessante observação...")

print("\nVocê estava sozinho ou acompanhado?")
print("\n[1] Sozinho, gosto de refletir sobre arte sem distrações")
print("[2] Com meu amigo John. Ele me acompanhou")
print("[3] Com um grupo, mas não lembro os nomes")
resposta = input("\n ")
if resposta == "1":
  pontuacao += 5
elif resposta == "2":
  pontuacao += 3
elif resposta == "3":
  pontuacao -= 5
else:
  print("\nOpção inválida. Tente novamente.")

print("\n Continue, isso está ficando revelador...")

print("\nVocê percebeu algo estranho durante sua visita?")
print("\n[1] Não, tudo parecia em ordem")
print("[2] A iluminação estava mais baixa que o normal")
print("[3] A pintura parecia deslocada")
resposta = input("\n ")
if resposta == "1":
  pontuacao += 2
elif resposta == "2":
  pontuacao += 5
elif resposta == "3":
  pontuacao -= 5
else:
  print("\nOpção inválida. Tente novamente.")

print("\nOs fatos são teimosos, mas siga adiante...")

print("\nVocê conhece bem a pintura de Sir Reginald Blackwell?")
print("\n[1] Sim, sou grande admirador das suas obras")
print("[2] Já vi algumas, mas nunca me interessei muito")
print("[3] Não, nunca gostei de suas pinturas")
resposta = input("\n")
if resposta == "1":
    pontuacao += 5
elif resposta == "2":
    pontuacao += 2
elif resposta == "3":
  pontuacao -= 5
else:
  print("\nOpção inválida. Tente novamente.")

print("\nCada detalhe importa, prossiga...")

print("\nVocê pode me descrever a pintura roubada?"),
print("\n[1]Era uma figura mitológica com tons de azul e dourado")
print("[2]Era grande e com tons claros, mas não lembro detalhes")
print("[3]Não me lembro bem... era de uma pessoa, talvez")
resposta = input("\n")
if resposta == "1":
  pontuacao += 5
elif resposta == "2":
  pontuacao += 2
elif resposta == "3":
  pontuacao -= 5
else:
  print("\nOpção inválida. Tente novamente.")

print("\nBasta, Minhas conclusões estão formadas.")

# Verdicto final
print("\n\033[1;36mSherlock Holmes analisa suas respostas, dedos unidos sob o queixo...\033[0m\n")

if pontuacao >= 20:
  print("\"Elementar, meu caro Watson! Suas respostas foram consistentes... por enquanto. Você está livre,\nmas continuarei observando.\"")
elif pontuacao >= 10 and pontuacao < 20:
  print("\"Hmm... algumas contradições perturbadoras. Não está preso ainda,\nmas não saia da cidade.\"")
else:
  print("\"Suas mentiras são óbvias demais até para o Dr. Watson.\nVocê está PRESO pelo roubo!\"")
