DROP TABLE IF EXISTS posts CASCADE;
-- Create the table without the foreign key first.
CREATE TABLE posts (
id SERIAL PRIMARY KEY,
title text,
post_content text
);

DROP TABLE IF EXISTS tags CASCADE;
CREATE TABLE tags (
tag_id SERIAL PRIMARY KEY,
tag_title VARCHAR(255)
);

DROP TABLE IF EXISTS posts_tags CASCADE;
CREATE TABLE posts_tags (
post_id int4,
tag_id int4
);

DROP TABLE IF EXISTS comments;
-- Then the table with the foreign key second.
CREATE TABLE comments (
id SERIAL PRIMARY KEY,
-- The foreign key name is always {other_table_singular}_id
post_id int,
constraint fk_post foreign key(post_id) 
    references posts(id) 
    on delete cascade,
comment_content text,
author_name text
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, post_content) VALUES ('How to use Git', 'Post_content_1');
INSERT INTO posts (title, post_content) VALUES ('Fun classes', 'Post_content_2');
INSERT INTO posts (title, post_content) VALUES ('Using a REPL', 'Post_content_3');
INSERT INTO posts (title, post_content) VALUES ('My weekend in Edinburgh', 'Post_content_4');
INSERT INTO posts (title, post_content) VALUES ('The best chocolate cake EVER', 'Post_content_5');
INSERT INTO posts (title, post_content) VALUES ('A foodie week in Spain', 'Post_content_6');
INSERT INTO posts (title, post_content) VALUES ('SQL basics', 'Post_content_7');


INSERT INTO tags (tag_title) VALUES ('coding');
INSERT INTO tags (tag_title) VALUES ('travel');
INSERT INTO tags (tag_title) VALUES ('cooking');
INSERT INTO tags (tag_title) VALUES ('education');


INSERT INTO posts_tags (post_id, tag_id) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 2),
(7, 1),
(6, 3),
(2, 4),
(3, 4);

ALTER TABLE posts_tags ADD FOREIGN KEY (tag_id) REFERENCES tags(tag_id);
ALTER TABLE posts_tags ADD FOREIGN KEY (post_id) REFERENCES posts(post_id);


INSERT INTO comments (post_id, comment_content, author_name) VALUES (1, 'Comment_1', 'Author_1');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (1, 'Comment_2', 'Author_2');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (2, 'Comment_3', 'Author_3');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (2, 'Comment_4', 'Author_1');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (3, 'Comment_5', 'Author_1');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (3, 'Comment_6', 'Author_1');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (3, 'Comment_7', 'Author_1');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (3, 'Comment_8', 'Author_1');
INSERT INTO comments (post_id, comment_content, author_name) VALUES (4, 'Comment_9', 'Author_1');

-- | Record                | Properties                    |
-- | --------------------- | ----------------------------- |
-- | posts                 | title, content                |
-- | tags                  | tag_id, tag_title             |
-- | posts_tags            | post_id, tag_id               |
-- | comments              | post_id, content, author_name |