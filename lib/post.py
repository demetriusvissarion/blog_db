class Post:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, post_content, comments = []):
        self.id = id
        self.title = title
        self.post_content = post_content
        self.comments = comments

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Post
    def __repr__(self):
        if len(self.comments) > 0:
            return f"Post({self.id}, {self.title}, {self.post_content}, {self.comments})"
        return f"Post({self.id}, {self.title}, {self.post_content})"

# | Record                | Properties                    |
# | --------------------- | ----------------------------- |
# | posts                 | title, content                |
# | comments              | post_id, content, author_name |