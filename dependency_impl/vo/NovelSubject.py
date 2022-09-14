class NovelSubject:
    __slots__ = ['subject', 'detail_url']

    def __init__(self, subject: str, detail_url: str):
        self.subject = subject
        self.detail_url = detail_url

    def json_dict(self) -> dict:
        return {
            'subject': self.subject,
            'detail_url': self.detail_url
        }

    def __str__(self):
        return CommonComponent.json_dump(self.json_dict())
