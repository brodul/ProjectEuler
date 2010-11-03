foo = 1
bar = 2
suma = 0
while  foo < 4*10**6:
    if not foo % 2:
        suma += foo
    foo, bar = bar, foo + bar
print suma
