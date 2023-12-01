class Tag:
    def __init__(self, tag_id, tag_title):
        self.tag_id = tag_id
        self.tag_title = tag_title

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Tag({self.tag_id}, {self.tag_title})"
    

# -- | Record                | Properties                    |
# -- | --------------------- | ----------------------------- |
# -- | posts                 | title, content                |
# -- | tags                  | tag_id, tag_title             |
# -- | posts_tags            | post_id, tag_id               |
# -- | comments              | post_id, content, author_name |