# Trabalho 01

## Introdução
Este trabalho tem por objetivo a criação de um sistema distribuído de automação predial para monitoramento e acionamento de sensores e dispositivos de um prédio com múltiplas salas. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um servidor central responsável pelo controle e interface com o usuário e servidores distribuídos para leitura e acionamento dos dispositivos. Dentre os dispositivos envolvidos estão o monitoramento de temperatura e umidade, sensores de presença, sensores de fumaça, sensores de contagem de pessoas, sensores de abertura e fechamento de portas e janelas, acionamento de lâmpadas, aparelhos de ar-condicionado, alarme e aspersores de água em caso de incêndio.

### Como rodar

É necessário configurar os arquivos sala_1.json e sala_2.json no diretorio src/json, onde encontra-se a informação dos IPs, portas e gpios selecionadas.

Inserir environment PYTHONPATH no ambiente que estiver executando o projeto

```
export PYTHONPATH="$PWD/src"
```

Para rodar o servidor central dentro FSE-2022-2-Trabalho-1:

```
make central
```

Para rodar o servidor distribuido dentro FSE-2022-2-Trabalho-1:

```
make distribuido
```
## Apresentação
[Link youtube](testeeset)

#### [Link do projeto](https://gitlab.com/fse_fga/trabalhos-2022_2/trabalho-1-2022-2)
