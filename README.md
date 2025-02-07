# Crud Gestão de Consumo e Faturamento de Energia

## Ricardo Marques

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

