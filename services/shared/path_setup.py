"""
Path Setup Utility

Helper để setup sys.path cho mỗi microservice.
Đảm bảo shared modules (python/) luôn available.
"""
import os
import sys


def setup_service_paths():
    """
    Setup sys.path cho một microservice.
    
    Thêm các directories cần thiết:
    - services/shared/
    - python/ (backward compat)
    - project root (cho vi_dieu_phap, etc.)
    """
    # Determine project root (tuvi-app/)
    service_dir = os.path.dirname(os.path.abspath(__file__))  # shared/
    services_dir = os.path.dirname(service_dir)                # services/
    project_root = os.path.dirname(services_dir)               # tuvi-app/
    
    python_dir = os.path.join(project_root, 'python')
    backend_dir = os.path.join(project_root, 'backend')
    
    # Add paths in priority order
    paths_to_add = [
        python_dir,      # python/core, python/chart, etc.
        backend_dir,     # backend/application, backend/presentation, etc.
        project_root,    # for vi_dieu_phap, etc.
        service_dir,     # shared/ itself
    ]
    
    for p in paths_to_add:
        if p not in sys.path and os.path.isdir(p):
            sys.path.insert(0, p)
    
    return {
        'project_root': project_root,
        'python_dir': python_dir,
        'backend_dir': backend_dir,
        'services_dir': services_dir,
        'shared_dir': service_dir,
    }


def get_project_root():
    """Return absolute path to project root (tuvi-app/)"""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
