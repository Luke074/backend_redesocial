

def returnStatus(http_status: int, success: bool, message: str, data: list = None):
    if data is None:
        data = []

    return {
        "http_status": http_status,
        "success": success,
        "message": message,
        "data": data
    }
