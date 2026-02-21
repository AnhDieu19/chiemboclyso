from .infrastructure.json_repository import JsonRepository
from .application.graph_service import GraphService
from .presentation.web.routes import create_vdp_blueprint

# Composition Root
_repo = JsonRepository()
_service = GraphService(_repo)

# Create and Expose Blueprint
vdp_bp = create_vdp_blueprint(_service)

# Backward compatibility alias
VdpRepository = JsonRepository
