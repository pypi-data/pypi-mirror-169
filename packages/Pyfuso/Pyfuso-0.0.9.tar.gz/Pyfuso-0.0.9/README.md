Pyfuso
======
#### Esse pacote realiza conversões de fusohorario de acordo com a região requerida pelo usuário, disponibilizando o fuso de mais de 150 países e suas respectivas cidades, sendo possível buscar data e hora de todos no formato desejado, e possibilida fazer a subtração de horas entre dois locais para saber a diferença. 


## Instalação:
    pip install Pyfuso

## Uso:

from Pyfuso import pyfuso as pf

### Criar um objeto da classe Pyfuso
fuso = pf.Pyfuso()
### Printa as opcões de fusohorario disponíveis(nome dos Países)
fuso.get_local() 

### Retorna a data e hora referente ao local, informar o país e a cidade ex.: 'Brasil/Brasília'
date = fuso.get_data('nome_país/nome_cidade') 

### Retorna apenas o horário referente ao local, informar o país e a cidade ex.: 'Brasil/Brasília'
horario = fuso.get_hora('nome_país/nome_cidade')

### Retorna a data e o horário referente ao local e no formato desejado, informar o país e a cidade ex.: 'Brasil/Brasília' , informar o formato ex.: 'D/M/A', 'M/D/A', 'A/M/D' 
date_formato = fuso.get_data_formato('nome_país/nome_cidade','D/M/A') 

### Retorna a diferença de horas dos locais desejados
dif_fuso = fuso.get_time_diff('local1','local2')


