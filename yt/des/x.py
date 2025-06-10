from fpdf import FPDF

# Dados estruturados para o PDF
steps = [
    {
        "etapa": "Ideação e Proposta de Valor",
        "descricao": "Definir o que é o produto, para quem ele serve e qual problema resolve.",
        "ferramentas": "Notion, Google Docs, Miro (Lean Canvas)",
        "resultado": "Ideia clara com proposta de valor definida."
    },
    {
        "etapa": "Pesquisa de Mercado e Benchmarking",
        "descricao": "Analisar concorrentes, identificar oportunidades, estudar seu público e validar ideias preliminares.",
        "ferramentas": "Google Trends, SimilarWeb, pesquisas manuais, Typeform",
        "resultado": "Insights de mercado e diferencial competitivo definido."
    },
    {
        "etapa": "Personas e Jornada do Usuário",
        "descricao": "Criar perfis fictícios de usuários e mapear sua experiência ideal com o produto.",
        "ferramentas": "UXPressia, Figma, Miro, Notion",
        "resultado": "Perfil e comportamento do usuário claramente mapeado."
    },
    {
        "etapa": "Levantamento de Requisitos",
        "descricao": "Requisitos funcionais e não funcionais baseados nas personas e na proposta de valor.",
        "ferramentas": "Google Docs, Notion, planilhas Google",
        "resultado": "Documento de requisitos completo."
    },
    {
        "etapa": "Casos de Uso e Regras de Negócio",
        "descricao": "Descrever fluxos de interação entre usuário e sistema.",
        "ferramentas": "Lucidchart, Draw.io, PlantUML",
        "resultado": "Casos de uso e lógica do negócio definidos."
    },
    {
        "etapa": "Story Mapping e Backlog",
        "descricao": "Criar backlog inicial priorizado com base em histórias de usuário.",
        "ferramentas": "Trello, Jira, GitHub Projects",
        "resultado": "Lista de funcionalidades priorizadas."
    },
    {
        "etapa": "Wireframes e Mockups",
        "descricao": "Esboços de telas e visualizações mais fiéis do produto.",
        "ferramentas": "Figma, Balsamiq, Whimsical",
        "resultado": "Primeira visualização da interface."
    },
    {
        "etapa": "Prototipagem Interativa",
        "descricao": "Criar um protótipo navegável para testes de usabilidade.",
        "ferramentas": "Figma, MarvelApp",
        "resultado": "Validação visual e de usabilidade."
    },
    {
        "etapa": "Cronograma e Planejamento Ágil",
        "descricao": "Dividir o projeto em etapas (sprints), definir marcos e tempo estimado para cada fase.",
        "ferramentas": "Notion, Gantt chart, planilhas Google",
        "resultado": "Roadmap visual com prazos."
    },
]

# Criação do PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Guia de Desenvolvimento de Software - Etapas", ln=True, align="C")

pdf.set_font("Arial", "", 12)
for step in steps:
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Etapa: {step['etapa']}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Descrição: {step['descricao']}")
    pdf.multi_cell(0, 8, f"Ferramentas: {step['ferramentas']}")
    pdf.multi_cell(0, 8, f"Resultado Esperado: {step['resultado']}")
    pdf.ln(3)

# Salvar o PDF
pdf_output_path = "./guia_desenvolvimento_software.pdf"
pdf.output(pdf_output_path)
pdf_output_path
