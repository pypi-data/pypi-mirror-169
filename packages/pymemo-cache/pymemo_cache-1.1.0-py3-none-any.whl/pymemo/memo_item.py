from typing import Any, Optional, Union
from datetime import datetime


class PyMemoItem:
    '''The base class that stores a memoized value.

    This class stores and manages whether the item has a valid memoized value.

    Attributes
    ----------
    value : Any, None
        The value that will be stored

    Methods
    -------
    has_valid_cache()
        Checks if the cache is valid based on the expiration time
    '''
    __slots__ = [
        '_value',
        '_expires_at',
    ]

    def __init__(
            self, value: Any, expires_at: Optional[datetime] = None) -> None:
        '''
        Parameters
        ----------
        value : Any
            The value that will be stored
        expires_at : datetime, optional
            The expiration date and time of the value (default is None, indicating
            that it never expire).
        '''
        self._value = value
        self._expires_at = expires_at

    @property
    def value(self) -> Union[Any, None]:
        '''The stored value.

        Returns
        -------
        None
            If the cache is invalid
        Any
            The value stored if has valid cache
        '''
        if not self.has_valid_cache():
            return None
        return self._value

    def has_valid_cache(self) -> bool:
        '''Checks if the cache is valid based on the expiration time.
        
        Returns
        -------
        bool
            A boolean that indicates if the cache is valid
        '''
        if not bool(self._expires_at):
            return True
        return datetime.now() <= self._expires_at
