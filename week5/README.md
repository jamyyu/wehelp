2-1:</br>
create database website;</br>
![2-1](https://github.com/jamyyu/wehelp_stage1/assets/103821947/b1d04494-8b9d-47e3-a594-a24c3e04df08
)</br>

2-2:</br>
use website;</br>
CREATE TABLE member(
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',</br>
    name VARCHAR(255) NOT NULL COMMENT 'Name',</br>
    username VARCHAR(255) NOT NULL COMMENT 'Username',</br>
    password VARCHAR(255) NOT NULL COMMENT 'Password',</br>
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',</br>
    time datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'</br>
);</br>
![2-2](https://github.com/jamyyu/wehelp_stage1/assets/103821947/a50fa586-e6f0-4f6d-a3fd-b3f4bef383d3
)</br>
