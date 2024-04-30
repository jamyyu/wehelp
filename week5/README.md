2-1:<br>
create database website;<br>
![2-1](https://github.com/jamyyu/wehelp_stage1/assets/103821947/b1d04494-8b9d-47e3-a594-a24c3e04df08
)<br>

2-2:<br>
use website;<br>
CREATE TABLE member(<br>
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',<br>
    name VARCHAR(255) NOT NULL COMMENT 'Name',<br>
    username VARCHAR(255) NOT NULL COMMENT 'Username',<br>
    password VARCHAR(255) NOT NULL COMMENT 'Password',<br>
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',<br>
    time datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'<br>
);<br>
![2-2](https://github.com/jamyyu/wehelp_stage1/assets/103821947/a50fa586-e6f0-4f6d-a3fd-b3f4bef383d3
)<br>

3-1:<br>
INSERT INTO member(id, name, username, password, follower_count, time) VALUES(1, 'test', 'test', 'test', 200, '2024-01-05 14:30:45');<br>
INSERT INTO member(name, username, password, follower_count, time) VALUES('Jon Snow', 'Jon', '123', 1000, '2024-03-05 13:05:25');<br>
INSERT INTO member(name, username, password, follower_count, time) VALUES('Arya Stark', 'Arya', '456', 1200, '2024-02-28 08:10:32');<br>
INSERT INTO member(name, username, password, follower_count, time) VALUES('Daenerys Targaryen', 'Mother of Dragons', '666', 1080, '2024-04-05 12:30:30');<br>
INSERT INTO member(name, username, password, follower_count, time) VALUES('Jaime Lannister', 'Jamie', '999', 1500, '2024-01-01 02:43:28');<br>
![3-1](https://github.com/jamyyu/wehelp_stage1/assets/103821947/b7987a9f-721a-4162-913e-c98d597c2088
)<br>

3-2:<br>
SELECT * FROM member;<br>
![3-2](https://github.com/jamyyu/wehelp_stage1/assets/103821947/46e0b005-8f04-413e-bdad-4ac4cf2446cd)<br>

3-3:<br>
SELECT * FROM member ORDER BY time DESC;<br>

