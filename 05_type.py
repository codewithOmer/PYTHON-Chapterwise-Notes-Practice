a = 'omer'
t = type(a)  # class <str>
b = 4
t = type(b)  # class <int>
c = 3.567
t = type(c)  # class <float>


d = "7.98"   # It is a floater but it is in [ "" ] so it shows has string.
t = type(d)  # class <str>  [important]
e = float(d) # d is a string but we want it has float then
t = type(e)  # by doing this we get what we want .

print(t)