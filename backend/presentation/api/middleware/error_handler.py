"""
Error Handler Middleware

Xử lý lỗi centralized cho toàn bộ application
"""
from flask import jsonify
from werkzeug.exceptions import HTTPException
import logging
import traceback

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    """
    Đăng ký tất cả error handlers
    """
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        """Handle all unhandled exceptions"""
        # Pass through HTTP errors properly
        if isinstance(e, HTTPException):
            return jsonify({
                "status": "error",
                "message": e.description or str(e)
            }), e.code
        
        # Always log errors
        logger.exception("Unhandled exception: %s", e)
        
        response_body = {
            "status": "error",
            "code": "INTERNAL_ERROR",
            "message": "Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau."
        }
        
        # Only include details in debug mode
        if app.debug:
            response_body["message"] = str(e)
            response_body["details"] = traceback.format_exception(type(e), e, e.__traceback__)
        
        return jsonify(response_body), 500
    
    @app.errorhandler(404)
    def not_found(e):
        """Handle 404 errors"""
        return jsonify({
            "status": "error",
            "code": "NOT_FOUND",
            "message": "Endpoint không tồn tại"
        }), 404
    
    @app.errorhandler(400)
    def bad_request(e):
        """Handle 400 errors"""
        return jsonify({
            "status": "error",
            "code": "BAD_REQUEST",
            "message": str(e)
        }), 400
