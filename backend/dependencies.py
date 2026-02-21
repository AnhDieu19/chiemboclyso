"""
Dependency Injection Container

Quản lý dependencies cho toàn bộ application
"""

class DependencyContainer:
    """
    Container đơn giản cho dependency injection
    """
    
    def __init__(self):
        self._services = {}
        
    def register(self, name: str, service):
        """Đăng ký một service"""
        self._services[name] = service
        
    def get(self, name: str):
        """Lấy một service"""
        if name not in self._services:
            raise KeyError(f"Service '{name}' chưa được đăng ký")
        return self._services[name]
    
    def has(self, name: str) -> bool:
        """Kiểm tra service đã đăng ký chưa"""
        return name in self._services


# Global container instance
container = DependencyContainer()


def setup_dependencies():
    """
    Setup tất cả dependencies cho application
    Được gọi khi khởi động app
    """
    # Import các services cần thiết
    # Sẽ được implement sau khi có các services
    
    # Example:
    # from backend.infrastructure.external.gemini_ai_service import GeminiAIService
    # container.register('ai_service', GeminiAIService())
    
    pass
