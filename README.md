# Calculadora
Esse é um script de calculadora com operações básicas (adição, subtração, divisão e multiplicação) para dois valores, para ser executada em Python. 

## Como executar
1. Clonar o repositório para o seu computador
2. Navegar até o diretório onde o repositório foi salvo no terminal Linux:
   
```bash
   cd home/.../repositório
```
3. Criar e editar o arquivo calculadora.sh com nano:

```bash
   nano calculadora.sh
```
O editor de texto nano abrirá. Então cole o seguinte código no editor:

```bash
  #!/bin/bash
#Script para executar a calculadora Python
python3 calculadora.py
```
4. Para tornar o script executável, altere as permissões:
```bash
   chmod +x calculadora.sh
```
5. Definir permissões de acesso para garantir que apenas o proprietário do arquivo tenha permissão de escrita e outros usuários tenham apenas permissão de leitura:

```bash
   chmod 744 calculadora.sh
```
6. Para executar o script da calculadora Python:
```bash
   ./calculadora.sh
```
Obs: Se o Pyhton 3 não estievr instalado, instale com o comando:
```bash
   sudo apt-get install python3
```
