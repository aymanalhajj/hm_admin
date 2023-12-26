-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hm_db
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Employee Role',7,'add_employeerole'),(26,'Can change Employee Role',7,'change_employeerole'),(27,'Can delete Employee Role',7,'delete_employeerole'),(28,'Can view Employee Role',7,'view_employeerole'),(29,'Can add Order Status',8,'add_orderstatus'),(30,'Can change Order Status',8,'change_orderstatus'),(31,'Can delete Order Status',8,'delete_orderstatus'),(32,'Can view Order Status',8,'view_orderstatus'),(33,'Can add Organization',9,'add_organization'),(34,'Can change Organization',9,'change_organization'),(35,'Can delete Organization',9,'delete_organization'),(36,'Can view Organization',9,'view_organization'),(37,'Can add Organization Type',10,'add_organizationtype'),(38,'Can change Organization Type',10,'change_organizationtype'),(39,'Can delete Organization Type',10,'delete_organizationtype'),(40,'Can view Organization Type',10,'view_organizationtype'),(41,'Can add Service Section',11,'add_servicesection'),(42,'Can change Service Section',11,'change_servicesection'),(43,'Can delete Service Section',11,'delete_servicesection'),(44,'Can view Service Section',11,'view_servicesection'),(45,'Can add Service Type',12,'add_servicetype'),(46,'Can change Service Type',12,'change_servicetype'),(47,'Can delete Service Type',12,'delete_servicetype'),(48,'Can view Service Type',12,'view_servicetype'),(49,'Can add Organization Service',13,'add_organizationservice'),(50,'Can change Organization Service',13,'change_organizationservice'),(51,'Can delete Organization Service',13,'delete_organizationservice'),(52,'Can view Organization Service',13,'view_organizationservice'),(53,'Can add Organization Employee',14,'add_organizationemployee'),(54,'Can change Organization Employee',14,'change_organizationemployee'),(55,'Can delete Organization Employee',14,'delete_organizationemployee'),(56,'Can view Organization Employee',14,'view_organizationemployee'),(57,'Can add Order Stage',15,'add_orderstage'),(58,'Can change Order Stage',15,'change_orderstage'),(59,'Can delete Order Stage',15,'delete_orderstage'),(60,'Can view Order Stage',15,'view_orderstage'),(61,'Can add Service Section Employee',16,'add_servicesectionemployee'),(62,'Can change Service Section Employee',16,'change_servicesectionemployee'),(63,'Can delete Service Section Employee',16,'delete_servicesectionemployee'),(64,'Can view Service Section Employee',16,'view_servicesectionemployee'),(65,'Can add User Type',17,'add_usertype'),(66,'Can change User Type',17,'change_usertype'),(67,'Can delete User Type',17,'delete_usertype'),(68,'Can view User Type',17,'view_usertype'),(69,'Can add User Account',18,'add_useraccount'),(70,'Can change User Account',18,'change_useraccount'),(71,'Can delete User Account',18,'delete_useraccount'),(72,'Can view User Account',18,'view_useraccount'),(73,'Can add Geo Location',19,'add_geolocation'),(74,'Can change Geo Location',19,'change_geolocation'),(75,'Can delete Geo Location',19,'delete_geolocation'),(76,'Can view Geo Location',19,'view_geolocation'),(77,'Can add organization visit',20,'add_organizationvisit'),(78,'Can change organization visit',20,'change_organizationvisit'),(79,'Can delete organization visit',20,'delete_organizationvisit'),(80,'Can view organization visit',20,'view_organizationvisit'),(81,'Can add Visit Status',21,'add_visitstatus'),(82,'Can change Visit Status',21,'change_visitstatus'),(83,'Can delete Visit Status',21,'delete_visitstatus'),(84,'Can view Visit Status',21,'view_visitstatus');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$mEHtD8KUR3mMZIWdzSl57U$wyNc9IOuNUamIn406TuI80bok4Z1yJUrPNAzUBZs1nk=','2023-12-24 05:30:24.363025',1,'admin','','','admin@gmail.com',1,1,'2023-12-19 11:15:51.410746');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_auth_useraccount`
--

DROP TABLE IF EXISTS `custom_auth_useraccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `custom_auth_useraccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `second_name` varchar(100) NOT NULL,
  `third_name` varchar(100) NOT NULL,
  `fourth_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `custom_auth_useracco_type_id_107be9e4_fk_custom_au` (`type_id`),
  CONSTRAINT `custom_auth_useracco_type_id_107be9e4_fk_custom_au` FOREIGN KEY (`type_id`) REFERENCES `custom_auth_usertype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_auth_useraccount`
--

