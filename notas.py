# Crie um código python, utilizando match case que analise 
# as notas dos alunos
# 1) Peça ao usuário 4 notas
# 2) Calcule a média 
# 3) classifique a média em:
# 0 a 4 = reprovado
# 5 e 6 = recuperação
# 7 a 10 = aprovado

nota1 = float(input("Digite uma nota:"))
nota2 = float(input("Digite uma nota:"))
nota3 = float(input("Digite uma nota:"))
nota4 = float(input("Digite uma nota:"))

media = (nota1 + nota2 + nota3 + nota4) /4
print(media)

match media:
    case media if media < 5:
        print(f"Você tirou {media:.2f} e reprovou")
    case media if 5 <= media < 7:
        print(f"Você tirou {media:.2f} e está de recuperação")
    case media if 7 <= media <= 10:
        print(f"Você tirou {media:.2f} e passou")
    case _:
        print("Digite um número válido")



    
