"""
Configuration Module

Centralized configuration for the application
"""
import os

class Config:
    """Base configuration"""

    # Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        # Only allow missing SECRET_KEY in development
        import sys
        if 'pytest' not in sys.modules:
            raise ValueError(
                "SECRET_KEY environment variable must be set. "
                "Generate a secure key with: python -c 'import secrets; print(secrets.token_hex(32))'"
            )
        SECRET_KEY = 'test-secret-key-for-development-only'

    DEBUG = False
    
    # Application config
    APP_NAME = "Tử Vi Đẩu Số"
    APP_VERSION = "2.0.0"
    
    # API config
    API_VERSION = "v1"
    
    # Gemini AI config
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY') or ''
    
    # Database config (for future use)
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///tuvi.db'


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    

# Config mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
