class Cancion:
    def __init__(self, id: str, titulo: str, artista: str, duracion: int):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        horas, resto = divmod(self.duracion, 3600)
        minutos, segundos = divmod(resto, 60)
        tiempo = f"{horas}:{minutos:02d}:{segundos:02d}" if horas else f"{minutos}:{segundos:02d}"
        return f"{self.id} {self.titulo} - {self.artista} ({tiempo})"
