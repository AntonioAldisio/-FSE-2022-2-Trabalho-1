# Trabalho 01
### Como rodar

É necessário configurar os arquivos sala_1.json e sala_2.json no diretorio src/json, onde encontra-se a informação dos IPs, portas e gpios selecionadas.
Deve ser mantem o mesmo ip e porta para o servidor central nos dois arquivos (sala_1.json e sala_2.json).

Inserir environment PYTHONPATH no ambiente que estiver executando o projeto e instalar as dependencias necessarias

```
export PYTHONPATH="$PWD/src"
make dependencias
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
[Link youtube](https://youtu.be/PftdVvnQKOw)

#### [Link do projeto](https://gitlab.com/fse_fga/trabalhos-2022_2/trabalho-1-2022-2)
