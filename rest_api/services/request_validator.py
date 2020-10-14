class RequestValidator:
    @staticmethod
    def validate_params(params, required):
        collection = []
        for param in required:
            if param not in params:
                return False
            collection.append(params[param])
        return collection
