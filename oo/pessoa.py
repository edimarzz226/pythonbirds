# Vamos estudar as classes as classes sempre começam com letra maiúscula
# e se hover mais palavras juntas, essas dever também começãr da mesma forma

class Pessoa:
    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p= Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
