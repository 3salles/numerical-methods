import math

def false_position(function):
  a = float(input('Digite início do intervalo: '))
  b = float(input('Digite final do intervalo: '))
  e = float(input('Digite precisão: '))

  max_iteration = int(input('Número máximo de iterações: '))

  iteration = 1

  fa = function(a)
  fb = function(b)

  # Bolzano's Theorem
  if (fa * fb > 0):
    print('Não há raízes neste intervalo')
  else:
    while (iteration <= max_iteration):
      root = ((a * fb) - (b * fa))/(fb - fa)
      froot =  function(root)

      if ((abs(b-a) < e) or (abs(froot) < e)):
        print(10*'-+-')
        print(f'Valor da raiz: {round(root, 4)}\nTotal de iterações: {iteration} ')
        break
      iteration += 1

      if (fa * froot < 0): # Check new interval
        b = root
      else:
        a = root
      
      if (iteration > max_iteration):
        print(10*'-+-')
        print(f'O método falhou após {max_iteration} iterações.')
        break

function = lambda x: x**3 + 5 * x**2 - 5 * x - 12 # Define function here

false_position(function) 
