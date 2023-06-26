# Vamos estudar as classes as classes sempre começam com letra maiúscula
# e se hover mais palavras juntas, essas dever também começãr da mesma forma

class Pessoa:
    olhos = 2 # Criando fora do sem está dentro do metodo __int__ estamos criando atributo de classe ou default
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
    Edimar.sobrenome = 'Fernandes'
    del Edimar.filhos
    Edimar.olhos = 1 # mudando o valor do atributo no objeto Edimar o id dele altera
    del Edimar.olhos # Aqui estamo deletando o atributo do objeto Edimar
    print(Edimar.__dict__) # vai aparecer um dicionário com os atributos que foram todos definidos acima idade, nome , filhos e o que foi criado dinamicamente sobrenome = Fernandes
    print(Isabella.__dict__) # Aqui diferente do objeto Isabella que não foi criado um atributo chamado sobrenome
    Pessoa.olhos = 3
    print(Pessoa.olhos) # Quantos olhos tem uma pessoa? Aqui estamos perguntando sobre o atributo de classe olhos
    print(Edimar.olhos) # Acessando os atribuos da classe através do objeto "Edimar"
    print(Isabella.olhos)
    print(id(Pessoa.olhos), id(Edimar.olhos), id(Isabella.olhos)) # Buscar o id do atributo = olhos vai imprimir na tela


