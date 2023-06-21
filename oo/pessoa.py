# Vamos estudar as classes as classes sempre começam com letra maiúscula
# e se hover mais palavras juntas, essas dever também começãr da mesma forma

class Pessoa:
    def __init__(self, nome = None, idade = 41):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Fernandes')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Edimar'
    print(p.nome)
    print(p.idade)


