// Existem dois principais tipos de threads, com base em sua criação e gerenciamento:

// Threads de nível de usuário (User-level threads):
// Essas threads são gerenciadas pela aplicação ou pela biblioteca de threads no nível do usuário, sem intervenção direta do sistema operacional. O sistema operacional não tem conhecimento sobre essas threads, ele apenas vê o processo que as contém.
// Vantagens:
// Menor sobrecarga, pois o gerenciamento de threads é feito pela própria aplicação.
// A criação e troca de contexto entre threads são rápidas.
// Desvantagens:
// Se uma thread de nível de usuário bloquear (por exemplo, em uma operação de I/O), todas as threads do processo são bloqueadas, já que o sistema operacional não consegue distinguir entre as threads.
// Threads de nível de kernel (Kernel-level threads):
// Essas threads são gerenciadas diretamente pelo sistema operacional, que é responsável pela criação, agendamento e destruição das threads.
// Vantagens:
// O sistema operacional pode agendar as threads de forma independente, permitindo que uma thread bloqueada não afete as outras.
// Melhor uso de múltiplos núcleos de processadores, pois o sistema operacional pode alocar diferentes threads para diferentes CPUs.
// Desvantagens:
// Maior sobrecarga, pois o gerenciamento de threads pelo sistema operacional exige mais recursos.
// A criação e troca de contexto entre threads pode ser mais lenta em comparação com threads de nível de usuário.
