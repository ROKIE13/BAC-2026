def nombre(ini, n):
    if n == 0:
        return ini
    return round(nombre(ini, n-1) * 0.95 + 200)

print(nombre(1000, 20))
    