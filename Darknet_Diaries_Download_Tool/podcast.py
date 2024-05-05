from __future__ import annotations
from collections import UserDict
from collections.abc import Mapping


class Podcast:
    """Information for each Darknet Diaries podcast."""

    def __init__(self) -> None:
        self.title: str
        self.ep_num: int
        self.author: str
        self.desc: str
        self.web_link: str
        self.dl_link: str

    def __repr__(self) -> str:
        return f'{type(self).__name__}()'

    def __str__(self) -> str:
        return f'{self.ep_num}: {self.title}'


class Podcasts(UserDict):
    """A dictionary object to store the podcast information in."""

    def __init__(self) -> None:
        self.podcast_dict: Mapping = {}

    def __repr__(self) -> str:
        return f'{type(self).__name__}()'

    def __str__(self) -> str:
        return 'Podcast Dictionary'


class PodcastTool:
    """Get the data from the xml page and populate the podcasts dictionary. 
    """

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'{type(self).__name__}()'

    def __str__(self) -> str:
        return 'Podcast Tool'
