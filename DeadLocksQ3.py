"""""
Garante que o sistema não entre em impasse. Como as regras de prevenção impedem que um deadlock ocorra, o sistema nunca ficará travado esperando por recursos.
Facilita a depuração e manutenção do sistema. OS sistemas sem deadlocks são mais previsíveis e fáceis de testar, pois não entram em estados indefinidos ou difíceis de reproduzir.
Melhora tambem a confiabilidade e a disponibilidade, e evitar deadlocks é essencial em sistemas críticos, como servidores, bancos de dados e sistemas operacionais.
Exemplo: Um banco de dados que usa travas (locks) em tabelas precisa evitar que transações fiquem presas. E tambem um menor consumo de recursos a longo prazo
Evitar deadlocks evita que processos fiquem bloqueados por tempo indefinido, liberando recursos mais rapidamente para outras operações.

"""