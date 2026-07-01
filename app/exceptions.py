"""Domain exceptions, translated to HTTP responses by global handlers."""


class AppError(Exception):
    """Base class for all domain errors."""


class NotFoundError(AppError):
    """A requested resource does not exist."""


class ConflictError(AppError):
    """A resource conflicts with existing data (e.g. a duplicate)."""