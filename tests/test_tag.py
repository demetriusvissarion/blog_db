from lib.tag import Tag

"""
Tag constructs with an id, title and content
"""
def test_tag_constructs():
    tag = Tag(1, "test tag")
    assert tag.tag_id == 1
    assert tag.tag_title == "test tag"

"""
We can format tags to strings nicely
"""
def test_tags_format_nicely():
    tag = Tag(1, "test tag")
    assert str(tag) == "Tag(1, test tag)"
    # Try commenting out the `__repr__` method in lib/tag.py
    # And see what happens when you run this test again.

"""
We can compare two identical tags
And have them be equal
"""
def test_tags_are_equal():
    tag1 = Tag(1, "test tag")
    tag2 = Tag(1, "test tag")
    assert tag1 == tag2
    # Try commenting out the `__eq__` method in lib/tag.py
    # And see what happens when you run this test again.
