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
# post_with_comments = post_repository.find_with_comments(2)
# print(post_with_comments)

# Phase Three: 05
# In this exercise, you will build on your `PostRepository` by adding a method
# called `find_by_tag`, which will find all posts with a particular tag.
# The array `posts` should contain the following Post objects:
#  * 1  How to use Git
#  * 2  Python classes
#  * 3  Using a Python REPL
#  * 7  SQL basics
posts = post_repository.find_by_tag('coding')
print(posts)