


# middleware/log_json_body.py
# import logging
import json, os

# logger = logging.getLogger("request.body")

class LogRequestBodyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if os.getenv('DEBUG') == "dev":
            if request.method in ('POST', 'PUT', 'PATCH'):
                try:
                    body = request.body.decode('utf-8')
                    data = json.loads(body)
                    # logger.info(f"{request.method} {request.path} body: {data}")
                    print(data)
                except Exception as e:
                    print(e)
                    # logger.warning(f"Cannot parse body: {e}")
        return self.get_response(request)
