#how much peperroni sticks do I need to order for next month?
#facts
#only one size rectangular ex 11 x 11 
#I leave  an edge on all sides 0.5" off each side from above
# pepronis sticks cut into 1/10th inch slices vary in thickness
# pep stick is  1" diameter (constant)
# pizza sold last month
import math

# lengthofpizza
# widthofpizza
# pizzassold
# edge in inches
#askfor lengthofpizza
#askfor width
#ask for thickness
# ask for pizza sold
# ask for edge
#how many slices go width wise? widthwise = (widthofpizza - 2 * edge) divide by / diameter.
#lenghofpizza -  (2 * edge) / peperonidiameter
#slicesofpizza = widthwiselices * lenghtwiseslices
#pepengthneeded = slicesofpizza * thickness * pizzasold
#sticksneeded = peplengthneeded / pep length


pepperonidiameter = 1.0
#pepperonilength = 10.0

#ask for:
#length of pizza
#width of pizza
#thickness
#pizzasold
#foredge
#length of pizza

lengthofpizza = float( input( "what is the length of the pizza (in.)? "))
widthofpizza = float( input("what is the width of the pizza (in.)? "))
thickness = float( input("what is the thickness of the the pepperoni slice (in.)? "))
edge = float( input("what is the edge of each pizza (in.)? "))
pizzasSold = int( input("how many pizzas sold last month? "))
#only one is needed for this lab..
pepperonilength = float(input ("what is the length of the pepperoni stick?"))





#how many slices go width wise
widthwiseslices = (widthofpizza - 2 * edge) / pepperonidiameter
#how many slices to lengthwise
lengthwiseslices = (lengthofpizza - 2 * edge) / pepperonidiameter
slicesonpizza = widthwiseslices * lengthwiseslices
pepperonilengthneeded = slicesonpizza * thickness * pizzasSold
sticksneeded = math.ceil(pepperonilengthneeded / pepperonilength)

print("you need", sticksneeded, "pepperoni sticks")
