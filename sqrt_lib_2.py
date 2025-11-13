import cmath
varnum=eval(input('Enter the number to find the square root:'))
varnum_sqrt=cmath.sqrt(varnum)
print('The square root of {0} is {1:0.2f}/+{2:0.2f}j'.format(varnum,varnum_sqrt.real,varnum_sqrt.imag))
