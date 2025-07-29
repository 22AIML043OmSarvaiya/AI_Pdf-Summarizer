"""
Configuration file for PDF Summarizer
Customize these settings to match your requirements
"""

# Application Settings
APP_NAME = "Secure PDF Summarizer - Professional Edition"
APP_VERSION = "2.0.0"
APP_DESCRIPTION = "AI-powered PDF summarization with privacy-first design"

# Model Configuration
DEFAULT_MODEL = "sshleifer/distilbart-cnn-12-6"
FALLBACK_MODELS = [
    "facebook/bart-large-cnn",
    "google/pegasus-xsum"
]

# Processing Settings
MAX_FILE_SIZE_MB = 50
MAX_TEXT_LENGTH = 100000  # characters
CHUNK_SIZE = 1024  # words per chunk

# Summary Settings
SUMMARY_LENGTHS = {
    "short": {"min_words": 50, "max_words": 200, "ratio": 0.4},
    "medium": {"min_words": 100, "max_words": 400, "ratio": 0.3},
    "long": {"min_words": 200, "max_words": 800, "ratio": 0.25},
    "very_long": {"min_words": 400, "max_words": 1200, "ratio": 0.2}
}

# UI Settings
THEME_COLOR = "#667eea"
SECONDARY_COLOR = "#764ba2"
SUCCESS_COLOR = "#28a745"
WARNING_COLOR = "#ffc107"
ERROR_COLOR = "#dc3545"

# Export Formats
EXPORT_FORMATS = {
    "txt": "Plain Text",
    "html": "HTML Report",
    "md": "Markdown"
}

# Security Settings
ENCRYPTION_ENABLED = True
TEMP_FILE_CLEANUP = True
SESSION_TIMEOUT = 3600  # seconds

# Performance Settings
GPU_PREFERRED = True
BATCH_SIZE = 1
MAX_CONCURRENT_PROCESSES = 1

# Logging Settings
LOG_LEVEL = "INFO"
LOG_FILE = "pdf_summarizer.log"
ENABLE_DEBUG_MODE = False 