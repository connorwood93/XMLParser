DROP TABLE IF EXISTS food;
CREATE TABLE food (
    id serial primary key,
    item varchar(32) not null,
    price decimal not null,
    description varchar(50),
    calories int
);