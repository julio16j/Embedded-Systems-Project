**INTRODUÇÃO**

  Com o advento da eletrônica digital, os sistemas que antes eram analógicos passaram a possuir processamento lógico. Em consequência a isso, o emprego da eletrônica digital nos sistemas atuais é algo que nos últimos 50 anos vem se expandindo para os mais variados dispositivos que antes eram apenas analógicos.

  Um exemplo de equipamento historicamente analógico, são as fechaduras de portas, é algo que a séculos é utilizado em conjunto com uma chave mecânica e atualmente segue sendo amplamente utilizado pela população mundial como um equipamento analógico.

  Por meio disso, é pretendido no presente trabalho o desenvolvimento de um sistema digital que será responsável pela abertura automática de uma fechadura de uma porta. Essa fechadura será um atuador elétrico acionado por meio de um microcontrolador de espressif chamado ESP32. 

  O usuário deverá por meio de uma tag de RFID se identificar para o ESP32. O ESP32 por sua vez irá se comunicar via wifi com um sistema robusto que irá verificar se o usuário tem permissão para abrir a porta, em caso afirmativo, o ESP32 envia um sinal elétrico para a tranca e por meio disso é liberada a passagem do usuário.

A grande vantagem desse projeto é a unificação de todas as chaves de um ambiente onde existem muitas portas que necessitam de controle de acesso. Um exemplo disso é o IFPB campus Campina Grande que necessita de um setor de chaves para liberar o acesso a laboratórios para alunos e servidores.

Com esse sistema os alunos e servidores do campus Campina Grande podem acessar qualquer ambiente do campus onde eles possuam acesso utilizando apenas um cartão de acesso pessoal que eles podem levar para casa.

Além disso, esse sistema não é propenso a erros de administração de acesso humanos, sendo possível saber exatamente quem adentrou um ambiente restrito do campus com precisão de horário. Esse sistema também visa a redução de custos com funcionários devido a obsolescência desses profissionais para controle de acesso a ambientes do campus.

Atualmente existem no mercado sistemas semelhantes ao desenvolvido neste projeto. Um exemplo disso seria a Fechadura Digital FR 201 da Intelbras, no entanto essa fechadura custa em média em diversos sites como Amazon, Magazine Luiza, Americanas e outros, o valor de R$ 800,00. O valor de custo do presente projeto gira em torno de R$ 200,00 por fechadura, além disso, existe a possibilidade de aperfeiçoamento e redução de custos desse projeto pela equipe de engenharia envolvida.

**ESCOPO DO PROJETO**

No presente projeto é pretendido realizar o controle de acesso a portas por meio de um sistema digital. Abaixo é possível visualizar a lista de componentes do projeto.

Componentes:

1 - Tranca eletrônica Senoidal

2 - Fonte externa

3 - led verde

4 - buzzer

5 - ESP32

5.1 - módulo Wifi

**Objetivos**

- **Geral:** 
  - Desenvolver um sistema de controle de acesso que utiliza uma fechadura eletrônica controlada por um ESP32.

- **Específico:**

- **ESP32**
  - Utilizar sensor RFID para receber dados dos cartões de acesso.
  - Utilizar o módulo Wifi do ESP32 para se comunicar com o servidor via internet.
  - Utilizar fechadura eletrônica com auxílio de fonte externa para acionamento do atuador.

- **SERVIDOR**
  - Ponto de acesso de cadastro, remoção e atualização de usuário.
  - Ponto de acesso de cadastro, remoção e atualização de trancas.
  - Ponto de acesso de cadastro, remoção e atualização de horários.

- **APLICAÇÃO WEB**
  - Tela de login de administrador
  - Tela de listagem. cadastro, remoção e atualização de usuário.
  - Tela de listagem. cadastro, remoção e atualização de trancas.
  - Tela de listagem. cadastro, remoção e atualização de horários.
