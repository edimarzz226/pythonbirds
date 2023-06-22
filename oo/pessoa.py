# Vamos estudar as classes as classes sempre começam com letra maiúscula
# e se hover mais palavras juntas, essas dever também começãr da mesma forma

class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    Isabella = Pessoa(nome= 'Isabella')
    Edimar = Pessoa(Isabella, nome ='Edimar')
    print(Pessoa.cumprimentar(Edimar))
    print(id(Edimar))
    print(Edimar.cumprimentar())
    print(Edimar.nome)
    print(Edimar.idade)
    for filho in Edimar.filhos:
        print(filho.nome)


