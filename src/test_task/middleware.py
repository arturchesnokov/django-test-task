import time

from user_profile.tasks import logger_write_db


# 3. Create middleware that stores all requests and execution time.
class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        full_time = time.time() - start_time
        full_path = request.path

        # if full_path.startswith('/admin/'):
        #     if request.user.pk is None:
        #         request.user.pk = 0
        if request.user.pk is None:
            request.user.pk = 0

        # logger_write_db(full_path, request.method, full_time, int(request.user.pk))
        logger_write_db.delay(full_path, request.method, full_time, int(request.user.pk))

        return response
