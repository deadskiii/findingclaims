# FindingClaims — Healthcare Provider Targeting from Public Data

A Python pipeline that collects, cleans, and combines 6 public healthcare datasets to identify high-opportunity HCPs (Healthcare Providers) and geographies for medical device sales, specifically compression garments for lymphedema treatment.

## Data Sources
* **CMS Medicare Part B** — provider-level claim volumes by procedure and diagnosis code
* **SEER Cancer Registry** — county-level cancer incidence and survivorship by type
* **CDC PLACES** — county and census-tract chronic disease prevalence estimates
* **LANA CLT Directory** — certified lymphedema therapist locations across the US
* **Patient Advocacy (LE&RN / NLN)** — lymphedema support group and provider directories
* **APCD (All-Payer Claims Databases)** — state-level all-payer claims (Phase 2, DUA required)

## Pipeline Overview
1. CMS Medicare Data (`01_cms_medicare.ipynb`)
2. SEER Cancer Registry (`02_seer_cancer.ipynb`)
3. CDC PLACES (`03_cdc_places.ipynb`)
4. LANA Directory Scrape (`04_lana_scrape.ipynb`)
5. Advocacy Organization Scrape (`05_advocacy_scrape.ipynb`)
6. APCD Processing (`06_apcd_placeholder.ipynb`)
7. Combine and Score (`07_combine_and_score.ipynb`)

## Setup Instructions

```bash
conda env create -f environment.yml
conda activate findingclaims
# Or alternatively with pip:
pip install -r requirements.txt
```

## Notes
- Geographic grain is county (FIPS code).
- Storage engine is DuckDB.

*Built as part of a real-world medical sales intelligence project*
