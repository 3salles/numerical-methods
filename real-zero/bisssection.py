import math

def calcule_min_iterations(initial_interval, final_interval, precision):
  """
  This function estimates the minimum number of iterations. 
  Returns: number (minimum iterations required)
  """

  estimate = (math.log10(final_interval - initial_interval) - math.log(precision)/math.log10(2))
  result =  int(math.ceil(estimate))
  return result


def bissection(function):
  print(10*'-+-')
  a = float(input('Digite início do intervalo: '))
  b = float(input('Digite final do intervalo: '))
  e = float(input('Digite precisão: '))

  min_itarations = calcule_min_iterations(a, b, e)
  print(f'O mínimo de iterações estimado: {min_itarations} ')

  print(10*'-+-')
  max_iterations = int(input('Número máximo de iterações: '))
  iteration = 1 

  fa = function(a)
  fb = function(b)

  kzao = fa

  # Bolzano's Theorem
  if (fa * fb > 0):
    print('Não há raízes neste intervalo')
  else:
    while (iteration <= max_iterations):
      root = (a + b)/2
      froot = function(root)

      if((froot == 0) or ((b-a) < e)):
        print(f'Valor da raiz: {root}\nTotal de iterações: {iteration} ')
        break
      
      iteration += 1
      # Determine new interval with Bolzano's Theorem
      if (kzao * froot < 0):
        b = root
      else:
        a = root
        kzao = froot
      
      if (iteration > max_iterations):
        print(f'O método falhou após {max_iterations} iterações. ')
        break

f = lambda x: math.exp(x)-x-2 # Define function here

bissection(f)

