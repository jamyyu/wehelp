-- MySQL dump 10.13  Distrib 8.3.0, for macos14 (arm64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'Unique ID',
  `name` varchar(255) NOT NULL COMMENT 'Name',
  `username` varchar(255) NOT NULL COMMENT 'Username',
  `password` varchar(255) NOT NULL COMMENT 'Password',
  `follower_count` int unsigned NOT NULL DEFAULT '0' COMMENT 'Follower Count',
  `time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time',
  PRIMARY KEY (`id`),
  KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',200,'2024-01-05 14:30:45'),(2,'Jon Snow','Jon','123',1000,'2024-03-05 13:05:25'),(3,'Arya Stark','Arya','456',1200,'2024-02-28 08:10:32'),(4,'Daenerys Targaryen','Mother of Dragons','666',1080,'2024-04-05 12:30:30'),(5,'Jaime Lannister','Jamie','999',1500,'2024-01-01 02:43:28'),(7,'Cersei Lannister','Cersei','0407',0,'2024-05-07 16:55:32'),(10,'麥考','cat','555',0,'2024-05-08 11:12:46'),(11,'米咕','meow','0228',0,'2024-05-09 18:59:09');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'Unique ID',
  `member_id` bigint NOT NULL COMMENT 'Member ID for Message Sender',
  `content` varchar(255) NOT NULL COMMENT 'Content',
  `like_count` int unsigned NOT NULL DEFAULT '0' COMMENT 'Like Count',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'Hello World',50,'2024-05-01 16:11:52'),(2,2,'Winter is coming',776,'2024-05-01 16:15:24'),(3,3,'Not today',893,'2024-05-01 16:20:27'),(4,4,'Dracarys',666,'2024-05-01 16:25:18'),(5,5,'If there are gods, why is the world so full of pain and injustice',888,'2024-05-01 16:33:42'),(6,1,'WeHelp',100,'2024-05-01 17:53:19'),(8,3,'麥考是大安區最可愛的貓',0,'2024-05-08 11:11:06'),(9,10,'ฅ^•ﻌ•^ฅ',0,'2024-05-08 11:14:25');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-09 19:15:38
