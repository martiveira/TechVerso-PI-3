from jobspy import scrape_jobs
from .models import JobPost  # ajuste para o nome do seu model


def buscar_vagas_externas(termo='desenvolvedor', localizacao='Brazil', quantidade=15):
    try:
        jobs = scrape_jobs(
            site_name=["linkedin", "indeed", "glassdoor"],
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
        url = str(row.get('job_url', '') or '')
        if not url:
            continue

        # evita duplicatas pela URL
        if JobPost.objects.filter(url=url).exists():
            continue

        JobPost.objects.create(
            title=str(row.get('title', '') or '')[:200],
            company=str(row.get('company', '') or '')[:200],
            location=str(row.get('location', '') or '')[:200],
            description=str(row.get('description', '') or ''),
            url=url,
            source=str(row.get('site', 'externo')),
        )
        novas += 1

    return novas
