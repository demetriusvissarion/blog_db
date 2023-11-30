from lib.comment import Comment

"""
Comment constructs with an post_id, content and author_name
"""
def test_comment_constructs():
    comment = Comment(1, 1, "Test Content", 'Test Author')
    assert comment.id == 1
    assert comment.post_id == 1
    assert comment.comment_content == "Test Content"
    assert comment.author_name == 'Test Author'

"""
We can format comments to strings nicely
"""
def test_comments_format_nicely():
    comment = Comment(1, 1, "Test Content", 'Test Author')
    assert str(comment) == "Comment(1, 1, Test Content, Test Author)"
    # Try commenting out the `__repr__` method in lib/comment.py
    # And see what happens when you run this test again.

"""
We can compare two identical comments
And have them be equal
"""
def test_comments_are_equal():
    comment1 = Comment(1, 1, "Test Content", 'Test Author')
    comment2 = Comment(1, 1, "Test Content", 'Test Author')
    assert comment1 == comment2
    # Try commenting out the `__eq__` method in lib/comment.py
    # And see what happens when you run this test again.
