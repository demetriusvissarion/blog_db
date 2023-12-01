# Repository classes with many-to-many relationships

Learn to design Repository classes using many-to-many relationships.

## Intro

In this exercise, you will build on your `PostRepository` by adding a method
called `find_by_tag`, which will find all posts with a particular tag.

Here is how it should work:

```python
post_repository = PostRepository()

posts = post_repository.find_by_tag('coding')

# The array `posts` should contain the following Post objects:
#
#  * 1  How to use Git
#  * 2  Python classes
#  * 3  Using a Python REPL
#  * 7  SQL basics
```

| Method        | Job                              | Arguments      | SQL query          | Returns         |
| ------------- | -------------------------------- | -------------- | ------------------ | --------------- |
| `find_by_tag` | Find all posts for the given tag | A tag (string) | `SELECT ... JOIN ` | Array of `Post` |

<!-- OMITTED -->

## Exercise 

Set up a new project `blog` for this exercise.

Test-drive and implement Model and Repository classes for the table `posts`,
with the method `PostRepository#find_by_tag` having the behaviour described
above.


Action plan:
 - use existing "blog" project
 - edit the blog.sql to add 'tags' table and the join table 'posts_tags' + new fake data
 psql -h 127.0.0.1 blog < seeds/blog.sql
 - TDD 'Tag' class
 - TDD edit 'PostRepository' class for new method find_by_tag