import math, sys;

def exemplo1(bar):
    uma_tupla=(   1,2, 3,'a'  );
    uma_variavel={'lista':[math.pi, 100,200,300,9876543210,'Esta é um string longa que vai longe.'],
    'mais':{'interior':'Esta linha de lógica deveria ser quebrada inteiramente.',uma_tupla:[1,
    20,300,40000,500000000,60000000000000000]}}
    #Comentários devem ter um espaço depois da tralha.
    if bar:
        bar += 1;  bar = bar * bar; return bar
    else:
        some_string = """
                           Indentação em strings multilinha não deve ser tocada.
    Comente código de fato deve ser reindentado.
    """
        return (sys.path, some_string)
