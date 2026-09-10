🍱 Sistema de Gerenciamento e Encomendas de Almoço📍 Instituto Federal de Brasília (IFB) — Campus TaguatingaUma solução web modernizada para automatizar a reserva de refeições, evitar filas e zerar o desperdício no campus.🎯 Sobre o ProjetoEste projeto foi desenvolvido para revolucionar o processo de refeições acadêmicas. Substituindo fluxos manuais e filas por uma plataforma totalmente digital, os alunos conseguem agendar seus almoços direto do smartphone, enquanto a equipe da cozinha obtém métricas em tempo real da demanda do dia.✨ Funcionalidades em Destaque📱 Visão do Estudante👨‍🍳 Visão da Gestão & Cozinha📱 Mobile First: Interface leve para pedir pelo celular📊 Métricas do Dia: Quantitativo exato de almoços do dia📅 Agendamento: Reserva antecipada da refeição🌱 Desperdício Zero: Planejamento exato de insumos⚡ Status do Pedido: Confirmação e acompanhamento em tempo real✅ Validação Ágil: Controle rápido na entrega dos pratos🛠️ Tech StackCore & Back-end: Python, Django (Arquitetura MVT & ORM)Banco de Dados: PostgreSQLDevOps & Deploy: Docker, Docker Compose, RenderFront-end: HTML5, CSS3, JavaScript (Layout Responsivo)🚀 Como Rodar Localmente[!TIP]Cerifique-se de ter o Git e o Docker Engine instalados em sua máquina antes de prosseguir.Bash# 1. Clone o repositório
git clone https://github.com/Marconny-Marques/sistema_encomendas_almoco_ifb.git

# 2. Acesse a pasta
cd sistema_encomendas_almoco_ifb

# 3. Configure as variáveis de ambiente
cp .env.example .env

# 4. Inicie o container
docker-compose up --build
🌐 Após a inicialização, abra em seu navegador: http://localhost:8000📂 Estrutura do RepositórioPlaintext📦 sistema_encomendas_almoco_ifb
 ┣ 📂 core/                # Configurações globais do Django
 ┣ 📂 encomendas/          # Módulo de regras de negócio e contagem de refeições
 ┣ 📂 static/              # Estilização CSS e scripts JS
 ┣ 📂 templates/           # Layouts HTML responsivos
 ┣ 📜 Dockerfile           # Imagem para deploy no Render
 ┣ 📜 docker-compose.yml   # Orquestração do app + PostgreSQL
 ┗ 📜 manage.py            # CLI do Django
