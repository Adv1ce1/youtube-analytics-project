import pytest
import json
from src.channel import Channel
from src.video import Video, PLVideo
from src.config import CHANNEL_ID, CHANNEL_ID_SECOND
from src.playlist import PlayList


@pytest.fixture
def channel():
    channel = Channel(CHANNEL_ID)
    return channel


@pytest.fixture
def channel_second():
    channel = Channel(CHANNEL_ID_SECOND)
    return channel


@pytest.fixture
def channel_info():
    return json.dumps({
        "kind": "youtube#channelListResponse",
        "etag": "uAdmwT0aDhY9LmAzJzIafD6ATRw",
        "pageInfo": {
            "totalResults": 1,
            "resultsPerPage": 5
        },
        "items": [
            {
                "kind": "youtube#channel",
                "etag": "cPh7A8SKcZxxs_UPCiBaXP1wNDk",
                "id": "UC-OVMPlMA3-YCIeg4z5z23A",
                "snippet": {
                    "title": "MoscowPython",
                    "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
                    "customUrl": "@moscowdjangoru",
                    "publishedAt": "2012-07-13T09:48:44Z",
                    "thumbnails": {
                        "default": {
                            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",
                            "width": 88,
                            "height": 88
                        },
                        "medium": {
                            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",
                            "width": 240,
                            "height": 240
                        },
                        "high": {
                            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",
                            "width": 800,
                            "height": 800
                        }
                    },
                    "localized": {
                        "title": "MoscowPython",
                        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
                    },
                    "country": "RU"
                },
                "statistics": {
                    "viewCount": "2303120",
                    "subscriberCount": "25900",
                    "hiddenSubscriberCount": False,
                    "videoCount": "685"
                }
            }
        ]
    })


@pytest.fixture
def video():
    return Video("AWX4JnAnjBE")


@pytest.fixture
def pl_video():
    return PLVideo("4fObz_qw9u4", "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC")


@pytest.fixture
def playlist():
    playlist = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    return playlist
@pytest.fixture
def duration(playlist):
    return playlist.total_duration