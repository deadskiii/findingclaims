from pathlib import Path

# Base directory setup
BASE_DIR = Path(r"C:\Users\sanat\Desktop\AntiGravity\findingclaims")

# Raw data directories
DATA_RAW = {
    "cms": BASE_DIR / "data" / "raw" / "cms",
    "seer": BASE_DIR / "data" / "raw" / "seer",
    "cdc_places": BASE_DIR / "data" / "raw" / "cdc_places",
    "lana": BASE_DIR / "data" / "raw" / "lana",
    "advocacy": BASE_DIR / "data" / "raw" / "advocacy",
    "apcd": BASE_DIR / "data" / "raw" / "apcd",
}

# Processed data directories
DATA_PROCESSED = {
    "cms": BASE_DIR / "data" / "processed" / "cms",
    "seer": BASE_DIR / "data" / "processed" / "seer",
    "cdc_places": BASE_DIR / "data" / "processed" / "cdc_places",
    "lana": BASE_DIR / "data" / "processed" / "lana",
    "advocacy": BASE_DIR / "data" / "processed" / "advocacy",
    "apcd": BASE_DIR / "data" / "processed" / "apcd",
}

# Output directories
OUTPUTS = {
    "maps": BASE_DIR / "outputs" / "maps",
    "reports": BASE_DIR / "outputs" / "reports",
    "exports": BASE_DIR / "outputs" / "exports",
}

# Database path
DB_PATH = BASE_DIR / "findingclaims.duckdb"

# URLs
FIPS_URL = "https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt"

# Target Code specifications
TARGET_CODES = {
    "ICD10": [
        "I89.0",  # Lymphedema (primary and secondary, any limb)
        "I87.2",  # Venous insufficiency (chronic, peripheral)
        "I87.3",  # Chronic venous hypertension
        "I83.9",  # Varicose veins without ulcer or inflammation
        "I80.9",  # Phlebitis and thrombophlebitis, unspecified
        "Q82.0",  # Hereditary lymphedema (congenital)
        "R60.0",  # Localized edema
    ],
    "HCPCS": [
        "L8100",  # Gradient compression stocking, below knee, 18-30 mmHg
        "L8110",  # Gradient compression stocking, below knee, 30-40 mmHg
        "L8120",  # Gradient compression stocking, full length or thigh, 18-30 mmHg
        "L8130",  # Custom compression garment, lower extremity
    ],
    "CPT": [
        "97016",  # Vasopneumatic device therapy (e.g. pneumatic compression)
        "97140",  # Manual therapy / manual lymphatic drainage (MLD)
        "97110",  # Therapeutic exercises used in lymphedema rehabilitation
        "93971",  # Unilateral venous duplex scan (diagnosis trigger for venous disease)
        "36475",  # Endovenous ablation, first vein (post-procedure requires compression)
    ]
}
