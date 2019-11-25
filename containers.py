class Tabuleiro2D:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def __contains__(self, coordenadas):
        x, y = coordenadas
        return 0 <= x < self.largura and 0 <= y < self.altura



