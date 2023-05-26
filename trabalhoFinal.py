#nome:gabriel rodrigues peron | rgm:30509793
#nome:daniel vitor da silva | rgm:29880301




class Disciplina:
    def __init__(self, nome, codigo, frequencia, nota):
        self.nome = nome
        self.codigo = codigo
        self.frequencia = frequencia
        self.nota = nota
        self.proximo = None


class Aluno:
    def __init__(self, rgm, nome, endereco, curso):
        self.rgm = rgm
        self.nome = nome
        self.endereco = endereco
        self.curso = curso
        self.disciplinas = None

    def adicionar_disciplina(self, nome, codigo, frequencia, nota):
        nova_disciplina = Disciplina(nome, codigo, frequencia, nota)
        if self.disciplinas is None:
            self.disciplinas = nova_disciplina
        else:
            disciplina_atual = self.disciplinas
            while disciplina_atual.proximo:
                disciplina_atual = disciplina_atual.proximo
            disciplina_atual.proximo = nova_disciplina

    def remover_disciplina(self, codigo_disciplina):
        if self.disciplinas:
            if self.disciplinas.codigo == codigo_disciplina:
                self.disciplinas = self.disciplinas.proximo
                print('Disciplina removida com sucesso.')
                return

            disciplina_atual = self.disciplinas
            disciplina_anterior = None
            while disciplina_atual:
                if disciplina_atual.codigo == codigo_disciplina:
                    disciplina_anterior.proximo = disciplina_atual.proximo
                    print('Disciplina removida com sucesso.')
                    return
                disciplina_anterior = disciplina_atual
                disciplina_atual = disciplina_atual.proximo

        print('A disciplina não está associada a este aluno.')

    def alterar_disciplina(self, codigo_disciplina):
        if self.disciplinas:
            disciplina_atual = self.disciplinas
            while disciplina_atual:
                if disciplina_atual.codigo == codigo_disciplina:
                    print(f'Disciplina: {disciplina_atual.nome}')
                    print(f'Código: {disciplina_atual.codigo}')
                    print(f'Frequência: {disciplina_atual.frequencia}')
                    print(f'Nota: {disciplina_atual.nota}')

                    num_alteracao = input('Digite o número do que deseja alterar: ')

                    if num_alteracao == '1':
                        novo_nome = input('Digite o novo nome da disciplina: ')
                        disciplina_atual.nome = novo_nome
                        print('Nome da disciplina alterado com sucesso.')
                    elif num_alteracao == '2':
                        novo_codigo = input('Digite o novo código da disciplina: ')
                        disciplina_atual.codigo = novo_codigo
                        print('Código da disciplina alterado com sucesso.')
                    elif num_alteracao == '3':
                        nova_frequencia = input('Digite a nova frequência da disciplina: ')
                        disciplina_atual.frequencia = nova_frequencia
                        print('Frequência da disciplina alterada com sucesso.')
                    elif num_alteracao == '4':
                        nova_nota = input('Digite a nova nota da disciplina: ')
                        disciplina_atual.nota = nova_nota
                        print('Nota da disciplina alterada com sucesso.')
                    else:
                        print('Opção inválida.')
                    break
                disciplina_atual = disciplina_atual.proximo
        else:
            print('O aluno não está cadastrado em nenhuma disciplina.')

    def adicionar_aluno(self):
        rgm = input('Digite o RGM do aluno: ')
        nome = input('Digite o nome completo do aluno: ')
        endereco = input('Digite o endereço do aluno: ')
        curso = input('Digite o curso do aluno: ')

        aluno = Aluno(rgm, nome, endereco, curso)

        while True:
            participa_disciplina = input('O aluno participa de alguma disciplina? (S/N): ')
            if participa_disciplina.upper() == 'S':
                nome_disciplina = input('Digite o nome da disciplina: ')
                codigo_disciplina = input('Digite o código da disciplina: ')
                frequencia_disciplina = input('Digite a frequência de participação do aluno na disciplina: ')
                nota_disciplina = input('Digite a nota da disciplina: ')
                aluno.adicionar_disciplina(nome_disciplina, codigo_disciplina, frequencia_disciplina, nota_disciplina)

                mais_disciplinas = input('Deseja adicionar mais uma disciplina? (S/N): ')
                if mais_disciplinas.upper() == 'N':
                    break
            else:
                break

        return aluno


def remover_aluno(alunos):
    rgm_aluno = input('Insira o RGM do aluno que deseja remover: ')
    for aluno in alunos:
        if aluno.rgm == rgm_aluno:
            if aluno.disciplinas:
                opcao = input('O aluno está cadastrado na(s) disciplina(s). Deseja removê-lo das disciplinas para fazer sua remoção? (S/N): ')
                if opcao.upper() == 'S':
                    aluno.disciplinas = None
                    alunos.remove(aluno)
                    print('Aluno removido com sucesso.')
                break
            else:
                alunos.remove(aluno)
                print('Aluno removido com sucesso.')
                break
    else:
        print('Aluno não encontrado.')


