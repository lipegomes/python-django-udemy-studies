from exchange.moeda import real


def increase(valor, percentage, conversion=False):
    r = float(valor + (valor * (percentage / 100)))

    if conversion:
        return real(r)
    else:
        return r


def reduction(valor, percentage, conversion=False):
    r = float(valor - (valor * (percentage / 100)))

    if conversion:
        return real(r)
    else:
        return r
