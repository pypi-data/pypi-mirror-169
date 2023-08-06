from typing import Any, Dict, Optional
from datetime import datetime, timedelta

from .memo_item import PyMemoItem


class PyMemoCollection:
    '''The base class that stores a collection of memoized values.

    This class stores and manages the access to the items that has a valid
    memoized value.

    Attributes
    ----------
    expiration_interval : float, None
        The expiration interval in seconds
    length : int
        The quantity of items in the collection

    Methods
    -------
    set_item(key, value, expires_at=None, expiration_interval=None)
        Defines a new item in the collection. If the key already exists the
        value will be overwritten.
    get_item(key)
        Gets the item value stored in the collection based on the key
    delete_item(key)
        Deletes the item stored in the collection based on the key
    clear(only_expired_items=True)
        Cleans all the collection or removes only expired items
    '''
    __slots__ = [
        '_expiration_interval',
        '_collection',
    ]

    def __init__(self, expiration_interval: Optional[float] = None) -> None:
        '''
        Parameters
        ----------
        expiration_interval : float, optional
            The default expiration interval in seconds of all items added to the
            collection (default is None, indicating that it will never expire).
        '''
        self._expiration_interval = expiration_interval
        self._collection: Dict[str, PyMemoItem] = {}

    @property
    def expiration_interval(self):
        '''The expiration interval in seconds.

        Returns
        -------
        float
            The expiration interval
        '''
        return self._expiration_interval

    @expiration_interval.setter
    def expiration_interval(self, expiration_interval: Optional[float]):
        '''Update the default expiration interval of the collection.

        Parameters
        ----------
        expiration_interval : float, None
            The default expiration interval in seconds of all items added to the
            collection. If None new itens will never expire.
        '''
        self._expiration_interval = expiration_interval

    @property
    def length(self):
        '''The quantity of items in the collection.

        Returns
        -------
        int
            The quantity of items in the collection
        '''
        return len(self._collection)

    def set_item(
            self, key: str, value: Any, expires_at: Optional[datetime] = None,
            expiration_interval: Optional[float] = None) -> None:
        '''Defines a new item in the collection. If the key already exists the
        value will be overwritten.

        If the `expires_at`, `expiration_interval` or the collection haven't a
        default expiration interval value, the item never expire.

        Parameters
        ----------
        key : str
            The key of the item in the collection
        value : Any
            The value that will be stored
        expires_at : datetime, optional
            The expiration date and time of the value (default is None)
        expiration_interval : float, optional
            The expiration interval in seconds of the item added to the collection
            (default is None).
        '''
        expiration_interval = expiration_interval if (
            bool(expiration_interval)) else self._expiration_interval

        if not expires_at and bool(expiration_interval):
            expires_at = datetime.now() + timedelta(seconds=expiration_interval)
        self._collection[key] = PyMemoItem(value, expires_at)

    def get_item(self, key: str) -> Any:
        '''Gets the item value stored in the collection based on the key.

        Parameters
        ----------
        key : str
            The key of the item in the collection

        Returns
        -------
        None
            If the cache is invalid
        Any
            The value stored if has valid cache
        '''
        try:
            return self._collection[key].value
        except KeyError:
            return None
        finally:
            self.clear()

    def delete_item(self, key: str) -> None:
        '''Deletes the item stored in the collection based on the key.

        Parameters
        ----------
        key : str
            The key of the item in the collection
        '''
        if key in self._collection:
            del self._collection[key]

    def clear(self, only_expired_items=True) -> None:
        '''Cleans all the collection or removes only expired items.

        Parameters
        ----------
        only_expired_items : bool
            The boolean that indicates which items will be removed (default is True)
        '''
        if only_expired_items:
            for key, item in self._collection.copy().items():
                if not item.has_valid_cache():
                    self.delete_item(key)
        else:
            self._collection = {}
