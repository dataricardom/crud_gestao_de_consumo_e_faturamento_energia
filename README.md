# Crud Gestão de Consumo e Faturamento de Energia

## Ricardo Marques

# Backend

### Conexão com o Banco de Dados
**Configuração do SQLAlchemy com PostgreSQL**

No arquivo database.py, foi configurada a conexão com o banco de dados PostgreSQL utilizando o SQLAlchemy



### Modelos de Dados e Relacionamentos no SQLAlchemy

**Arquivo models.py**

No arquivo models.py, foram definidas as classes que representam as tabelas no banco de dados utilizando o SQLAlchemy. Essas classes seguem a estrutura do banco de dados e incluem os relacionamentos entre elas.

1. Cliente e Fatura (1:N)
- Descrição: Um cliente pode ter várias faturas, mas uma fatura só pode ter um cliente.
- Relação: 1:N (um cliente para muitas faturas).
- Explicação: A chave estrangeira cliente_id na tabela FaturaModel indica que a fatura pertence a um único cliente, enquanto um cliente pode ter várias faturas associadas a ele.
2. Cliente e Medidor (1:N)
- Descrição: Um cliente pode ter vários medidores, mas um medidor só pode pertencer a um cliente.
- Relação: 1:N (um cliente para muitos medidores).
- Explicação: A chave estrangeira cliente_id na tabela MedidorModel indica que o medidor está associado a um único cliente, e cada cliente pode ter múltiplos medidores.
3. Medidor e Leitura (1:N)
- Descrição: Um medidor pode ter várias leituras, mas uma leitura só pode pertencer a um medidor.
- Relação: 1:N (um medidor para muitas leituras).
- Explicação: A chave estrangeira medidor_id na tabela LeituraModel indica que cada leitura está associada a um único medidor, mas um medidor pode ter várias leituras.

### Estrutura dos Schemas Pydantic

o arquivo schemas.py:

Este projeto utiliza Pydantic para a validação e transformação de dados entre o cliente e o banco de dados. Abaixo está uma explicação detalhada sobre os schemas utilizados nas tabelas Cliente, Medidor, Leitura e Fatura, incluindo as operações de criação, atualização e resposta.

1. Cliente
- ClienteBase
Este modelo contém os campos essenciais para a criação e atualização de um cliente, incluindo nome, endereco, telefone e email_cliente. Este modelo é a base para outras operações.

- ClienteCreate
Herda de ClienteBase e é utilizado para criar novos clientes. Não adiciona novos campos, apenas reutiliza os campos básicos.

- ClienteResponse
Este modelo é utilizado para retornar a resposta quando um cliente for consultado no banco de dados. Além dos campos básicos (nome, endereco, etc.), inclui o campo id_cliente (identificador único gerado pelo banco) e data_cadastro (data de criação). A configuração orm_mode = True foi definida na classe Config para permitir a conversão adequada de objetos ORM (SQLAlchemy) para Pydantic.

- ClienteUpdate
Modelo utilizado para atualizar dados de um cliente. Permite a modificação dos campos endereco, telefone e email_cliente. O uso do Optional indica que esses campos são opcionais e podem ser deixados de fora na requisição, preservando os valores anteriores no banco de dados.

2. Medidor
- MedidorBase
Este modelo define os campos principais para o medidor, como client_id (referência ao cliente associado), numero_medidor e tipo. Serve como base para a criação e consulta de medidores.

- MedidorCreate
Herda de MedidorBase e é usado quando um novo medidor é criado. Não há campos novos, apenas reutiliza os campos da base.

- MedidorResponse
Além dos campos de medidor, inclui o campo medidor_id (identificador único) e data_instalacao (data de instalação do medidor). Assim como no ClienteResponse, a configuração orm_mode = True permite a conversão correta de instâncias ORM.

- MedidorUpdate
Permite a atualização dos campos de medidor, como numero_medidor e tipo. A chave client_id é obrigatória, já que cada medidor está vinculado a um cliente. Outros campos são opcionais.

3. Leitura
- LeituraBase
Define os campos básicos para a tabela de leitura, como medidor_id (referência ao medidor associado) e leitura_kwh (valor da leitura de consumo de energia).

- LeituraCreate
Herda de LeituraBase e serve para criar uma nova leitura de medidor.

- LeituraResponse
Além dos campos básicos, inclui id_leitura (identificador único da leitura) e data_leitura (data em que a leitura foi registrada). A configuração orm_mode = True foi aplicada para garantir a conversão adequada de objetos ORM.

