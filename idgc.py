import re

class IDGC:
    def Brazil_CPF_Validator(self, cpf: str) -> bool:
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)

        # Verifica se o CPF tem 11 dígitos
        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF deve conter 11 dígitos numéricos!")
            return False

        # Verifica se todos os dígitos são iguais (CPFs inválidos como "11111111111")
        if cpf == cpf[0] * 11:
            print("CPF inválido: todos os números são iguais!")
            return False

        # Cálculo do primeiro dígito verificador
        pesoTotalD1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (pesoTotalD1 % 11)
        if digito1 >= 10:
            digito1 = 0

        # Cálculo do segundo dígito verificador (inclui o primeiro dígito calculado)
        pesoTotalD2 = sum(int(cpf[i]) * (11 - i) for i in range(9)) + digito1 * 2
        digito2 = 11 - (pesoTotalD2 % 11)
        if digito2 >= 10:
            digito2 = 0

        # Verifica se os dígitos calculados conferem com os do CPF original
        if cpf[-2:] == f"{digito1}{digito2}":
            return True
        else:
            print("CPF inválido: Dígitos verificadores não correspondem!")
            return False

# Testando a validação
jif = IDGC()
cpf = "306.559.490-03"  # CPF com pontuação
if jif.Brazil_CPF_Validator(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
