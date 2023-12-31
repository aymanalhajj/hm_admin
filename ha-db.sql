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
-- Table structure for table `app_settings_employeerole`
--

DROP TABLE IF EXISTS `app_settings_employeerole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_employeerole` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_employeerole`
--

LOCK TABLES `app_settings_employeerole` WRITE;
/*!40000 ALTER TABLE `app_settings_employeerole` DISABLE KEYS */;
INSERT INTO `app_settings_employeerole` VALUES (1,'مالك'),(2,'مدير'),(3,'موظف');
/*!40000 ALTER TABLE `app_settings_employeerole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_orderstage`
--

DROP TABLE IF EXISTS `app_settings_orderstage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_orderstage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_orderstage`
--

LOCK TABLES `app_settings_orderstage` WRITE;
/*!40000 ALTER TABLE `app_settings_orderstage` DISABLE KEYS */;
INSERT INTO `app_settings_orderstage` VALUES (1,'ترويج'),(2,'دراسة'),(3,'تعاقد');
/*!40000 ALTER TABLE `app_settings_orderstage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_orderstatus`
--

DROP TABLE IF EXISTS `app_settings_orderstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_orderstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_orderstatus`
--

LOCK TABLES `app_settings_orderstatus` WRITE;
/*!40000 ALTER TABLE `app_settings_orderstatus` DISABLE KEYS */;
INSERT INTO `app_settings_orderstatus` VALUES (1,'يحتاج الآن'),(2,'تحديد تاريخ'),(3,'محتمل');
/*!40000 ALTER TABLE `app_settings_orderstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_organizationtype`
--

DROP TABLE IF EXISTS `app_settings_organizationtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_organizationtype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_organizationtype`
--

LOCK TABLES `app_settings_organizationtype` WRITE;
/*!40000 ALTER TABLE `app_settings_organizationtype` DISABLE KEYS */;
INSERT INTO `app_settings_organizationtype` VALUES (1,'برج'),(2,'مركز تجاري'),(3,'فندق'),(4,'مبنى سكني');
/*!40000 ALTER TABLE `app_settings_organizationtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_projectsetting`
--

DROP TABLE IF EXISTS `app_settings_projectsetting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_projectsetting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `days_before_contract` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_projectsetting`
--

LOCK TABLES `app_settings_projectsetting` WRITE;
/*!40000 ALTER TABLE `app_settings_projectsetting` DISABLE KEYS */;
INSERT INTO `app_settings_projectsetting` VALUES (1,30);
/*!40000 ALTER TABLE `app_settings_projectsetting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_servicesection`
--

DROP TABLE IF EXISTS `app_settings_servicesection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_servicesection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `section_manager_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_settings_service_section_manager_id_05db8a28_fk_custom_au` (`section_manager_id`),
  CONSTRAINT `app_settings_service_section_manager_id_05db8a28_fk_custom_au` FOREIGN KEY (`section_manager_id`) REFERENCES `custom_auth_useraccount` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_servicesection`
--

LOCK TABLES `app_settings_servicesection` WRITE;
/*!40000 ALTER TABLE `app_settings_servicesection` DISABLE KEYS */;
INSERT INTO `app_settings_servicesection` VALUES (1,'مصاعد',NULL),(2,'أنظمة أمن',NULL),(3,'أنظمة سلامة',NULL);
/*!40000 ALTER TABLE `app_settings_servicesection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_servicesectionemployee`
--

DROP TABLE IF EXISTS `app_settings_servicesectionemployee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_servicesectionemployee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `employee_id` bigint DEFAULT NULL,
  `service_section_id` bigint DEFAULT NULL,
  `service_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_settings_service_employee_id_fbd44cb6_fk_custom_au` (`employee_id`),
  KEY `app_settings_service_service_section_id_ae224e09_fk_app_setti` (`service_section_id`),
  KEY `app_settings_service_service_type_id_0c6aa3ab_fk_app_setti` (`service_type_id`),
  CONSTRAINT `app_settings_service_employee_id_fbd44cb6_fk_custom_au` FOREIGN KEY (`employee_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `app_settings_service_service_section_id_ae224e09_fk_app_setti` FOREIGN KEY (`service_section_id`) REFERENCES `app_settings_servicesection` (`id`),
  CONSTRAINT `app_settings_service_service_type_id_0c6aa3ab_fk_app_setti` FOREIGN KEY (`service_type_id`) REFERENCES `app_settings_servicetype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_servicesectionemployee`
--

LOCK TABLES `app_settings_servicesectionemployee` WRITE;
/*!40000 ALTER TABLE `app_settings_servicesectionemployee` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_settings_servicesectionemployee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_servicetype`
--

DROP TABLE IF EXISTS `app_settings_servicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_servicetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_servicetype`
--

LOCK TABLES `app_settings_servicetype` WRITE;
/*!40000 ALTER TABLE `app_settings_servicetype` DISABLE KEYS */;
INSERT INTO `app_settings_servicetype` VALUES (1,'تركيب'),(2,'صيانة'),(3,'اعطال');
/*!40000 ALTER TABLE `app_settings_servicetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_settings_visitstatus`
--

DROP TABLE IF EXISTS `app_settings_visitstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_settings_visitstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_settings_visitstatus`
--

LOCK TABLES `app_settings_visitstatus` WRITE;
/*!40000 ALTER TABLE `app_settings_visitstatus` DISABLE KEYS */;
INSERT INTO `app_settings_visitstatus` VALUES (1,'تم الإتفاق'),(2,'لم يتم الإتفاق');
/*!40000 ALTER TABLE `app_settings_visitstatus` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Organization',7,'add_organization'),(26,'Can change Organization',7,'change_organization'),(27,'Can delete Organization',7,'delete_organization'),(28,'Can view Organization',7,'view_organization'),(29,'Can add Organization Visit',8,'add_organizationvisit'),(30,'Can change Organization Visit',8,'change_organizationvisit'),(31,'Can delete Organization Visit',8,'delete_organizationvisit'),(32,'Can view Organization Visit',8,'view_organizationvisit'),(33,'Can add Organization Service',9,'add_organizationservice'),(34,'Can change Organization Service',9,'change_organizationservice'),(35,'Can delete Organization Service',9,'delete_organizationservice'),(36,'Can view Organization Service',9,'view_organizationservice'),(37,'Can add Organization Employee',10,'add_organizationemployee'),(38,'Can change Organization Employee',10,'change_organizationemployee'),(39,'Can delete Organization Employee',10,'delete_organizationemployee'),(40,'Can view Organization Employee',10,'view_organizationemployee'),(41,'Can add User Type',11,'add_usertype'),(42,'Can change User Type',11,'change_usertype'),(43,'Can delete User Type',11,'delete_usertype'),(44,'Can view User Type',11,'view_usertype'),(45,'Can add User Account',12,'add_useraccount'),(46,'Can change User Account',12,'change_useraccount'),(47,'Can delete User Account',12,'delete_useraccount'),(48,'Can view User Account',12,'view_useraccount'),(49,'Can add Geo Location',13,'add_geolocation'),(50,'Can change Geo Location',13,'change_geolocation'),(51,'Can delete Geo Location',13,'delete_geolocation'),(52,'Can view Geo Location',13,'view_geolocation'),(53,'Can add Employee Role',14,'add_employeerole'),(54,'Can change Employee Role',14,'change_employeerole'),(55,'Can delete Employee Role',14,'delete_employeerole'),(56,'Can view Employee Role',14,'view_employeerole'),(57,'Can add Order Stage',15,'add_orderstage'),(58,'Can change Order Stage',15,'change_orderstage'),(59,'Can delete Order Stage',15,'delete_orderstage'),(60,'Can view Order Stage',15,'view_orderstage'),(61,'Can add Order Status',16,'add_orderstatus'),(62,'Can change Order Status',16,'change_orderstatus'),(63,'Can delete Order Status',16,'delete_orderstatus'),(64,'Can view Order Status',16,'view_orderstatus'),(65,'Can add Organization Type',17,'add_organizationtype'),(66,'Can change Organization Type',17,'change_organizationtype'),(67,'Can delete Organization Type',17,'delete_organizationtype'),(68,'Can view Organization Type',17,'view_organizationtype'),(69,'Can add Service Section',18,'add_servicesection'),(70,'Can change Service Section',18,'change_servicesection'),(71,'Can delete Service Section',18,'delete_servicesection'),(72,'Can view Service Section',18,'view_servicesection'),(73,'Can add Service Type',19,'add_servicetype'),(74,'Can change Service Type',19,'change_servicetype'),(75,'Can delete Service Type',19,'delete_servicetype'),(76,'Can view Service Type',19,'view_servicetype'),(77,'Can add Visit Status',20,'add_visitstatus'),(78,'Can change Visit Status',20,'change_visitstatus'),(79,'Can delete Visit Status',20,'delete_visitstatus'),(80,'Can view Visit Status',20,'view_visitstatus'),(81,'Can add Service Section Employee',21,'add_servicesectionemployee'),(82,'Can change Service Section Employee',21,'change_servicesectionemployee'),(83,'Can delete Service Section Employee',21,'delete_servicesectionemployee'),(84,'Can view Service Section Employee',21,'view_servicesectionemployee'),(85,'Can add Project Setting',22,'add_projectsetting'),(86,'Can change Project Setting',22,'change_projectsetting'),(87,'Can delete Project Setting',22,'delete_projectsetting'),(88,'Can view Project Setting',22,'view_projectsetting');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$XqGaOd7jLJYFKTftEwrGYL$7hW4tQ5WK9dsrGI+sjT8wO0aCA5CrGUzokzvvRA37xg=','2023-12-30 11:51:48.000000',1,'admin','','','admin@admin.com',1,1,'2023-12-30 11:50:31.000000');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_auth_useraccount`
--

LOCK TABLES `custom_auth_useraccount` WRITE;
/*!40000 ALTER TABLE `custom_auth_useraccount` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-12-30 12:14:57.499266','2','ProjectSetting object (2)',1,'[{\"added\": {}}]',22,1),(2,'2023-12-30 12:15:10.565748','2','ProjectSetting object (2)',2,'[]',22,1),(3,'2023-12-30 14:49:05.088300','1','ترويج',1,'[{\"added\": {}}]',15,1),(4,'2023-12-30 14:49:17.654218','2','دراسة',1,'[{\"added\": {}}]',15,1),(5,'2023-12-30 14:49:39.043224','1','مندوب',1,'[{\"added\": {}}]',11,1),(6,'2023-12-30 14:49:44.055518','2','مهندس',1,'[{\"added\": {}}]',11,1),(7,'2023-12-30 14:49:51.771344','3','مشرف',1,'[{\"added\": {}}]',11,1),(8,'2023-12-30 14:54:03.519401','1','مصاعد',1,'[{\"added\": {}}]',18,1),(9,'2023-12-30 14:54:42.025004','2','أنظمة أمن',1,'[{\"added\": {}}]',18,1),(10,'2023-12-30 14:54:54.489764','3','أنظمة سلامة',1,'[{\"added\": {}}]',18,1),(11,'2023-12-30 14:55:27.331985','1','تم الإتفاق',1,'[{\"added\": {}}]',20,1),(12,'2023-12-30 14:55:37.283694','2','لم يتم الإتفاق',1,'[{\"added\": {}}]',20,1),(13,'2023-12-30 14:55:54.647033','1','يحتاج الآن',1,'[{\"added\": {}}]',16,1),(14,'2023-12-30 14:56:05.087803','2','تحديد تاريخ',1,'[{\"added\": {}}]',16,1),(15,'2023-12-30 14:56:13.326613','3','محتمل',1,'[{\"added\": {}}]',16,1),(16,'2023-12-30 14:57:07.876995','1','تركيب',1,'[{\"added\": {}}]',19,1),(17,'2023-12-30 14:57:12.690931','2','صيانة',1,'[{\"added\": {}}]',19,1),(18,'2023-12-30 14:57:17.181494','3','اعطال',1,'[{\"added\": {}}]',19,1),(19,'2023-12-30 14:57:28.915036','1','برج',1,'[{\"added\": {}}]',17,1),(20,'2023-12-30 14:57:35.806121','2','مركز تجاري',1,'[{\"added\": {}}]',17,1),(21,'2023-12-30 14:57:49.569099','3','فندق',1,'[{\"added\": {}}]',17,1),(22,'2023-12-30 14:57:59.592289','4','مبنى سكني',1,'[{\"added\": {}}]',17,1),(23,'2023-12-30 14:58:39.208987','1','مالك',1,'[{\"added\": {}}]',14,1),(24,'2023-12-30 14:58:43.834139','2','مدير',1,'[{\"added\": {}}]',14,1),(25,'2023-12-30 14:58:49.083931','3','موظف',1,'[{\"added\": {}}]',14,1),(26,'2023-12-30 15:00:11.385180','3','تعاقد',1,'[{\"added\": {}}]',15,1),(27,'2023-12-30 15:02:18.261853','1','admin',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',4,1),(28,'2023-12-30 15:27:16.724960','1','ProjectSetting object (1)',1,'[{\"added\": {}}]',22,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(14,'app_settings','employeerole'),(15,'app_settings','orderstage'),(16,'app_settings','orderstatus'),(17,'app_settings','organizationtype'),(22,'app_settings','projectsetting'),(18,'app_settings','servicesection'),(21,'app_settings','servicesectionemployee'),(19,'app_settings','servicetype'),(20,'app_settings','visitstatus'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'custom_auth','useraccount'),(11,'custom_auth','usertype'),(13,'geo_location','geolocation'),(7,'orgs','organization'),(10,'orgs','organizationemployee'),(9,'orgs','organizationservice'),(8,'orgs','organizationvisit'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-12-30 11:48:16.777960'),(2,'auth','0001_initial','2023-12-30 11:48:17.646207'),(3,'admin','0001_initial','2023-12-30 11:48:17.895494'),(4,'admin','0002_logentry_remove_auto_add','2023-12-30 11:48:17.919981'),(5,'admin','0003_logentry_add_action_flag_choices','2023-12-30 11:48:17.931794'),(6,'custom_auth','0001_initial','2023-12-30 11:48:18.072081'),(7,'custom_auth','0002_alter_useraccount_second_name','2023-12-30 11:48:18.078091'),(8,'custom_auth','0003_alter_useraccount_email_and_more','2023-12-30 11:48:18.102601'),(9,'app_settings','0001_initial','2023-12-30 11:48:18.604770'),(10,'contenttypes','0002_remove_content_type_name','2023-12-30 11:48:18.728352'),(11,'auth','0002_alter_permission_name_max_length','2023-12-30 11:48:18.843497'),(12,'auth','0003_alter_user_email_max_length','2023-12-30 11:48:18.890387'),(13,'auth','0004_alter_user_username_opts','2023-12-30 11:48:18.903933'),(14,'auth','0005_alter_user_last_login_null','2023-12-30 11:48:18.977505'),(15,'auth','0006_require_contenttypes_0002','2023-12-30 11:48:18.984772'),(16,'auth','0007_alter_validators_add_error_messages','2023-12-30 11:48:18.995905'),(17,'auth','0008_alter_user_username_max_length','2023-12-30 11:48:19.105312'),(18,'auth','0009_alter_user_last_name_max_length','2023-12-30 11:48:19.219194'),(19,'auth','0010_alter_group_name_max_length','2023-12-30 11:48:19.245218'),(20,'auth','0011_update_proxy_permissions','2023-12-30 11:48:19.263874'),(21,'auth','0012_alter_user_first_name_max_length','2023-12-30 11:48:19.345616'),(22,'orgs','0001_initial','2023-12-30 11:48:21.024202'),(23,'geo_location','0001_initial','2023-12-30 11:48:21.149772'),(24,'orgs','0002_alter_organization_employee_and_more','2023-12-30 11:48:21.786952'),(25,'sessions','0001_initial','2023-12-30 11:48:21.876126'),(26,'app_settings','0002_projectsetting','2023-12-30 12:12:15.242147'),(27,'app_settings','0003_alter_projectsetting_days_before_contract','2023-12-30 12:12:15.251324'),(28,'orgs','0003_organizationemployee_created_date_and_more','2023-12-30 12:27:04.695072');
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
INSERT INTO `django_session` VALUES ('qtbmo9gfvr3z6r82jxnmmd35b1mtxkl9','.eJxVjL0OAiEQhN-F2hCQv9XS_p6BALvIqYHkuKuM7y6XXKHFTDHfzLyZD9ta_NZp8TOyK5Ps9JvFkJ5Ud4CPUO-Np1bXZY58r_CDdj41pNft6P4dlNDLWCcXXQRUkCXgxZwxDAOwFm1S1hgQKLWIAgmdBjRuSIHTWWUhSRH7fAHWUDdk:1rJXsa:1ABL0Z-nHFfVRNgrs6GOMUCTiJ7XAatYZQ4BH2nWPh0','2024-01-13 11:51:48.292023');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geo_location_geolocation`
--

LOCK TABLES `geo_location_geolocation` WRITE;
/*!40000 ALTER TABLE `geo_location_geolocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `geo_location_geolocation` ENABLE KEYS */;
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
  `image_url` varchar(100) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `employee_id` bigint DEFAULT NULL,
  `order_stage_id` bigint DEFAULT NULL,
  `order_status_id` bigint DEFAULT NULL,
  `org_type_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organization_employee_id_61b9ee19_fk_custom_au` (`employee_id`),
  KEY `orgs_organization_order_stage_id_62c59bed_fk_app_setti` (`order_stage_id`),
  KEY `orgs_organization_order_status_id_6e1b53be_fk_app_setti` (`order_status_id`),
  KEY `orgs_organization_org_type_id_d3fb2bce_fk_app_setti` (`org_type_id`),
  CONSTRAINT `orgs_organization_employee_id_61b9ee19_fk_custom_au` FOREIGN KEY (`employee_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_organization_order_stage_id_62c59bed_fk_app_setti` FOREIGN KEY (`order_stage_id`) REFERENCES `app_settings_orderstage` (`id`),
  CONSTRAINT `orgs_organization_order_status_id_6e1b53be_fk_app_setti` FOREIGN KEY (`order_status_id`) REFERENCES `app_settings_orderstatus` (`id`),
  CONSTRAINT `orgs_organization_org_type_id_d3fb2bce_fk_app_setti` FOREIGN KEY (`org_type_id`) REFERENCES `app_settings_organizationtype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organization`
--

LOCK TABLES `orgs_organization` WRITE;
/*!40000 ALTER TABLE `orgs_organization` DISABLE KEYS */;
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
  `created_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organizationemp_organization_id_e793b97c_fk_orgs_orga` (`organization_id`),
  KEY `orgs_organizationemp_role_id_f647f6e7_fk_app_setti` (`role_id`),
  CONSTRAINT `orgs_organizationemp_organization_id_e793b97c_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`),
  CONSTRAINT `orgs_organizationemp_role_id_f647f6e7_fk_app_setti` FOREIGN KEY (`role_id`) REFERENCES `app_settings_employeerole` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationemployee`
--

LOCK TABLES `orgs_organizationemployee` WRITE;
/*!40000 ALTER TABLE `orgs_organizationemployee` DISABLE KEYS */;
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
  `is_visited` int NOT NULL,
  `organization_id` bigint NOT NULL,
  `service_section_id` bigint NOT NULL,
  `service_type_id` bigint NOT NULL,
  `created_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organizationser_organization_id_8211dca1_fk_orgs_orga` (`organization_id`),
  KEY `orgs_organizationser_service_section_id_cdacb9b9_fk_app_setti` (`service_section_id`),
  KEY `orgs_organizationser_service_type_id_ee9123f3_fk_app_setti` (`service_type_id`),
  CONSTRAINT `orgs_organizationser_organization_id_8211dca1_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`),
  CONSTRAINT `orgs_organizationser_service_section_id_cdacb9b9_fk_app_setti` FOREIGN KEY (`service_section_id`) REFERENCES `app_settings_servicesection` (`id`),
  CONSTRAINT `orgs_organizationser_service_type_id_ee9123f3_fk_app_setti` FOREIGN KEY (`service_type_id`) REFERENCES `app_settings_servicetype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationservice`
--

LOCK TABLES `orgs_organizationservice` WRITE;
/*!40000 ALTER TABLE `orgs_organizationservice` DISABLE KEYS */;
/*!40000 ALTER TABLE `orgs_organizationservice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orgs_organizationvisit`
--

DROP TABLE IF EXISTS `orgs_organizationvisit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orgs_organizationvisit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `visit_state` int NOT NULL,
  `visit_note` varchar(100) NOT NULL,
  `is_reviewed` int NOT NULL,
  `review_note` varchar(100) NOT NULL,
  `created_date` date DEFAULT NULL,
  `organization_id` bigint NOT NULL,
  `reviewer_id` bigint DEFAULT NULL,
  `service_section_id` bigint NOT NULL,
  `service_type_id` bigint NOT NULL,
  `visitor_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orgs_organizationvis_organization_id_1908da37_fk_orgs_orga` (`organization_id`),
  KEY `orgs_organizationvis_reviewer_id_42a11357_fk_custom_au` (`reviewer_id`),
  KEY `orgs_organizationvis_service_section_id_825507e4_fk_app_setti` (`service_section_id`),
  KEY `orgs_organizationvis_service_type_id_b861c5e0_fk_app_setti` (`service_type_id`),
  KEY `orgs_organizationvis_visitor_id_0e616466_fk_custom_au` (`visitor_id`),
  CONSTRAINT `orgs_organizationvis_organization_id_1908da37_fk_orgs_orga` FOREIGN KEY (`organization_id`) REFERENCES `orgs_organization` (`id`),
  CONSTRAINT `orgs_organizationvis_reviewer_id_42a11357_fk_custom_au` FOREIGN KEY (`reviewer_id`) REFERENCES `custom_auth_useraccount` (`id`),
  CONSTRAINT `orgs_organizationvis_service_section_id_825507e4_fk_app_setti` FOREIGN KEY (`service_section_id`) REFERENCES `app_settings_servicesection` (`id`),
  CONSTRAINT `orgs_organizationvis_service_type_id_b861c5e0_fk_app_setti` FOREIGN KEY (`service_type_id`) REFERENCES `app_settings_servicetype` (`id`),
  CONSTRAINT `orgs_organizationvis_visitor_id_0e616466_fk_custom_au` FOREIGN KEY (`visitor_id`) REFERENCES `custom_auth_useraccount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orgs_organizationvisit`
--

LOCK TABLES `orgs_organizationvisit` WRITE;
/*!40000 ALTER TABLE `orgs_organizationvisit` DISABLE KEYS */;
/*!40000 ALTER TABLE `orgs_organizationvisit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-30 18:30:21
