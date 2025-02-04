# Validador de CPF e CNPJ

Este projeto contém uma classe `IDGC` para validação de CPF e CNPJ no Brasil. Ele pode ser utilizado para verificar se um CPF ou CNPJ fornecido é válido, aplicando as regras matemáticas necessárias para garantir sua autenticidade.

## Funcionalidades
- **Validação de CPF:** Verifica se um CPF fornecido é válido com base nos dígitos verificadores.
- **Validação de CNPJ:** Confere se um CNPJ fornecido é legítimo utilizando os cálculos corretos dos dígitos verificadores.

## Como Usar

### Requisitos
- Python 3.x

### Instalação
Nenhuma instalação de pacotes adicionais é necessária além do Python padrão.

### Exemplo de Uso

```python
from validator import IDGC

# Criando uma instância da classe IDGC
validador = IDGC()

# Validando um CPF
cpf = "306.559.490-03"
if validador.Brazil_CPF_Validator(cpf):
    print("CPF válido")
else:
    print("CPF inválido")

# Validando um CNPJ
cnpj = "11.222.333/0001-81"
if validador.Brazil_CNPJ_Validator(cnpj):
    print("CNPJ válido")
else:
    print("CNPJ inválido")
