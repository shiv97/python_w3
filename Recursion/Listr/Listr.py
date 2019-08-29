def to_string(n,base):
   convtString = "0123456789ABCDEF"
   if n < base:
      return convtString[n]
   else:
      return to_string(n//base,base) + convtString[n % base]

print(to_string(2835,16))