- LeituraUpdate
Permite a atualização do valor de leitura_kwh, deixando os outros campos imutáveis durante a atualização.

4. Fatura
- FaturaBase
Este modelo contém os campos principais para a criação de faturas, como valor (quantia da fatura) e status_pagamento (indica o estado do pagamento da fatura).

- FaturaCreate
Herda de FaturaBase e é utilizado para a criação de novas faturas.

- FaturaResponse
Além dos campos de fatura, inclui id_fatura (identificador único da fatura), mes_referencia (mês da fatura), data_emissao (data de emissão) e data_vencimento (data de vencimento). O orm_mode = True é utilizado para garantir a conversão de instâncias ORM.

- FaturaUpdate
Permite a atualização de valor e status_pagamento. Ambos são opcionais, permitindo que apenas um desses campos seja alterado, sem a necessidade de alterar todos os dados da fatura.

Configuração do Pydantic
Em todas as classes de resposta (como ClienteResponse, MedidorResponse, LeituraResponse e FaturaResponse), a configuração from_attributes = True foi adicionada na classe Config. Essa configuração é importante para permitir a conversão de objetos ORM retornados pelo SQLAlchemy para modelos Pydantic. Isso garante que as instâncias ORM possam ser transformadas corretamente em formatos que o cliente pode usar, como JSON.

Conclusão
Esses schemas Pydantic são usados para validar e transformar dados de entrada e saída entre o cliente e o banco de dados. Eles garantem que os dados enviados para a API e os dados retornados da API estejam bem estruturados e corretos, utilizando validações como tipos de dados e campos opcionais. A integração com SQLAlchemy, por meio do uso de orm_mode = True, garante que as instâncias ORM sejam manipuladas corretamente durante o ciclo de vida dos dados.

Esses modelos formam a espinha dorsal da aplicação, garantindo a comunicação eficiente entre as camadas de dados e a API.


### Funções CRUD - crud.py
Este arquivo contém as funções responsáveis pelas operações CRUD (Create, Read, Update, Delete) em cada uma das tabelas do banco de dados: Clientes, Medidores, Leituras e Faturas. Essas funções são chamadas pelas rotas definidas no arquivo routers.py e interagem diretamente com o banco de dados utilizando a biblioteca SQLAlchemy.

1. CRUD para Clientes
As funções do Cliente são responsáveis por criar, buscar, atualizar e excluir registros da tabela de clientes.

get_clientes(db: Session): Retorna uma lista de todos os clientes cadastrados no banco de dados.
get_cliente(db: Session, cliente_id: int): Retorna um cliente específico com base no cliente_id.
create_cliente(db: Session, cliente: ClienteCreate): Cria um novo cliente no banco de dados. Recebe um objeto ClienteCreate com os dados necessários.
delete_cliente(db: Session, cliente_id: int): Exclui um cliente do banco de dados com base no cliente_id.
update_cliente(db: Session, cliente_id: int, cliente: ClienteUpdate): Atualiza as informações de um cliente específico no banco de dados, com base no cliente_id. Os campos que não são None na atualização são alterados.
2. CRUD para Medidores
As funções do Medidor permitem criar, buscar, atualizar e excluir medidores de consumo.

get_medidores(db: Session): Retorna uma lista de todos os medidores cadastrados no banco de dados.
get_medidor(db: Session, medidor_id: int): Retorna um medidor específico com base no medidor_id.
create_medidor(db: Session, medidor: MedidorCreate): Cria um novo medidor no banco de dados. Recebe um objeto MedidorCreate com os dados necessários.
delete_medidor(db: Session, medidor_id: int): Exclui um medidor específico com base no medidor_id.
update_medidor(db: Session, medidor_id: int, medidor: MedidorUpdate): Atualiza os dados de um medidor no banco de dados, com base no medidor_id. Caso algum campo seja None, ele não será alterado.
3. CRUD para Leituras
As funções do Leitura tratam das leituras de consumo realizadas pelos medidores.

get_leituras(db: Session): Retorna uma lista de todas as leituras registradas no banco de dados.
get_leitura(db: Session, leitura_id: int): Retorna uma leitura específica com base no leitura_id.
create_leitura(db: Session, leitura: LeituraCreate): Cria uma nova leitura no banco de dados. Recebe um objeto LeituraCreate com os dados necessários.
delete_leitura(db: Session, leitura_id: int): Exclui uma leitura específica com base no leitura_id.
update_leitura(db: Session, leitura_id: int, leitura: LeituraUpdate): Atualiza os dados de uma leitura específica no banco de dados. Caso algum campo seja None, ele não será alterado.
4. CRUD para Faturas
As funções do Fatura são responsáveis pela criação, busca, atualização e exclusão de faturas geradas com base nas leituras de consumo.

