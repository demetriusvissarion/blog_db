# from lib.post_repository import PostRepository
# from lib.post import Post
# from lib.comment import Comment

# """
# When we call PostRepository#all
# We get a list of Post objects reflecting the seed data.
# """
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/blog.sql") # Seed our database with some test data
#     repository = PostRepository(db_connection) # Create a new PostRepository

#     posts = repository.all() # Get all posts

#     # Assert on the results
#     assert str(posts) == '[Post(1, Post_title_1, Post_content_1), Post(2, Post_title_2, Post_content_2), Post(3, Post_title_3, Post_content_3), Post(4, Post_title_4, Post_content_4)]'


# """
# When we call PostRepository#find
# We get a single Post object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/blog.sql")
#     repository = PostRepository(db_connection)

#     post = repository.find(3)
#     assert post == Post(3, 'Post_title_3', 'Post_content_3')

# def test_find_with_comments(db_connection):
#     db_connection.seed("seeds/blog.sql")
#     repository = PostRepository(db_connection)

#     post = repository.find_with_comments(1) # find post 1 and all comments
#     assert post == Post(1, 'Post_title_1', 'Post_content_1', [
#         Comment(1, 1, 'Comment_1', 'Author_1'),
#         Comment(2, 1, 'Comment_2', 'Author_2'),
#     ])

# # """
# # When we call PostRepository#create
# # We get a new record in the database.
# # """
# # def test_create_record(db_connection):
# #     db_connection.seed("seeds/blog.sql")
# #     repository = PostRepository(db_connection)

# #     repository.create(Post(None, "The Beatles", "Rock"))

# #     result = repository.all()
# #     assert result == [
# #         Post(1, "Pixies", "Rock"),
# #         Post(2, "ABBA", "Pop"),
# #         Post(3, "Taylor Swift", "Pop"),
# #         Post(4, "Nina Simone", "Jazz"),
# #         Post(5, "The Beatles", "Rock"),
# #     ]

# # """
# # When we call PostRepository#delete
# # We remove a record from the database.
# # """
# # def test_delete_record(db_connection):
# #     db_connection.seed("seeds/blog.sql")
# #     repository = PostRepository(db_connection)
# #     repository.delete(3) # Apologies to Taylor Swift fans

# #     result = repository.all()
# #     assert result == [
# #         Post(1, "Pixies", "Rock"),
# #         Post(2, "ABBA", "Pop"),
# #         Post(4, "Nina Simone", "Jazz"),
# #     ]

# # | Record                | Properties                    |
# # | --------------------- | ----------------------------- |
# # | posts                 | title, post_content                |
# # | comments              | post_id, comment_content, author_title |