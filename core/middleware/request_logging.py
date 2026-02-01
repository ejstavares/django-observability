import time
import structlog
from django.utils.deprecation import MiddlewareMixin
from request_id import local

log = structlog.get_logger()

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_ts = time.time()

    def process_response(self, request, response):
        duration_ms = None
        if hasattr(request, "_start_ts"):
            duration_ms = int((time.time() - request._start_ts) * 1000)

        rid = getattr(local, "request_id", None)

        log.info(
            "http_request",
            request_id=rid,
            method=request.method,
            path=request.path,
            status_code=response.status_code,
            duration_ms=duration_ms,
            remote_addr=request.META.get("REMOTE_ADDR"),
            user_agent=request.META.get("HTTP_USER_AGENT"),
        )
        return response
