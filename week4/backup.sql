-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: assignment
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `author` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author` (`author`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`author`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'spy_family0','spy_story',1),(2,'spy_family1','spy_story',1),(3,'spy_family2','spy_story',1),(4,'spy_family3','spy_story',1),(5,'spy_family4','spy_story',1),(6,'sozounofuriren2','adventure',2),(7,'sozounofuriren4','adventure',4),(8,'sozounofuriren6','adventure',6),(9,'sozounofuriren8','adventure',8),(10,'oshinoko9','idol',9),(11,'oshinoko10','idol',10),(12,'oshinoko11','idol',11),(13,'oshinoko12','idol',12),(14,'oshinoko13','idol',13),(15,'oshinoko14','idol',14),(16,'naruto15','honokage',15),(17,'naruto15','honokage',15),(18,'naruto15','honokage',15),(19,'naruto15','honokage',15),(20,'naruto15','honokage',15),(21,'naruto15','honokage',15),(22,'naruto15','honokage',15),(23,'naruto15','honokage',15),(24,'kyojin16','honokage',16),(25,'kyojin17','honokage',17),(26,'kyojin18','honokage',18),(27,'kyojin19','honokage',19),(28,'86-20','revenge',20),(29,'86-21','revenge',20),(30,'86-22','revenge',20);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Ramya@gmail','1234'),(2,'anya0@gmail','1234'),(3,'anya1@gmail','1234'),(4,'anya2@gmail','1234'),(5,'anya3@gmail','1234'),(6,'anya4@gmail','1234'),(7,'anya5@gmail','1234'),(8,'anya6@gmail','1234'),(9,'anya7@gmail','1234'),(10,'anya8@gmail','1234'),(11,'anya9@gmail','1234'),(12,'anya10@gmail','1234'),(13,'anya11@gmail','1234'),(14,'anya12@gmail','1234'),(15,'anya13@gmail','1234'),(16,'anya14@gmail','1234'),(17,'anya15@gmail','1234'),(18,'anya16@gmail','1234'),(19,'anya17@gmail','1234'),(20,'anya18@gmail','1234'),(21,'anya19@gmail','1234'),(22,'anya20@gmail','1234'),(23,'anya21@gmail','1234'),(24,'anya22@gmail','1234'),(25,'anya23@gmail','1234'),(26,'anya24@gmail','1234'),(27,'anya25@gmail','1234'),(28,'anya26@gmail','1234'),(29,'anya27@gmail','1234'),(30,'anya28@gmail','1234'),(31,'anya29@gmail','1234');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-02 22:02:40
