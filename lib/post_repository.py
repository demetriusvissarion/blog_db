from lib.post import Post
from lib.comment import Comment

class PostRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all posts
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["post_content"])
            posts.append(item)
        return posts
    
    # Find a single post by their id
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["post_content"])

    # Find a single post with its comments
    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            "SELECT posts.id as post_id, posts.title, posts.post_content, comments.id as comment_id, comments.comment_content, comments.author_name  " \
            "FROM posts JOIN comments ON posts.id = comments.post_id " \
            "WHERE posts.id = %s", [post_id])
        comments = []
        for row in rows:
            comment = Comment(row["comment_id"], row["post_id"], row["comment_content"], row["author_name"])
            comments.append(comment)

        # Each row has the same id, cohort_name, and starting_date, so we just use the first
        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)

    # # Create a new post
    # # Do you want to get its id back? Look into RETURNING id;
    # def create(self, post):
    #     self._connection.execute('INSERT INTO posts (title, content) VALUES (%s, %s)', [post.title, post.content])
    #     return None

    # # Delete an post by their id
    # def delete(self, post_id):
    #     self._connection.execute(
    #         'DELETE FROM posts WHERE id = %s', [post_id])
    #     return None

# | Record                | Properties                    |
# | --------------------- | ----------------------------- |
# | posts                 | title, content                |
# | comments              | post_id, content, author_title |

