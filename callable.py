class Contador:

    def __init__(self):
        self._contagem = 0

    def __call__(self, *args, **kwargs):
        self._contagem += 1
        return self._contagem

