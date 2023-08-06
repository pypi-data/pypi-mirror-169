# -*- coding: utf-8 -*-

"""
This module define all Exceptions for GDetect.
GDetectError is for all external call.
All other exceptions are for internal use.
"""


class GDetectError(BaseException):
    """global error for external return"""


class NoAuthenticateToken(ValueError):
    """no token to authentication exists"""


class BadAuthenticationToken(ValueError):
    """given token has bad format"""


class NoURL(ValueError):
    """no URL to API found"""


class UnauthorizedAccess(ValueError):
    """access to API is unauthorized"""


class BadUUID(ValueError):
    """given UUID is wrong"""


class BadSHA256(ValueError):
    """given SHA256 hash is wrong"""


class MissingToken(KeyError):
    """Missing token field in result"""


class MissingSID(KeyError):
    """Missing file sid field in result"""


class MissingResponse(AttributeError):
    """Missing response from api client"""
