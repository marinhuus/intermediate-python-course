import random

def main():
  dice_rolls = int(input('Quantos dados voce gostaria de lancar?'))
  dice_size = int(input('Quantos lados sao os dados?'))
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'Voce deu um {roll}! Falha Critica')
    elif roll == dice_size:
      print(f'Voce deu um {roll}! Sucesso Critico')
    else:
      print(f'Voce rolou um {roll}')
  print(f'Voce lancou um total de {dice_sum}')

if __name__== "__main__":
  main()