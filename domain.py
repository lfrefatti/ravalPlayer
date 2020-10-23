class Song:
    
    def __init__(self, track_name, artists, link):
        self.track_name = track_name
        self.artists = artists
        self.link = link


class PlaylistEntry:
    
    def __init__(self, title, _file, howl = 'null'):
        self.title = title
        self.file = _file
        self.howl = howl

    def __repr__(self):
        return str(self.__dict__)