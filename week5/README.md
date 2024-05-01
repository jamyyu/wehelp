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
![3-3](https://github.com/jamyyu/wehelp_stage1/assets/103821947/0b0f6b9e-8b2f-4581-83db-fdca426632d3)<br>

3-4:<br>
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;<br>
![3-4](https://github.com/jamyyu/wehelp_stage1/assets/103821947/d5f75dd1-c7f7-481b-9fb3-de4e5e33d017)<br>

3-5:<br>
SELECT * FROM member WHERE username='test';<br>
![3-5](https://github.com/jamyyu/wehelp_stage1/assets/103821947/7e45baf9-6f28-44f9-9da0-eb843c3d02fd)<br>

3-6:<br>
SELECT * FROM member WHERE name LIKE '%es%';<br>
![3-6](https://github.com/jamyyu/wehelp_stage1/assets/103821947/e9e6513d-e332-4ed3-ab8c-3038309c0115)<br>

3-7:<br>
SELECT * FROM member WHERE username='test' and password='test';<br>
![3-7](https://github.com/jamyyu/wehelp_stage1/assets/103821947/0c03237a-ec43-4787-a27f-63b92fcfb9a3)<br>

3-8:<br>
UPDATE member SET name='test2' WHERE username='test';<br>
![3-8](https://github.com/jamyyu/wehelp_stage1/assets/103821947/bf5fa30a-9de8-465f-9727-0dcbedace909)<br>

4-1:<br>
SELECT COUNT(*) FROM member;<br>
![4-1](https://github.com/jamyyu/wehelp_stage1/assets/103821947/b47b2639-6188-4d14-a52b-b5f8278aad8d)<br>

4-2:<br>
SELECT SUM(follower_count) FROM member;<br>
![4-2](https://github.com/jamyyu/wehelp_stage1/assets/103821947/bfee4392-d7d4-47b5-a808-db9b3bdf1bf7)<br>

4-3:<br>
SELECT AVG(follower_count) FROM member;<br>
![4-3](https://github.com/jamyyu/wehelp_stage1/assets/103821947/e5c915dc-fb9a-49ca-b252-0e3af4e2bf19)<br>

4-4:<br>
SELECT AVG(follower_count) FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS top_two_avg;<br>
![4-4](https://github.com/jamyyu/wehelp_stage1/assets/103821947/b11ddda1-aa5c-4608-bf05-2c5b8240242c)<br>

5-1:<br>
CREATE TABLE message(<br>
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',<br>
    member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',<br>
    content VARCHAR(255) NOT NULL COMMENT 'Content',<br>
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',<br>
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',<br>
    FOREIGN KEY(member_id)<br>
    REFERENCES member(id)<br>
);<br>
![5-1](https://github.com/jamyyu/wehelp_stage1/assets/103821947/85baedf1-7e3d-4dbb-b256-16c2edc13894)<br>



 


