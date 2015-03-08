from hashlib import md5

class SecretBallotMiddleware(object):
    def process_request(self, request):
        request.secretballot_token = self.generate_token(request)

    def generate_token(self, request):
        raise NotImplementedError


class SecretBallotIpMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        return request.META['REMOTE_ADDR']
        # return ip address


class SecretBallotIpUseragentMiddleware(SecretBallotMiddleware):
    def generate_token(self, request):
        s = ''.join((request.META['REMOTE_ADDR'], request.META.get('HTTP_USER_AGENT', '')))
        return md5(s).hexdigest()

# Function to calculate token 
def retrieve_token(request):
    value=''.join((request.META['REMOTE_ADDR'], request.META.get('HTTP_USER_AGENT', '')))   
    token=md5(value).hexdigest()
    return token