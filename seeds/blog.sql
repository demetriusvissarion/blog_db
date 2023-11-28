DROP TABLE IF EXISTS posts;
-- Create the table without the foreign key first.
CREATE TABLE posts (
id SERIAL PRIMARY KEY,
title text,
content text
);

DROP TABLE IF EXISTS comments;
-- Then the table with the foreign key second.
CREATE TABLE comments (
id SERIAL PRIMARY KEY,
content text,
author_name text,
-- The foreign key name is always {other_table_singular}_id
post_id int,
constraint fk_post foreign key(post_id) 
    references posts(id) 
    on delete cascade
);