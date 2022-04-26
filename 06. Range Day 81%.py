class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pass

    def add_photos(self, label):
        for r in range(self.pages):
            for c in range(4):
                if self.photos[r][c] == "":
                    self.photos[r][c] = label
    def pr(self):
        return self.photos

p = PhotoAlbum(3)
p.add_photos("ivan")
print(p.pr())




p = PhotoAlbum(4)