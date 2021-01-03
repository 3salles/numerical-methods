'''
This code was created to the University Subject Numerical Calculus at UFMA

Developed by Beatriz Salles

Atention: Remove quotation marks one by one in each example before using an example.
'''
import math
from prettytable import PrettyTable # This is just a lib to print the results in a table.



def diff_phi_x (x):
  h =  10**(-10)
  diff_phi_x = (phi_x(x + h) - phi_x(x))/h 
  return diff_phi_x

def fixed_point(function):
  a = float(input('Digite início do intervalo: '))
  b = float(input("Digite o final do intervalo: "))
  x0 = float(input('Digite a aproximaçao inicial: '))
  e1 = float(input('Digite a precisão 1: '))
  e2 = float(input('Digite a precisão 2: '))


  max_iteration = int(input('Número máximo de iterações: '))
  iteration = 0

  fa = function(a)
  fb = function(b)

  root = phi_x(x0) # First iteration
  
  if( fa*fb > 0):
    print(10*'-+-')
    print(f'Não existe raiz no intervalo [{a}, {b}]')
  else:
    
    if (abs(diff_phi_x(x0)) > 1):
      print(15*'-+-')
      print('A sequência irá divergir.')
    else:
      table = PrettyTable()
      table.field_names = ['Iteração', 'x', 'f(x)']
      table.add_row(['0', x0, round(function(x0),6)])
      

      while (iteration <= max_iteration):
        iteration += 1
        x0 = root # This is the current k iteration
        root =  phi_x(x0)  # Calculate the new k+1 iteration

        
        # Stopping Criteria
        if (iteration > max_iteration):
          print(15*'-+-')
          print(f'O método falhou após {iteration} iterações.')
          break
        
        else:
          table.add_row([iteration, round(x0, 6), round(function(x0),6)])
          
          if ((abs(root - x0) < e2) or (abs(function(root)) < e1)):
            print(table)
            print(f'Valor da raiz: {round(root, 6)}\nTotal de iterações: {iteration}')
            break
          


# Define Functions here

# Equations to Example 1

function = lambda x: -math.exp(x) + x + 2
phi_x = lambda x: math.exp(x) - 2


# Equations to Example 2

'''
function = lambda x: math.cos(x) - math.sqrt(x)
phi_x = lambda x: math.pow(math.cos(x), 2)
''' 

# Euqations to Example 3
'''
function = lambda x: x**2 - x -2 
phi_x = lambda x: x**2 - 2
'''

fixed_point(function)