class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, outro_personagem):
        print(f"{self.nome} ataca {outro_personagem.nome}!")
        dano = max(0, self.ataque - outro_personagem.defesa)
        outro_personagem.sofrer_dano(dano)

    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

personagem1 = Personagem("Guerreiro", 100, 20, 5)
personagem2 = Personagem("Mago", 80, 15, 3)

personagem1.atacar(personagem2)
personagem2.atacar(personagem1)
