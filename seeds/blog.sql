DROP TABLE IF EXISTS posts CASCADE;
-- Create the table without the foreign key first.
CREATE TABLE posts (
id SERIAL PRIMARY KEY,
title text,
post_content text
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
INSERT INTO posts (title, post_content) VALUES ('Post_title_1', 'Post_content_1');
INSERT INTO posts (title, post_content) VALUES ('Post_title_2', 'Post_content_2');
INSERT INTO posts (title, post_content) VALUES ('Post_title_3', 'Post_content_3');
INSERT INTO posts (title, post_content) VALUES ('Post_title_4', 'Post_content_4');

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
-- | comments              | post_id, content, author_name |