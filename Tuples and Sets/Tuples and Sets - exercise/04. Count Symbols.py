symbols = input()
symbols_set = {}

for symbol in symbols:
    if symbol not in symbols_set.keys():
        symbols_set[symbol] = 0
    symbols_set[symbol] += 1

[print(f"{key}: {value} time/s") for key, value in sorted(symbols_set.items())]













