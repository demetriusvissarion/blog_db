from lib.post import Post

"""
Post constructs with an id, title and content
"""
def test_post_constructs():
    post = Post(1, "Quisque", "Quisque at efficitur libero.")
    assert post.id == 1
    assert post.title == "Quisque"
    assert post.post_content == "Quisque at efficitur libero."

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Quisque", "Quisque at efficitur libero.")
    assert str(post) == "Post(1, Quisque, Quisque at efficitur libero.)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Quisque", "Quisque at efficitur libero.")
    post2 = Post(1, "Quisque", "Quisque at efficitur libero.")
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/post.py
    # And see what happens when you run this test again.
