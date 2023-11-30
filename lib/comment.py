class Comment:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, post_id, comment_content, author_name):
        self.id = id
        self.post_id = post_id
        self.comment_content = comment_content
        self.author_name = author_name

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Comment
    def __repr__(self):
        return f"Comment({self.id}, {self.post_id}, {self.comment_content}, {self.author_name})"

# | Record                | Properties                    |
# | --------------------- | ----------------------------- |
# | posts                 | title, content                |
# | comments              | post_id, content, author_name |