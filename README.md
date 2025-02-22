# Validador de Identificação (CPF, CNPJ, DNI e CUIL)

Este projeto contém uma classe `IDGC` para validação de documentos de identificação utilizados no Brasil e na Argentina. Ele pode ser usado para verificar a autenticidade de **CPF**, **CNPJ**, **DNI** e **CUIL**, garantindo conformidade com os cálculos dos dígitos verificadores e regras estabelecidas para cada tipo de documento.

## 🚀 Funcionalidades

✅ **Validação de CPF (Brasil):** Verifica se um CPF fornecido é válido aplicando os cálculos dos dígitos verificadores.  
✅ **Validação de CNPJ (Brasil):** Confere a autenticidade de um CNPJ utilizando o algoritmo oficial de validação.  
✅ **Validação de DNI (Argentina):** Garante que um DNI argentino segue o formato correto (7 ou 8 dígitos numéricos).  
✅ **Validação de CUIL (Argentina):** Valida o Código Único de Identificación Laboral (CUIL), conferindo o formato `XX-YYYYYYYY-Z` e a integridade dos dígitos verificadores.  

## 📌 Como Usar

### 🔧 Requisitos
- Python 3.x

### 📥 Instalação
Nenhuma instalação adicional é necessária além do Python padrão.

### 📝 Exemplo de Uso

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

# Validando um DNI
dni = "12345678"
if validador.Argentina_DNI_Validator(dni):
    print("DNI válido")
else:
    print("DNI inválido")

# Validando um CUIL
cuil = "20-12345678-3"
if validador.Argentina_CUIL_Validator(cuil):
    print("CUIL válido")
else:
    print("CUIL inválido")