def remover_disciplina(alunos):
    rgm_aluno = input('Digite o RGM do aluno: ')
    for aluno in alunos:
        if aluno.rgm == rgm_aluno:
            if aluno.disciplinas:
                disciplina_atual = aluno.disciplinas
                while disciplina_atual:
                    print(f'Disciplina: {disciplina_atual.nome} ({disciplina_atual.codigo})')
                    disciplina_atual = disciplina_atual.proximo

                codigo_disciplina = input('Digite o número da disciplina que deseja remover: ')
                aluno.remover_disciplina(codigo_disciplina)
                break
            else:
                print('O aluno não está cadastrado em nenhuma disciplina.')
                break
    else:
        print('Aluno não encontrado.')


def alterar_disciplina(alunos):
    rgm_aluno = input('Digite o RGM do aluno: ')
    for aluno in alunos:
        if aluno.rgm == rgm_aluno:
            if aluno.disciplinas:
                disciplina_atual = aluno.disciplinas
                while disciplina_atual:
                    print(f'Disciplina: {disciplina_atual.nome} ({disciplina_atual.codigo})')
                    disciplina_atual = disciplina_atual.proximo

                codigo_disciplina = input('Digite o número da disciplina que deseja alterar: ')
                aluno.alterar_disciplina(codigo_disciplina)
                break
            else:
                print('O aluno não está cadastrado em nenhuma disciplina.')
                break
    else:
        print('Aluno não encontrado.')


def visualizar_aluno(alunos):
    rgm_aluno = input('Digite o RGM do aluno: ')
    for aluno in alunos:
        if aluno.rgm == rgm_aluno:
            print(f'RGM: {aluno.rgm}')
            print(f'Nome: {aluno.nome}')
            print(f'Endereço: {aluno.endereco}')
            print(f'Curso: {aluno.curso}')

            disciplina_atual = aluno.disciplinas
            if disciplina_atual:
                print('Disciplinas:')
                while disciplina_atual:
                    print(f'Nome: {disciplina_atual.nome}')
                    print(f'Código: {disciplina_atual.codigo}')
                    print(f'Frequência: {disciplina_atual.frequencia}')
                    print(f'Nota: {disciplina_atual.nota}')

                    if float(disciplina_atual.nota) >=6:
                        print('aprovado')
                    else:
                        print('reprovado')

                    disciplina_atual = disciplina_atual.proximo
            else:
                print('O aluno não está cadastrado em nenhuma disciplina.')
            break
    else:
        print('Aluno não encontrado.')


def listar_alunos(alunos):
    if alunos:
        print('Lista de Alunos:')
        for aluno in alunos:
            print(f'RGM: {aluno.rgm} - Nome: {aluno.nome}')
    else:
        print('Não há alunos cadastrados.')


def main():
    alunos = []

    while True:
        print('------ Menu ------')
        print('1 - Adicionar aluno')
        print('2 - Remover aluno')
        print('3 - Remover disciplina de um aluno')
        print('4 - Alterar disciplina de um aluno')
        print('5 - Visualizar informações de um aluno')
        print('6 - Listar todos os alunos')
        print('0 - Sair')

        opcao = input('Digite o número da opção desejada: ')

        if opcao == '1':
            rgm = input('Digite o RGM do aluno: ')
            nome = input('Digite o nome completo do aluno: ')
            endereco = input('Digite o endereço do aluno: ')
            curso = input('Digite o curso do aluno: ')

            aluno = Aluno(rgm, nome, endereco, curso)
            alunos.append(aluno)
            print('Aluno adicionado com sucesso.')

            while True:
                participa_disciplina = input('O aluno participa de alguma disciplina? (S/N): ')
                if participa_disciplina.upper() == 'S':
                    nome_disciplina = input('Digite o nome da disciplina: ')
                    codigo_disciplina = input('Digite o código da disciplina: ')
                    frequencia_disciplina = input('Digite a frequência de participação do aluno na disciplina: ')
                    nota_disciplina = input('Digite a nota da disciplina: ')
                    aluno.adicionar_disciplina(nome_disciplina, codigo_disciplina, frequencia_disciplina, nota_disciplina)

                    mais_disciplinas = input('Deseja adicionar mais uma disciplina? (S/N): ')
                    if mais_disciplinas.upper() == 'N':
                        break
                else:
                    break
        elif opcao == '2':
            remover_aluno(alunos)
        elif opcao == '3':
            remover_disciplina(alunos)
        elif opcao == '4':
            alterar_disciplina(alunos)
        elif opcao == '5':
            visualizar_aluno(alunos)
        elif opcao == '6':
            listar_alunos(alunos)
        elif opcao == '0':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Digite novamente.')


if __name__ == '__main__':
    main()

            #aluno.adicionar_aluno()