LOCK TABLES `custom_auth_useraccount` WRITE;
/*!40000 ALTER TABLE `custom_auth_useraccount` DISABLE KEYS */;
INSERT INTO `custom_auth_useraccount` VALUES (1,'علي','','','','الحسيني','','0532222222','ali','ali',1),(2,'خالد','','','','خالد','','0532222222','khalid','khalid',3),(3,'احمد','','','','الحسيني','','0532222222','ahmed','ahmed',2);
/*!40000 ALTER TABLE `custom_auth_useraccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_auth_usertype`
--

DROP TABLE IF EXISTS `custom_auth_usertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `custom_auth_usertype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_auth_usertype`
--

LOCK TABLES `custom_auth_usertype` WRITE;
/*!40000 ALTER TABLE `custom_auth_usertype` DISABLE KEYS */;
INSERT INTO `custom_auth_usertype` VALUES (1,'مندوب'),(2,'مهندس'),(3,'مشرف');
/*!40000 ALTER TABLE `custom_auth_usertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-19 11:16:26.674086','1','مندوب',1,'[{\"added\": {}}]',17,1),(2,'2023-12-19 11:16:35.664251','2','مهندس',1,'[{\"added\": {}}]',17,1),(3,'2023-12-19 11:16:41.487521','3','مسرف',1,'[{\"added\": {}}]',17,1),(4,'2023-12-19 11:16:58.639646','1','يحتاج الآن',1,'[{\"added\": {}}]',8,1),(5,'2023-12-19 11:17:13.368489','2','تحديد تاريخ',1,'[{\"added\": {}}]',8,1),(6,'2023-12-19 11:17:18.164937','3','محتمل',1,'[{\"added\": {}}]',8,1),(7,'2023-12-19 11:17:33.407445','1','مالك',1,'[{\"added\": {}}]',7,1),(8,'2023-12-19 11:17:38.502099','2','مدير',1,'[{\"added\": {}}]',7,1),(9,'2023-12-19 11:17:42.774542','3','موظف',1,'[{\"added\": {}}]',7,1),(10,'2023-12-19 11:18:45.569247','1','علي  الحسيني',1,'[{\"added\": {}}]',18,1),(11,'2023-12-19 11:19:09.104802','1','أنظمة امن',1,'[{\"added\": {}}]',11,1),(12,'2023-12-19 11:19:16.559987','2','أنظمة سلامة',1,'[{\"added\": {}}]',11,1),(13,'2023-12-19 11:19:31.753236','3','مصاعد',1,'[{\"added\": {}}]',11,1),(14,'2023-12-19 11:20:19.923899','1','برج',1,'[{\"added\": {}}]',10,1),(15,'2023-12-19 11:20:26.903100','2','مركز تجاري',1,'[{\"added\": {}}]',10,1),(16,'2023-12-19 11:20:42.158589','1','تركيب',1,'[{\"added\": {}}]',12,1),(17,'2023-12-19 11:20:47.144698','2','صيانة',1,'[{\"added\": {}}]',12,1),(18,'2023-12-19 11:20:52.091709','3','اعطال',1,'[{\"added\": {}}]',12,1),(19,'2023-12-19 11:21:26.679512','1','أنظمة امن',1,'[{\"added\": {}}]',16,1),(20,'2023-12-19 11:21:40.918919','2','أنظمة سلامة',1,'[{\"added\": {}}]',16,1),(21,'2023-12-19 11:32:20.986105','1','جديد',1,'[{\"added\": {}}]',15,1),(22,'2023-12-19 11:33:08.565102','1','هامة المدن',1,'[{\"added\": {}}]',9,1),(23,'2023-12-19 11:33:26.506420','1','OrganizationService object (1)',1,'[{\"added\": {}}]',13,1),(24,'2023-12-20 06:28:49.452405','2','خالد  خالد',1,'[{\"added\": {}}]',18,1),(25,'2023-12-20 06:29:24.604813','3','احمد  الحسيني',1,'[{\"added\": {}}]',18,1),(26,'2023-12-20 06:29:33.167115','2','خالد  خالد',2,'[{\"changed\": {\"fields\": [\"User type\"]}}]',18,1),(27,'2023-12-20 06:39:14.518952','1','أنظمة امن',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(28,'2023-12-20 06:39:59.092350','2','OrganizationService object (2)',1,'[{\"added\": {}}]',13,1),(29,'2023-12-20 06:40:09.057444','3','OrganizationService object (3)',1,'[{\"added\": {}}]',13,1),(30,'2023-12-20 07:34:00.000081','3','مصاعد',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(31,'2023-12-20 07:34:28.048897','2','أنظمة سلامة',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(32,'2023-12-20 09:57:32.222661','1','الموقع (38.6299047, 24.4780239)',1,'[{\"added\": {}}]',19,1),(33,'2023-12-21 04:28:45.656767','2','أنظمة سلامة',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(34,'2023-12-21 04:29:02.161397','1','أنظمة امن',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(35,'2023-12-21 04:47:50.302053','1','تم الإتفاق',1,'[{\"added\": {}}]',21,1),(36,'2023-12-21 04:48:15.756901','2','لم يتم الإتفاق',1,'[{\"added\": {}}]',21,1),(37,'2023-12-21 05:02:55.239243','10','OrganizationVisit object (10)',2,'[{\"changed\": {\"fields\": [\"Service section\"]}}]',20,1),(38,'2023-12-21 05:03:23.590000','10','OrganizationVisit object (10)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\"]}}]',20,1),(39,'2023-12-21 05:03:37.908515','10','OrganizationVisit object (10)',3,'',20,1),(40,'2023-12-21 05:03:37.965172','9','OrganizationVisit object (9)',3,'',20,1),(41,'2023-12-21 05:03:37.972677','8','OrganizationVisit object (8)',3,'',20,1),(42,'2023-12-21 05:03:37.980736','7','OrganizationVisit object (7)',3,'',20,1),(43,'2023-12-21 05:03:37.980736','6','OrganizationVisit object (6)',3,'',20,1),(44,'2023-12-21 05:03:37.988687','5','OrganizationVisit object (5)',3,'',20,1),(45,'2023-12-21 05:03:37.996687','4','OrganizationVisit object (4)',3,'',20,1),(46,'2023-12-21 05:03:38.005826','3','OrganizationVisit object (3)',3,'',20,1),(47,'2023-12-21 05:03:38.008723','2','OrganizationVisit object (2)',3,'',20,1),(48,'2023-12-21 05:03:38.012770','1','OrganizationVisit object (1)',3,'',20,1),(49,'2023-12-21 05:05:36.839373','1','أنظمة امن',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(50,'2023-12-21 05:22:50.102349','11','OrganizationVisit object (11)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\"]}}]',20,1),(51,'2023-12-21 05:23:03.269302','11','OrganizationVisit object (11)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\"]}}]',20,1),(52,'2023-12-21 09:37:15.847616','11','OrganizationVisit object (11)',3,'',20,1),(53,'2023-12-22 08:58:49.902931','3','أنظمة امن',1,'[{\"added\": {}}]',16,1),(54,'2023-12-22 09:00:53.580493','2','أنظمة سلامة',2,'[{\"changed\": {\"fields\": [\"Section engineer\"]}}]',16,1),(55,'2023-12-22 09:01:09.880821','1','أنظمة امن',2,'[{\"changed\": {\"fields\": [\"Section engineer\"]}}]',16,1),(56,'2023-12-22 09:04:32.872149','3','مصاعد',2,'[{\"changed\": {\"fields\": [\"Section manager\"]}}]',11,1),(57,'2023-12-22 09:19:01.779686','20','OrganizationVisit object (20)',3,'',20,1),(58,'2023-12-22 09:19:01.800532','19','OrganizationVisit object (19)',3,'',20,1),(59,'2023-12-22 09:19:01.800532','18','OrganizationVisit object (18)',3,'',20,1),(60,'2023-12-22 09:19:01.800532','17','OrganizationVisit object (17)',3,'',20,1),(61,'2023-12-22 09:19:01.800532','16','OrganizationVisit object (16)',3,'',20,1),(62,'2023-12-22 09:19:01.815427','15','OrganizationVisit object (15)',3,'',20,1),(63,'2023-12-22 09:19:01.819908','14','OrganizationVisit object (14)',3,'',20,1),(64,'2023-12-22 09:19:01.824917','13','OrganizationVisit object (13)',3,'',20,1),(65,'2023-12-22 09:19:01.830153','12','OrganizationVisit object (12)',3,'',20,1),(66,'2023-12-22 10:10:15.179421','23','OrganizationVisit object (23)',3,'',20,1),(67,'2023-12-22 10:10:15.192993','22','OrganizationVisit object (22)',3,'',20,1),(68,'2023-12-22 10:10:15.194864','21','OrganizationVisit object (21)',3,'',20,1),(69,'2023-12-22 10:22:24.153439','3','مشرف',2,'[{\"changed\": {\"fields\": [\"User type name\"]}}]',17,1),(70,'2023-12-23 05:13:00.844744','1','OrganizationService object (1)',2,'[{\"changed\": {\"fields\": [\"Is visited\"]}}]',13,1),(71,'2023-12-23 05:27:22.831049','24','OrganizationVisit object (24)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\"]}}]',20,1),(72,'2023-12-23 06:04:00.371406','1','هامة المدن',3,'',9,1),(73,'2023-12-24 05:36:17.168008','3','هامة المدن',2,'[{\"changed\": {\"fields\": [\"Engineer\", \"Manager\", \"Order stage\", \"Admin note\", \"Image url\"]}}]',9,1),(74,'2023-12-24 05:41:36.446560','3','هامة المدن',2,'[{\"changed\": {\"fields\": [\"Image url\"]}}]',9,1),(75,'2023-12-24 05:54:17.639309','4','هامة المدن',3,'',9,1),(76,'2023-12-24 05:54:17.709594','3','هامة المدن',3,'',9,1),(77,'2023-12-24 05:59:29.760284','2','هامة المدن',2,'[{\"changed\": {\"fields\": [\"Engineer\", \"Manager\", \"Order stage\", \"Admin note\", \"Image url\"]}}]',9,1),(78,'2023-12-24 07:46:33.871049','7','هامة المدن',3,'',9,1),(79,'2023-12-24 07:46:33.927542','6','هامة المدن',3,'',9,1),(80,'2023-12-24 07:46:33.927542','5','هامة المدن',3,'',9,1),(81,'2023-12-25 11:32:43.104024','14','hamat',3,'',9,1),(82,'2023-12-25 11:32:43.118093','13','hamat',3,'',9,1),(83,'2023-12-25 11:32:43.119419','12','hamat',3,'',9,1),(84,'2023-12-25 11:32:43.119419','11','hamat',3,'',9,1),(85,'2023-12-25 11:32:43.119419','10','hamat',3,'',9,1),(86,'2023-12-25 11:32:43.119419','9','hamat',3,'',9,1),(87,'2023-12-25 11:32:43.119419','8','hamat',3,'',9,1),(88,'2023-12-25 11:33:05.300504','7','OrganizationService object (7)',3,'',13,1),(89,'2023-12-25 11:33:05.302511','6','OrganizationService object (6)',3,'',13,1),(90,'2023-12-25 11:33:05.304496','5','OrganizationService object (5)',3,'',13,1),(91,'2023-12-25 11:33:05.307096','4','OrganizationService object (4)',3,'',13,1),(92,'2023-12-25 11:33:21.002575','5','fdff',3,'',14,1),(93,'2023-12-25 11:33:21.004569','4','yy',3,'',14,1),(94,'2023-12-25 11:33:21.007583','3','ali',3,'',14,1),(95,'2023-12-25 12:23:49.003796','26','OrganizationVisit object (26)',2,'[{\"changed\": {\"fields\": [\"Visit note\", \"Is reviewed\"]}}]',20,1),(96,'2023-12-25 13:59:33.373526','26','OrganizationVisit object (26)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\"]}}]',20,1),(97,'2023-12-25 14:01:48.927554','26','OrganizationVisit object (26)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\"]}}]',20,1),(98,'2023-12-25 14:01:55.812478','25','OrganizationVisit object (25)',2,'[{\"changed\": {\"fields\": [\"Is reviewed\", \"Review note\"]}}]',20,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(18,'custom_auth','useraccount'),(17,'custom_auth','usertype'),(19,'geo_location','geolocation'),(7,'orgs','employeerole'),(15,'orgs','orderstage'),(8,'orgs','orderstatus'),(9,'orgs','organization'),(14,'orgs','organizationemployee'),(13,'orgs','organizationservice'),(10,'orgs','organizationtype'),(20,'orgs','organizationvisit'),(11,'orgs','servicesection'),(16,'orgs','servicesectionemployee'),(12,'orgs','servicetype'),(21,'orgs','visitstatus'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-19 11:14:01.891049'),(2,'auth','0001_initial','2023-12-19 11:14:02.457595'),(3,'admin','0001_initial','2023-12-19 11:14:02.589978'),(4,'admin','0002_logentry_remove_auto_add','2023-12-19 11:14:02.611470'),(5,'admin','0003_logentry_add_action_flag_choices','2023-12-19 11:14:02.623811'),(6,'contenttypes','0002_remove_content_type_name','2023-12-19 11:14:02.723931'),(7,'auth','0002_alter_permission_name_max_length','2023-12-19 11:14:02.791255'),(8,'auth','0003_alter_user_email_max_length','2023-12-19 11:14:02.813467'),(9,'auth','0004_alter_user_username_opts','2023-12-19 11:14:02.829575'),(10,'auth','0005_alter_user_last_login_null','2023-12-19 11:14:02.892628'),(11,'auth','0006_require_contenttypes_0002','2023-12-19 11:14:02.892628'),(12,'auth','0007_alter_validators_add_error_messages','2023-12-19 11:14:02.908935'),(13,'auth','0008_alter_user_username_max_length','2023-12-19 11:14:03.013272'),(14,'auth','0009_alter_user_last_name_max_length','2023-12-19 11:14:03.075183'),(15,'auth','0010_alter_group_name_max_length','2023-12-19 11:14:03.105744'),(16,'auth','0011_update_proxy_permissions','2023-12-19 11:14:03.111826'),(17,'auth','0012_alter_user_first_name_max_length','2023-12-19 11:14:03.175112'),(18,'custom_auth','0001_initial','2023-12-19 11:14:03.283980'),(19,'custom_auth','0002_alter_useraccount_second_name','2023-12-19 11:14:03.289599'),(20,'custom_auth','0003_alter_useraccount_email_and_more','2023-12-19 11:14:03.298005'),(21,'orgs','0001_initial','2023-12-19 11:14:03.893154'),(22,'geo_location','0001_initial','2023-12-19 11:14:03.997073'),(23,'orgs','0002_orderstage','2023-12-19 11:14:04.016428'),(24,'orgs','0003_organization_order_stage','2023-12-19 11:14:04.105631'),(25,'orgs','0004_alter_organization_note','2023-12-19 11:14:04.173643'),(26,'orgs','0005_organization_admin_note_organization_engineer_note','2023-12-19 11:14:04.241040'),(27,'orgs','0006_servicesection_section_manager_and_more','2023-12-19 11:14:04.483028'),(28,'orgs','0007_rename_engineer_servicesectionemployee_employee','2023-12-19 11:14:04.599759'),(29,'orgs','0008_alter_servicesectionemployee_options_and_more','2023-12-19 11:14:04.696674'),(30,'sessions','0001_initial','2023-12-19 11:14:04.725818'),(31,'orgs','0009_organizationvisit','2023-12-20 15:53:56.462226'),(32,'orgs','0010_visitstatus','2023-12-21 04:42:56.202194'),(33,'orgs','0011_organizationvisit_is_reviewed','2023-12-21 04:51:57.414240'),(34,'orgs','0012_organizationvisit_review_note_and_more','2023-12-21 06:25:07.997294'),(35,'orgs','0013_alter_organizationvisit_is_reviewed','2023-12-21 06:58:34.269040'),(36,'orgs','0014_alter_organizationvisit_is_reviewed_and_more','2023-12-21 07:17:54.262357'),(37,'orgs','0015_alter_organizationvisit_options_and_more','2023-12-22 10:04:48.202167'),(38,'orgs','0016_organization_image_url','2023-12-23 10:16:14.333156');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3ca80xjsxv1x0y6gdjoc3zutftut0za5','.eJxVjMsOgjAUBf-la9N4C6WtS_d8Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexVwMmNPvRsgPnXYgd5xus-V5WpeR7K7Yg1bbz6LP6-H-HQxYh2_dAnEroI6gYXUSUjlH8eBIY_RN0CINI4lg6FyKSJp84eITkAThzrw_A245Kg:1rFY4s:ZBXKI_-0q15oH9pWLY51I1xZm9lHNuYj10WtYOWzfPc','2024-01-02 11:15:58.030699'),('7jbgvfp5odt69g5gekl1fqg31ph6oxbv','.eJxVjMsOgjAUBf-la9N4C6WtS_d8Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexVwMmNPvRsgPnXYgd5xus-V5WpeR7K7Yg1bbz6LP6-H-HQxYh2_dAnEroI6gYXUSUjlH8eBIY_RN0CINI4lg6FyKSJp84eITkAThzrw_A245Kg:1rHH4C:l7E6Qe80t3PskrW4rllBgcstm8D8N9DkqV_gTc8MPZQ','2024-01-07 05:30:24.372808'),('7zla1bj5a22ohmld6afkd725jbwooryu','.eJxVjMsOgjAUBf-la9N4C6WtS_d8Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexVwMmNPvRsgPnXYgd5xus-V5WpeR7K7Yg1bbz6LP6-H-HQxYh2_dAnEroI6gYXUSUjlH8eBIY_RN0CINI4lg6FyKSJp84eITkAThzrw_A245Kg:1rGxuD:udQhdF5I_phvpB-gp2vPPPMsXzHW0SirAka6R1apeZM','2024-01-06 09:02:49.562121'),('j22l4b2ni9fnwsx83den3afwha2pge0x','.eJxVjMsOgjAUBf-la9N4C6WtS_d8Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexVwMmNPvRsgPnXYgd5xus-V5WpeR7K7Yg1bbz6LP6-H-HQxYh2_dAnEroI6gYXUSUjlH8eBIY_RN0CINI4lg6FyKSJp84eITkAThzrw_A245Kg:1rFYK0:SDhFfhD5MA5KSDo_HAY7Mu6ap5ZXyxWgwCNTM1ltRKs','2024-01-02 11:31:36.913562');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `geo_location_geolocation`
--

DROP TABLE IF EXISTS `geo_location_geolocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `geo_location_geolocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  `country_name` varchar(100) NOT NULL,
  `locality` varchar(200) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `organization_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `geo_location_geoloca_organization_id_14a36780_fk_orgs_orga` (`organization_id`),
  CONSTRAINT `geo_location_geoloca_organization_id_14a36780_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geo_location_geolocation`
--

LOCK TABLES `geo_location_geolocation` WRITE;
/*!40000 ALTER TABLE `geo_location_geolocation` DISABLE KEYS */;
INSERT INTO `geo_location_geolocation` VALUES (1,38.6299047,24.4780239,'Saudia','Madinah','4 Round Street, Sana\'a (Yemen)',NULL),(2,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',2),(3,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(4,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(5,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(6,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(7,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(8,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(9,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(10,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(11,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(12,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(13,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(14,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',NULL),(15,39.6299047,24.4780239,'Saudi Arabia','Madinah','FJHH+6X2, Bani Muawiyah, Madinah 42313, Saudi Arabia',15);
/*!40000 ALTER TABLE `geo_location_geolocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_employeerole`
--

DROP TABLE IF EXISTS `orgs_employeerole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_employeerole` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_employeerole`
--

LOCK TABLES `orgs_employeerole` WRITE;
/*!40000 ALTER TABLE `orgs_employeerole` DISABLE KEYS */;
INSERT INTO `orgs_employeerole` VALUES (1,'مالك'),(2,'مدير'),(3,'موظف');
/*!40000 ALTER TABLE `orgs_employeerole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_orderstage`
--

DROP TABLE IF EXISTS `orgs_orderstage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_orderstage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_orderstage`
--

LOCK TABLES `orgs_orderstage` WRITE;
/*!40000 ALTER TABLE `orgs_orderstage` DISABLE KEYS */;
INSERT INTO `orgs_orderstage` VALUES (1,'جديد');
/*!40000 ALTER TABLE `orgs_orderstage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_orderstatus`
--

DROP TABLE IF EXISTS `orgs_orderstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_orderstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_orderstatus`
--

LOCK TABLES `orgs_orderstatus` WRITE;
/*!40000 ALTER TABLE `orgs_orderstatus` DISABLE KEYS */;
INSERT INTO `orgs_orderstatus` VALUES (1,'يحتاج الآن'),(2,'تحديد تاريخ'),(3,'محتمل');
/*!40000 ALTER TABLE `orgs_orderstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_organization`
--

DROP TABLE IF EXISTS `orgs_organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_organization` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `note` longtext,
  `expected_date` date DEFAULT NULL,
  `employee_id` bigint DEFAULT NULL,
  `engineer_id` bigint DEFAULT NULL,
  `order_status_id` bigint NOT NULL,
  `org_type_id` bigint NOT NULL,
  `order_stage_id` bigint DEFAULT NULL,
  `admin_note` longtext,
  `engineer_note` longtext,
  `manager_id` bigint DEFAULT NULL,
  `image_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organization_org_type_id_d3fb2bce_fk_orgs_orga` (`org_type_id`),
  KEY `orgs_organization_employee_id_61b9ee19_fk_custom_au` (`employee_id`),
  KEY `orgs_organization_engineer_id_cf231973_fk_custom_au` (`engineer_id`),
  KEY `orgs_organization_order_status_id_6e1b53be_fk_orgs_orde` (`order_status_id`),
  KEY `orgs_organization_order_stage_id_62c59bed_fk_orgs_orderstage_id` (`order_stage_id`),
  KEY `orgs_organization_manager_id_0fcda8a0_fk_custom_au` (`manager_id`),
  CONSTRAINT `orgs_organization_employee_id_61b9ee19_fk_custom_au` FOREIGN KEY (`employee_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_organization_engineer_id_cf231973_fk_custom_au` FOREIGN KEY (`engineer_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_organization_manager_id_0fcda8a0_fk_custom_au` FOREIGN KEY (`manager_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_organization_order_stage_id_62c59bed_fk_orgs_orderstage_id` FOREIGN KEY (`order_stage_id`) REFERENCES `orgs_orderstage` (`id`),
  CONSTRAINT `orgs_organization_order_status_id_6e1b53be_fk_orgs_orde` FOREIGN KEY (`order_status_id`) REFERENCES `orgs_orderstatus` (`id`),
  CONSTRAINT `orgs_organization_org_type_id_d3fb2bce_fk_orgs_orga` FOREIGN KEY (`org_type_id`) REFERENCES `orgs_organizationtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organization`
--

LOCK TABLES `orgs_organization` WRITE;
/*!40000 ALTER TABLE `orgs_organization` DISABLE KEYS */;
INSERT INTO `orgs_organization` VALUES (2,'هامة المدن','تم','2023-12-23',NULL,1,2,1,1,'s','2',1,'images/8faf8dc8-b505-4148-a3b1-8b2687d9eca0.jpg'),(15,'hamat','hamat','2031-08-25',NULL,NULL,3,2,NULL,NULL,NULL,NULL,'images/7b5153db-4c98-4258-9ec3-105738c5c4d8.jpg');
/*!40000 ALTER TABLE `orgs_organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_organizationemployee`
--

DROP TABLE IF EXISTS `orgs_organizationemployee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_organizationemployee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `organization_id` bigint NOT NULL,
  `role_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organizationemp_organization_id_e793b97c_fk_orgs_orga` (`organization_id`),
  KEY `orgs_organizationemp_role_id_f647f6e7_fk_orgs_empl` (`role_id`),
  CONSTRAINT `orgs_organizationemp_organization_id_e793b97c_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`),
  CONSTRAINT `orgs_organizationemp_role_id_f647f6e7_fk_orgs_empl` FOREIGN KEY (`role_id`) REFERENCES `orgs_employeerole` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationemployee`
--

LOCK TABLES `orgs_organizationemployee` WRITE;
/*!40000 ALTER TABLE `orgs_organizationemployee` DISABLE KEYS */;
INSERT INTO `orgs_organizationemployee` VALUES (2,'ابو كنان','0539758319',2,1),(6,'uyy','999',2,2),(7,'6y6','88',2,2);
/*!40000 ALTER TABLE `orgs_organizationemployee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_organizationservice`
--

DROP TABLE IF EXISTS `orgs_organizationservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_organizationservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `organization_id` bigint NOT NULL,
  `service_section_id` bigint NOT NULL,
  `service_type_id` bigint NOT NULL,
  `is_visited` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organizationser_organization_id_8211dca1_fk_orgs_orga` (`organization_id`),
  KEY `orgs_organizationser_service_section_id_cdacb9b9_fk_orgs_serv` (`service_section_id`),
  KEY `orgs_organizationser_service_type_id_ee9123f3_fk_orgs_serv` (`service_type_id`),
  CONSTRAINT `orgs_organizationser_organization_id_8211dca1_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`),
  CONSTRAINT `orgs_organizationser_service_section_id_cdacb9b9_fk_orgs_serv` FOREIGN KEY (`service_section_id`) REFERENCES `orgs_servicesection` (`id`),
  CONSTRAINT `orgs_organizationser_service_type_id_ee9123f3_fk_orgs_serv` FOREIGN KEY (`service_type_id`) REFERENCES `orgs_servicetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationservice`
--

LOCK TABLES `orgs_organizationservice` WRITE;
/*!40000 ALTER TABLE `orgs_organizationservice` DISABLE KEYS */;
INSERT INTO `orgs_organizationservice` VALUES (8,2,1,2,1),(9,15,2,1,0);
/*!40000 ALTER TABLE `orgs_organizationservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_organizationtype`
--

DROP TABLE IF EXISTS `orgs_organizationtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_organizationtype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationtype`
--

LOCK TABLES `orgs_organizationtype` WRITE;
/*!40000 ALTER TABLE `orgs_organizationtype` DISABLE KEYS */;
INSERT INTO `orgs_organizationtype` VALUES (1,'برج'),(2,'مركز تجاري');
/*!40000 ALTER TABLE `orgs_organizationtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_organizationvisit`
--

DROP TABLE IF EXISTS `orgs_organizationvisit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_organizationvisit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `visit_note` varchar(100) NOT NULL,
  `visit_state` int NOT NULL,
  `organization_id` bigint NOT NULL,
  `service_section_id` bigint NOT NULL,
  `service_type_id` bigint NOT NULL,
  `visitor_id` bigint DEFAULT NULL,
  `is_reviewed` int NOT NULL,
  `review_note` varchar(100) NOT NULL,
  `reviewer_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organizationvis_organization_id_1908da37_fk_orgs_orga` (`organization_id`),
  KEY `orgs_organizationvis_service_section_id_825507e4_fk_orgs_serv` (`service_section_id`),
  KEY `orgs_organizationvis_service_type_id_b861c5e0_fk_orgs_serv` (`service_type_id`),
  KEY `orgs_organizationvis_visitor_id_0e616466_fk_custom_au` (`visitor_id`),
  KEY `orgs_organizationvis_reviewer_id_42a11357_fk_custom_au` (`reviewer_id`),
  CONSTRAINT `orgs_organizationvis_organization_id_1908da37_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`),
  CONSTRAINT `orgs_organizationvis_reviewer_id_42a11357_fk_custom_au` FOREIGN KEY (`reviewer_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_organizationvis_service_section_id_825507e4_fk_orgs_serv` FOREIGN KEY (`service_section_id`) REFERENCES `orgs_servicesection` (`id`),
  CONSTRAINT `orgs_organizationvis_service_type_id_b861c5e0_fk_orgs_serv` FOREIGN KEY (`service_type_id`) REFERENCES `orgs_servicetype` (`id`),
  CONSTRAINT `orgs_organizationvis_visitor_id_0e616466_fk_custom_au` FOREIGN KEY (`visitor_id`) REFERENCES `custom_auth_useraccount` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationvisit`
--

LOCK TABLES `orgs_organizationvisit` WRITE;
/*!40000 ALTER TABLE `orgs_organizationvisit` DISABLE KEYS */;
INSERT INTO `orgs_organizationvisit` VALUES (25,'تم الاتفاق مع العميل',1,2,1,1,3,1,'تم تم تم.',2),(26,'donedone',1,2,1,2,2,1,'تم تم',2);
/*!40000 ALTER TABLE `orgs_organizationvisit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_servicesection`
--

DROP TABLE IF EXISTS `orgs_servicesection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_servicesection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `section_manager_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_servicesection_section_manager_id_9c44150e_fk_custom_au` (`section_manager_id`),
  CONSTRAINT `orgs_servicesection_section_manager_id_9c44150e_fk_custom_au` FOREIGN KEY (`section_manager_id`) REFERENCES `custom_auth_useraccount` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_servicesection`
--

LOCK TABLES `orgs_servicesection` WRITE;
/*!40000 ALTER TABLE `orgs_servicesection` DISABLE KEYS */;
INSERT INTO `orgs_servicesection` VALUES (1,'أنظمة امن',2),(2,'أنظمة سلامة',2),(3,'مصاعد',1);
/*!40000 ALTER TABLE `orgs_servicesection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_servicesectionemployee`
--

DROP TABLE IF EXISTS `orgs_servicesectionemployee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_servicesectionemployee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employee_id` bigint DEFAULT NULL,
  `service_section_id` bigint DEFAULT NULL,
  `service_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_servicesectione_service_section_id_ad7e57f2_fk_orgs_serv` (`service_section_id`),
  KEY `orgs_servicesectione_service_type_id_3b1b0317_fk_orgs_serv` (`service_type_id`),
  KEY `orgs_servicesectione_employee_id_595449b4_fk_custom_au` (`employee_id`),
  CONSTRAINT `orgs_servicesectione_employee_id_595449b4_fk_custom_au` FOREIGN KEY (`employee_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_servicesectione_service_section_id_ad7e57f2_fk_orgs_serv` FOREIGN KEY (`service_section_id`) REFERENCES `orgs_servicesection` (`id`),
  CONSTRAINT `orgs_servicesectione_service_type_id_3b1b0317_fk_orgs_serv` FOREIGN KEY (`service_type_id`) REFERENCES `orgs_servicetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_servicesectionemployee`
--

LOCK TABLES `orgs_servicesectionemployee` WRITE;
/*!40000 ALTER TABLE `orgs_servicesectionemployee` DISABLE KEYS */;
INSERT INTO `orgs_servicesectionemployee` VALUES (1,3,1,1),(2,3,2,2),(3,3,1,1);
/*!40000 ALTER TABLE `orgs_servicesectionemployee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_servicetype`
--

DROP TABLE IF EXISTS `orgs_servicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_servicetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_servicetype`
--

LOCK TABLES `orgs_servicetype` WRITE;
/*!40000 ALTER TABLE `orgs_servicetype` DISABLE KEYS */;
INSERT INTO `orgs_servicetype` VALUES (1,'تركيب'),(2,'صيانة'),(3,'اعطال');
/*!40000 ALTER TABLE `orgs_servicetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_visitstatus`
--

DROP TABLE IF EXISTS `orgs_visitstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_visitstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_visitstatus`
--

LOCK TABLES `orgs_visitstatus` WRITE;
/*!40000 ALTER TABLE `orgs_visitstatus` DISABLE KEYS */;
INSERT INTO `orgs_visitstatus` VALUES (1,'تم الإتفاق'),(2,'لم يتم الإتفاق');
/*!40000 ALTER TABLE `orgs_visitstatus` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-26  9:12:20
