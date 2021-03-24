from rest_framework.throttling import UserRateThrottle

class KamalThrottle(UserRateThrottle):
    scope='kamal'