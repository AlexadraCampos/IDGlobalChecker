class IDGC:
    def Brazil_CPF_Validator(self, cpf: str) -> bool:
        # Remove caracteres não numéricos

        
        # Rertona falso se um dos i for não numérico.
        for i in cpf:
            if i.isnumeric() == False:
                print("DIGITE APENAS NÚMEROS!")
                return False 


        # Verifica se o CPF tem 11 dígitos ou se todos os dígitos são iguais
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - (soma % 11)
        if digito1 >= 10:
            digito1 = 0

        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - (soma % 11)
        if digito2 >= 10:
            digito2 = 0

        # Verifica se os dígitos calculados conferem com os dígitos finais do CPF
        return cpf[-2:] == f"{digito1}{digito2}"


jif = IDGC()
cpf = "306.559.490-03"
retorno = jif.Brazil_CPF_Validator(cpf)

if retorno:
    print("CPF válido")
else:
    print("CPF inválido")
