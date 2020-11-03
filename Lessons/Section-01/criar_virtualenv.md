Criando ambiente virtual:

1) Linux

$ virtualenv [opções] <nome_da_pasta>

1.2 - Ativando ambiente virtual:
<!-- aonde está escrito ENV, por o nome do ambiente virtual que foi digitado ao ser criado -->
$ source ENV/bin/activate
<!-- source env-udemy/bin/activate -->

1.2 - Desavitar e remover:
$ deactivate
$ rm -r ENV


2) Windows 10

2.1 Instalar virtualenv
$ pip install virtualenv

2.2 Criar virtualenv
$ virtualenv [opções] <nome_da_pasta>

2.3 Ativar virtualenv

ENV\Scripts\Activate.bat

2.3 - Desavitar e remover:
$ deactivate
$ rm -r ENV
