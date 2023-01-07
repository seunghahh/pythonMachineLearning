import numpy

speed = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]

x1 = numpy.std(speed)
x2 = numpy.var(speed)
y1 = numpy.std(speed2)
y2 = numpy.var(speed2)
print("%.2f" %x1)
print("%.2f" %x2)
print("%.2f" %y1)
print("%.2f" %y2)