"""Exceptions for doppyler."""
from __future__ import annotations


class DopplerException(Exception):
    """Base Exception class for doppyler."""


class BadRequestException(DopplerException):
    """Raised when request was malformed."""


class UnauthorizedException(DopplerException):
    """Raised when request is unauthorized."""


class UnknownException(DopplerException):
    """Raised when unknown error occurs."""


class CantConnectException(DopplerException):
    """Raise when client can't connect to Doppler API."""


class ExpiredNonce(DopplerException):
    """Raise when nonce has expired and needs to be re-requested."""


class InvalidDataReturned(DopplerException):
    """Raise when HTTP response is OK but the data returned is invalid."""
