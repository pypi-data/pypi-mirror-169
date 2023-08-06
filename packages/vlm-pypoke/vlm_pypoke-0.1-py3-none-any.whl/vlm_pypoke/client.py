import requests
from typing import Any, Dict, Optional
from .error import PokeError


class PokeClient:
    """
    A client for the PokeAPI.
    
    Contains only the methods needed for this project.
    - /pokemon/
    - /pokemon-species/
    """

    _base_url = 'https://pokeapi.co/api/v2/'

    def get_pokemon(
        self, 
        name: Optional[str] = None, 
        id: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Get pokemon information

        /pokemon/{id or name}/

        :param name: Pokemon name, defaults to ""
        :type name: str, optional
        :param id: Pokemon ID, defaults to None
        :type id: int, optional
        :raises ValueError: You must provide a pokemon name or an id
        :raises PokeError: Pokemon not found
        :return: Pokemon information
        :rtype: Dict[str, Any]
        """
        if name and not id:
            payload = name
        elif id and not name:
            payload = id
        else:
            raise ValueError("You must provide a pokemon name or an id")

        url = f"{self._base_url}pokemon/{payload}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise PokeError(response.status_code, "Pokemon not found")

    def get_pokemon_species(
        self, 
        name: Optional[str] = None, 
        id: int = None
    ) -> Dict[str, Any]:
        """
        Get pokemon species information

        /pokemon-species/{id or name}/

        :param name: Pokemon name, defaults to ""
        :type name: str, optional
        :param id: Pokemon ID, defaults to None
        :type id: int, optional
        :raises ValueError: You must provide a pokemon name or an id
        :raises PokeError: Pokemon Species not found
        :return: Pokemon species information
        :rtype: Dict[str, Any]
        """
        if name and not id:
            payload = name
        elif id and not name:
            payload = id
        else:
            raise ValueError("You must provide a pokemon name or an id")

        url = f"{self._base_url}pokemon-species/{payload}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise PokeError(response.status_code, "Pokemon Species not found")