from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog.sql")

# Retrieve all posts
post_repository = PostRepository(connection)
posts = post_repository.all()

# # List them out
# for post in posts:
#     print(post)

# 2. Write a small program in `app.py` using the class `PostRepository` to print
#    out the data of one post with its comments to the terminal.
post_with_comments = post_repository.find_with_comments(2)
print(post_with_comments)