get_faturas(db: Session): Retorna uma lista de todas as faturas registradas no banco de dados.
get_fatura(db: Session, fatura_id: int): Retorna uma fatura específica com base no fatura_id.
create_fatura(db: Session, fatura: FaturaCreate): Cria uma nova fatura no banco de dados. Recebe um objeto FaturaCreate com os dados necessários.
delete_fatura(db: Session, fatura_id: int): Exclui uma fatura específica com base no fatura_id.
update_fatura(db: Session, fatura_id: int, fatura: FaturaUpdate): Atualiza os dados de uma fatura no banco de dados. Caso algum campo seja None, ele não será alterado.
Processos Internos de CRUD
Criação de Recursos: Para criar um novo recurso (cliente, medidor, leitura ou fatura), a função recebe um objeto que contém os dados do novo registro. A função então utiliza o método add do SQLAlchemy para adicionar o registro no banco de dados, seguido de um commit para salvar a alteração.

Leitura de Recursos: Para ler os dados, as funções utilizam o método query do SQLAlchemy, seguido de um filter para buscar registros específicos. O retorno pode ser uma lista (para todas as instâncias) ou um único item (para registros específicos com base no id).

Atualização de Recursos: Para atualizar um recurso, as funções primeiro verificam se o registro existe no banco de dados. Em seguida, alteram apenas os campos que não são None, e um commit é feito para salvar as alterações.

Exclusão de Recursos: Para excluir um recurso, as funções localizam o registro desejado e o removem do banco de dados com o método delete, seguido por um commit para aplicar a remoção.

Essas funções de CRUD são essenciais para o gerenciamento da aplicação, permitindo que os dados sejam manipulados de forma eficiente e segura dentro do banco de dados.





### Roteamento da API - routers.py
Este arquivo contém todas as rotas da API FastAPI para realizar operações de CRUD (Create, Read, Update, Delete) sobre os dados da aplicação. As rotas estão divididas em quatro categorias principais: Clientes, Medidores, Leituras e Faturas. Para cada uma dessas categorias, foram implementadas rotas que permitem criar, listar, atualizar, excluir e consultar informações. As operações são feitas com o auxílio de funções de CRUD definidas no arquivo crud.py.

Funcionalidade das Rotas
1. Clientes
As rotas relacionadas aos clientes permitem cadastrar, listar, atualizar, excluir e consultar dados dos clientes.

POST /cliente/: Cria um novo cliente.
GET /cliente/: Retorna uma lista de todos os clientes cadastrados.
GET /cliente/{cliente_id}: Retorna os dados de um cliente específico, identificado pelo cliente_id.
DELETE /cliente/{cliente_id}: Exclui um cliente específico, identificado pelo cliente_id.
PUT /cliente/{cliente_id}: Atualiza os dados de um cliente específico, identificado pelo cliente_id.
2. Medidores
As rotas de medidores permitem o gerenciamento de dispositivos de medição de consumo.

POST /medidor/: Cria um novo medidor.
GET /medidor/: Retorna uma lista de todos os medidores cadastrados.
GET /medidor/{medidor_id}: Retorna os dados de um medidor específico.
DELETE /medidor/{medidor_id}: Exclui um medidor específico, identificado pelo medidor_id.
PUT /medidor/{medidor_id}: Atualiza os dados de um medidor específico.
3. Leituras
As rotas de leituras permitem registrar e consultar as medições de consumo feitas pelos medidores.

POST /leitura/: Cria uma nova leitura de consumo.
GET /leitura/: Retorna uma lista de todas as leituras registradas.
GET /leitura/{leitura_id}: Retorna os dados de uma leitura específica.
DELETE /leitura/{leitura_id}: Exclui uma leitura específica.
PUT /leitura/{leitura_id}: Atualiza os dados de uma leitura específica.
4. Faturas
As rotas de faturas gerenciam os registros de cobrança gerados a partir das leituras de consumo.

