from datetime import datetime as dt

h_inicio = "08:00:00"
h_fim = "12:00:00"

format_h = "%H:%M:%S"

# -- strptime() --> converte a (string) em (datetime).

h_calc = str(dt.strptime(h_fim, format_h) - dt.strptime(h_inicio, format_h))

print(h_calc)

print(type(h_calc))

