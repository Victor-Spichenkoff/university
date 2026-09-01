# Introdução

Trabalho realizado ao longo de 8 sprints, as quais serão exemplificadas abaixo. Supervisão de desenvolvedor sênior e suporte de gerente de projeto.



O Projeto, por questão contratual, não pode ser anexado, contudo, tratou-se de um API desenvolvida em ASP.NET, com banco em Postgres, RabbitMQ, Webhook. O projeto foi iniciado do zero, portanto, vi sua criação completa. 



O apontamento de horas era feito, nos 2 primeiros meses, via planilha. Vou anexar a planilha do segundo mês (o primeiro que trabalhei mais de 160 horas)





# Rotina

- 2 daylies por dia.
  
  - A primeira interna, às 9:30
  
  - A segunda com o cliente, às 10:30

- Sprints reviews realizadas quinzenalmente para revisar e apresentar o progresso

- Comunicação via Teams e Outlook

Segue descrição mais detalhada sobre cada sprint



# Sprint 1

- Primeiro contato com Git e GitHub no ambiente profissional

- Criação de docker-compose com configuração do banco de dados
  
  - Na sprint 4, esse banco Postgres será trocado por um Postgis, contistuindo um desafio para alterar o tipo, mas mantendo os dados locais. Após alguma pesquisa, realizei o procedimento com sucesso

- Criar um CRUD básico da entidade Motorista
  
  - Houve um pequeno desentendimento aqui. A task pedia para implementar utilizando classes dedicadas, contudo eu imaginei ser como um Service comum. Posteriormente, ficou claro tratar-se do padrão Mediator. 

- Adicionar Swagger básico

- Configurar Redis
  
  - Aqui, fiz minha primeira reunião. Feita com o arquiteto de software. Ele pediu para remover o código para Redis, pois seria usado uma lib interna. Contudo, posteriormente, a ideia foi deixada e tive que adicionar novamente.

# Sprint 2

- Adição de validações para telefone, CPF, CNH e CPNJ

- Mapeamento com conversão para de telefones, CPFs, datas

- Refatoração: Alguns Enums estavam em português e outros em inglês. Realizei a padronização em inglês

- Correção da injeção de dependência, quebrando em arquivos por camada.

- Adição de middleware global para tratar exeções

# Sprint 3

- Adição de testes para os use cases de autenticação

- Reaplicação de cache e uso para relatórios (evitar consultas frequentes)

- Reescrita alterando de Service para UseCase

# Sprint 4

- Adição de seed para entidades principais

- Criação de script para automatizar a geração de backups do banco em desenvolvimento e sua restauração
  
  - Tarefa sugerida por mim para melhorar o fluxo e aprovada pela gestora

- POC API de suporte
  
  - Outra ideia minha
  
  - Uma API em TS para simular integrações com terceiros, com controle total.
  
  - Não posso colocar o código exato, questões contratuais, mas anexo uma versão minha feita anteriormente e bem similar. 
  
  - LINK: 

# Sprint 5

- Documentar a POC, que foi aprovada em reunião com um dos clientes

- Endpoint com consulta para obter a performance de um motorista

- Refatoração dos enpoints de dashboard
  
  - As queries eram realizadas diretamente nos controllers. Realizei a refatoração para utilizar Mediator em todos

- Refatoração de busca de motoristas
  
  - Adição de filtros agregados e 

# Sprint 6

- Criação da entidade "Notificação"

- Geocode reverso: consulta para API do google passando coordenadas e recebendo endereço

- Criação de entidade de "Feedback" de viagem

- Adição de endpoints necessários para um dos clientes da API (Bot de Whatsapp)

# Sprint 7

- Entidade e comportamento de Chat
  
  - Enviar e receber mensagens da central de atendimento para motorista

- Integração com API de envio de email
  
  - Foi criada pelo próprio cliente e disponibilizada

- Health check

- Criação de sistema de recuperação de senha
  
  - Multi-etapas, envio de OTP para email

- Criação multi-etapas
