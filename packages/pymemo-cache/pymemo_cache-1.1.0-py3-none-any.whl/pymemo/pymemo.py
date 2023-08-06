from typing import Dict, Optional

from .memo_collection import PyMemoCollection


class PyMemo:
    '''The main class that centralize all collections of memoized items.

    This class stores and manages all collections of memoized items.

    Attributes
    ----------
    length : int
        The quantity of collections

    Methods
    -------
    create_collection(name, expiration_interval=None)
        Creates a collection if it doesn't exist and returns it
    collection(name)
        Gets an existing collection
    delete_collection(name)
        Deletes an collection
    clear_collections(only_expired_items=True)
        Cleans all the collections items or removes only expired items
    '''
    __slots__ = [
        '_collections',
    ]

    def __init__(self) -> None:
        self._collections: Dict[str, PyMemoCollection] = {}

    def __str__(self):
        result = [f'Total collections: {self.length}\n']
        for name, collection in self._collections.items():
            result.append(f'{name} ─ Total items: {collection.length}')
        return '\n'.join(result)

    @property
    def length(self):
        '''The quantity of collections.

        Returns
        -------
        int
            The quantity of collections
        '''
        return len(self._collections)

    def create_collection(
            self, name: str,
            expiration_interval: Optional[int] = None) -> PyMemoCollection:
        '''Creates a collection if it doesn't exist and returns it.

        Parameters
        ----------
        name : str
            The name of the collection
        expiration_interval : float, optional
            The default expiration interval in seconds of the collection
            (default is None).
        
        Returns
        -------
        PyMemoCollection
            The collection created
        '''
        if name not in self._collections:
            self._collections[name] = PyMemoCollection(expiration_interval)
        return self._collections[name]

    def collection(self, name: str) -> PyMemoCollection:
        '''Gets an existing collection.

        Parameters
        ----------
        name : str
            The name of the collection
        
        Returns
        -------
        PyMemoCollection
            An existing collection
        None
            If the collection doesn't exist
        '''
        try:
            return self._collections[name]
        except KeyError:
            return None

    def delete_collection(self, name: str) -> None:
        '''Deletes an collection.

        Parameters
        ----------
        name : str
            The name of the collection
        '''
        if name in self._collections:
            del self._collections[name]

    def clear_collections(self, only_expired_items=True) -> None:
        '''Cleans all the collections items or removes only expired items.

        Parameters
        ----------
        only_expired_items : bool
            The boolean that indicates which items will be removed (default is True)
        '''
        for collection in self._collections.values():
            collection.clear(only_expired_items)
