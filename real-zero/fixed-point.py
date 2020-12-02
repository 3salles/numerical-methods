import math

def diff_phi_x (x):
  h =  10**(-10)
  diff_phi_x = (phi_x(x + h) - phi_x(x))/h 
  return diff_phi_x

def fixed_point(function):
  x0 = float(input('Digite a aproximaçao inicial: '))
  e1 = float(input('Digita a precisão 1: '))
  e2 = float(input('Digita a precisão 2: '))

  max_iteration = int(input('Número máximo de iterações: '))
  iteration = 1

  root = phi_x(x0) # First iteration

  if (abs(diff_phi_x(x0)) > 1):
    print('A sequência irá divergir.')
  else:
    while (iteration <= max_iteration):
      iteration += 1
      x0 = root # Thi is the current k iteration
      root =  phi_x(x0)  # Calculate the new k+1 iteration

      # Stopping Criteria
      if ((abs(root - x0) < e2) or (abs(function(root)) < e1)):
        print(10*'-+-')
        print(f'Valor da raiz: {round(root, 4)}\nTotal de iterações: {iteration}')
        break
      elif(iteration > max_iteration):
        print(10*'-+-')
        print(f'O método falhou após {max_iteration} iterações.')
        break

# Define Functions here

# function = lambda x: x**3 - x - 1
# phi_x = lambda x: math.pow(x+1, 1/3) #x0 = 1 e1=e2=0.001

# function =  lambda x: x**2 + x - 6
# phi_x = lambda x: math.pow(-x + 6, 1/2) # x0 = 1.5 e1 = -3 e e2 =2

function = lambda x: x**3 -9*x + 3
phi_x = lambda x: ((x**3)/9) + (1/3) # x0 = 0.5 e1=e2=0.0005

fixed_point(function)