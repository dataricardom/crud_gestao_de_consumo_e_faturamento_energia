# Crud Gestão de Consumo e Faturamento de Energia

## Ricardo Marques


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

# Estrutura dos Schemas Pydantic

o arquivo schemas.py:

Este projeto utiliza Pydantic para a validação e transformação de dados entre o cliente e o banco de dados. Abaixo está uma explicação detalhada sobre os schemas utilizados nas tabelas Cliente, Medidor, Leitura e Fatura, incluindo as operações de criação, atualização e resposta.

1. Cliente
ClienteBase
Este modelo contém os campos essenciais para a criação e atualização de um cliente, incluindo nome, endereco, telefone e email_cliente. Este modelo é a base para outras operações.

ClienteCreate
Herda de ClienteBase e é utilizado para criar novos clientes. Não adiciona novos campos, apenas reutiliza os campos básicos.

ClienteResponse
Este modelo é utilizado para retornar a resposta quando um cliente for consultado no banco de dados. Além dos campos básicos (nome, endereco, etc.), inclui o campo id_cliente (identificador único gerado pelo banco) e data_cadastro (data de criação). A configuração orm_mode = True foi definida na classe Config para permitir a conversão adequada de objetos ORM (SQLAlchemy) para Pydantic.

ClienteUpdate
Modelo utilizado para atualizar dados de um cliente. Permite a modificação dos campos endereco, telefone e email_cliente. O uso do Optional indica que esses campos são opcionais e podem ser deixados de fora na requisição, preservando os valores anteriores no banco de dados.

2. Medidor
MedidorBase
Este modelo define os campos principais para o medidor, como client_id (referência ao cliente associado), numero_medidor e tipo. Serve como base para a criação e consulta de medidores.

MedidorCreate
Herda de MedidorBase e é usado quando um novo medidor é criado. Não há campos novos, apenas reutiliza os campos da base.

MedidorResponse
Além dos campos de medidor, inclui o campo medidor_id (identificador único) e data_instalacao (data de instalação do medidor). Assim como no ClienteResponse, a configuração orm_mode = True permite a conversão correta de instâncias ORM.

MedidorUpdate
Permite a atualização dos campos de medidor, como numero_medidor e tipo. A chave client_id é obrigatória, já que cada medidor está vinculado a um cliente. Outros campos são opcionais.

3. Leitura
LeituraBase
Define os campos básicos para a tabela de leitura, como medidor_id (referência ao medidor associado) e leitura_kwh (valor da leitura de consumo de energia).

LeituraCreate
Herda de LeituraBase e serve para criar uma nova leitura de medidor.

LeituraResponse
Além dos campos básicos, inclui id_leitura (identificador único da leitura) e data_leitura (data em que a leitura foi registrada). A configuração orm_mode = True foi aplicada para garantir a conversão adequada de objetos ORM.

LeituraUpdate
Permite a atualização do valor de leitura_kwh, deixando os outros campos imutáveis durante a atualização.

4. Fatura
FaturaBase
Este modelo contém os campos principais para a criação de faturas, como valor (quantia da fatura) e status_pagamento (indica o estado do pagamento da fatura).

FaturaCreate
Herda de FaturaBase e é utilizado para a criação de novas faturas.

FaturaResponse
Além dos campos de fatura, inclui id_fatura (identificador único da fatura), mes_referencia (mês da fatura), data_emissao (data de emissão) e data_vencimento (data de vencimento). O orm_mode = True é utilizado para garantir a conversão de instâncias ORM.

FaturaUpdate
Permite a atualização de valor e status_pagamento. Ambos são opcionais, permitindo que apenas um desses campos seja alterado, sem a necessidade de alterar todos os dados da fatura.

Configuração do Pydantic
Em todas as classes de resposta (como ClienteResponse, MedidorResponse, LeituraResponse e FaturaResponse), a configuração orm_mode = True foi adicionada na classe Config. Essa configuração é importante para permitir a conversão de objetos ORM retornados pelo SQLAlchemy para modelos Pydantic. Isso garante que as instâncias ORM possam ser transformadas corretamente em formatos que o cliente pode usar, como JSON.

Conclusão
Esses schemas Pydantic são usados para validar e transformar dados de entrada e saída entre o cliente e o banco de dados. Eles garantem que os dados enviados para a API e os dados retornados da API estejam bem estruturados e corretos, utilizando validações como tipos de dados e campos opcionais. A integração com SQLAlchemy, por meio do uso de orm_mode = True, garante que as instâncias ORM sejam manipuladas corretamente durante o ciclo de vida dos dados.

Esses modelos formam a espinha dorsal da aplicação, garantindo a comunicação eficiente entre as camadas de dados e a API.