from jobspy import scrape_jobs
from .models import JobPost
from datetime import date

TIPO_CONTRATO_MAP = {
    'full-time': 'CLT',
    'part-time': 'CLT',
    'contract':  'PJ',
    'internship':'Estágio',
    'freelance': 'Freelancer',
}

LOCAL_MAP = {
    'remote':  'Remoto',
    'hybrid':  'Híbrido',
    'on-site': 'Presencial',
}

def buscar_vagas_externas(termo='desenvolvedor', localizacao='Brazil', quantidade=15):
    try:
        jobs = scrape_jobs(
            site_name=["indeed", "linkedin"],
            search_term=termo,
            location=localizacao,
            results_wanted=quantidade,
            hours_old=48,
            country_indeed='Brazil',
        )
    except Exception as e:
        print(f"Erro no scraping: {e}")
        return 0

    novas = 0
    for _, row in jobs.iterrows():
        url = str(row.get('job_url', '') or '').strip()
        if not url:
            continue

        if JobPost.objects.filter(url=url).exists():
            continue

        # Mapeia tipo de contrato
        job_type_raw = str(row.get('job_type', '') or '').lower()
        tipo_contrato = TIPO_CONTRATO_MAP.get(job_type_raw, 'CLT')

        # Mapeia local de trabalho
        is_remote = row.get('is_remote', False)
        local_trabalho = 'Remoto' if is_remote else 'Presencial'

        # Salário — pega o mínimo se disponível
        salario = None
        try:
            salario = float(row.get('min_amount', 0) or 0) or None
        except (ValueError, TypeError):
            salario = None

        JobPost.objects.create(
            titulo=str(row.get('title', '') or '')[:255],
            empresa=str(row.get('company', '') or '')[:200],
            descricao=str(row.get('description', '') or '')[:200],
            cidade=str(row.get('location', 'Brasil') or 'Brasil')[:255],
            tipo_contrato=tipo_contrato,
            local_trabalho=local_trabalho,
            salario=salario,
            link_inscricao=url[:200],
            url=url,
            source=str(row.get('site', 'externo')),
            data_publicacao=date.today(),
            prazo_inscricao=date.today(),
        )
        novas += 1

    return novas