POST /fatura/: Cria uma nova fatura com base nos dados informados.
GET /fatura/: Retorna uma lista de todas as faturas registradas.
GET /fatura/{fatura_id}: Retorna os dados de uma fatura específica.
DELETE /fatura/{fatura_id}: Exclui uma fatura específica.
PUT /fatura/{fatura_id}: Atualiza os dados de uma fatura específica.
Fluxo de Funcionamento
Criação de Recursos: As rotas POST são usadas para criar novos registros, seja de clientes, medidores, leituras ou faturas. Os dados são recebidos na requisição em formato JSON e passados para as funções de CRUD para inserção no banco de dados.

Leitura de Recursos: As rotas GET permitem consultar os dados no banco de dados. O recurso pode ser consultado de forma geral (ex: listar todos os clientes) ou de forma específica (ex: obter dados de um cliente pelo seu cliente_id).

Atualização de Recursos: A rota PUT é usada para atualizar os dados de um recurso existente. O cliente_id, medidor_id, leitura_id ou fatura_id são passados na URL para identificar o recurso a ser atualizado.

Exclusão de Recursos: A rota DELETE exclui um recurso específico, identificado pelo respectivo id. Se o recurso não for encontrado, uma exceção HTTP 404 é levantada.

Tratamento de Erros
Em todas as rotas, foi implementado um tratamento de erros que utiliza o código de status HTTP 404 quando um recurso solicitado não é encontrado. O erro é acompanhado de uma mensagem explicativa sobre o que ocorreu, garantindo que o usuário saiba exatamente qual recurso não pôde ser encontrado.

Considerações Finais
As rotas implementadas têm como objetivo fornecer uma interface simples para o gerenciamento de clientes, medidores, leituras e faturas. Com a FastAPI e SQLAlchemy, a comunicação com o banco de dados é eficiente e rápida, e o tratamento de exceções garante que as operações sejam realizadas de maneira segura e informativa para o usuário.

Esse texto pode ser adicionado ao seu README.md ou outro documento de explicação da sua API para descrever as funcionalidades implementadas nas rotas. Ele descreve claramente o propósito de cada conjunto de rotas, explicando como o usuário pode interagir com o sistema para realizar as operações desejadas.


### Arquivo principal main.py
Este arquivo é responsável por inicializar e configurar a aplicação FastAPI, além de estabelecer a conexão com o banco de dados, criar as tabelas necessárias e incluir as rotas definidas para interagir com os recursos da aplicação.

1. Importação de dependências
from fastapi import FastAPI: Importa a classe FastAPI, que é utilizada para criar a instância da aplicação web.
from database import engine: Importa o objeto engine, que é responsável pela conexão com o banco de dados. Este objeto foi configurado no arquivo database.py.
import models: Importa o arquivo models.py, onde estão definidos os modelos de dados (tabelas) que serão usadas no banco de dados.
from routers import routers: Importa as rotas definidas no arquivo routers.py. Essas rotas gerenciam as operações CRUD para os recursos da aplicação, como clientes, medidores, leituras e faturas.
2. Criação das tabelas no banco de dados
models.Base.metadata.create_all(bind=engine): Este comando cria todas as tabelas no banco de dados conforme definidos nos modelos do arquivo models.py. Ele usa a metadata da Base para gerar as tabelas, e o bind=engine garante que as tabelas sejam criadas na conexão com o banco de dados especificada pelo engine. Esse processo é realizado automaticamente sempre que o aplicativo é iniciado.
3. Inicialização da aplicação FastAPI
app = FastAPI(): Aqui, a aplicação FastAPI é criada e a variável app é a instância da aplicação.
4. Inclusão das rotas na aplicação
app.include_router(routers): Esse comando inclui as rotas definidas no arquivo routers.py dentro da instância da aplicação FastAPI. A variável routers contém as rotas que foram configuradas, e essa linha garante que as rotas estejam acessíveis quando a API estiver em execução.
Resumo do Processo:
O FastAPI é iniciado criando uma instância de FastAPI().
As tabelas do banco de dados são criadas utilizando o comando create_all().
As rotas (definidas no arquivo routers.py) são adicionadas ao aplicativo usando app.include_router(routers).
Ao executar a aplicação, a FastAPI disponibiliza os endpoints definidos no arquivo routers.py, permitindo que os usuários interajam com os dados (clientes, medidores, leituras e faturas) via API.
Isso configura a aplicação e o banco de dados de forma que você pode fazer chamadas HTTP para realizar operações como cadastrar, consultar, atualizar e excluir dados dos recursos da aplicação.



<p align="center">
  <img src="pic/KPUUDATA.png" alt="logo" width="300"/>
</p>