# Projeto: Criação de pacote de Processamento de Imagens

Descrição: O pacote image_processing-test1 é usado para:
>
	Processing:
		- Correspondência de histograma
		- Semelhança estrutural
		- Redimensionar imagem
	Utils:
		- Ler imagem
		- Salvar imagem
		- Plotar imagem
		- Resultado da plotagem
		- Plotar histograma
## Overview (template)
Este é um overview do que faremos:

![image](https://user-images.githubusercontent.com/53586684/192152925-fc3e9713-f07a-4bf9-befb-828fd46e7c0d.png)

Fonte: Karina Kato - Machine Learning Engineer/Machine Learning Tech Lead - Take

## Passo a passo
### 1. Criar um projeto
Você pode realizar um fork deste projeto para utilizá-lo como modelo. Ele já segue a organização da imagem apresentada acima.

### 2. Editar os arquivos "setup.py", "requirements.txt" e "README.md"
Após criado o projeto e editado os arquivos "setup.py", "requirements.txt" e "README.md" é necessário gerar as distribuições "wheel" e "sdist".
Para isso, você deve:

### 3. Acessar a raiz do seu projeto
Acesse a raiz do seu projeto para aplicar os próximos passos.

### 4. Aplicar os comandos de instalação
No seu terminal, aplique os seguintes comandos:

``` bash
python -m pip install --upgrade pip
```
``` bash
python -m pip install --user twine
```
``` bash
python -m pip install --user setuptools
```
``` bash
pip install wheel
````

### 5. Aplicar o comando para criar a distribuição
Crie a distribuição, aplicando o seguinte comando:

``` bash
python setup.py sdist bdist_wheel
```
### 6. Publicar pacote
Realizada as etapas anteriores com êxito, o próximo passo é a publicação do pacote.
Você precisa ter uma conta no Test Pypi e no Pypi para realizar essa etapa. A seguir os links:

https://test.pypi.org/account/register/

https://pypi.org/account/register/

### Test Pypi
#### 6.1. Primeiro, publique no Teste Pypi, aplicando o seguinte comando:
``` bash
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
#### 6.2. Agora, instale o pacote de teste:
```bash
pip install -i https://test.pypi.org/simple/ image-processing-test1
```

### Pypi
#### 6.3. Com tudo testado, é hora de publicar o pacote no Pypi:
```bash
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
#### 6.4. Instale o pacote publicado:
Utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar image_processing-test1

```bash
pip install image-processing-test1
```

## Autor

Projeto original: by Karina Kato

Este exercício: by Tiago de Freitas Faustino

Este projeto tem o objetivo apenas de exercitar a criação publicação e utilização de pacotes.
Para este fim, como ainda não tenho um projeto próprio, foram realizados apenas pequenos 
ajustes no projeto original de Karina Kato.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
