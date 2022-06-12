def aumentar(moeda, taxa, formato=False):
    aum = moeda + (moeda*taxa/100)
    #return format(aum)     torna todas as formatações válidas sem escolher se quer ou não formatar
    return aum if formato is False else format(aum)