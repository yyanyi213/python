/*
Navicat MySQL Data Transfer

Source Server         : secnews
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : secnewsdb

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-12-18 23:00:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `page1`
-- ----------------------------
DROP TABLE IF EXISTS `page1`;
CREATE TABLE `page1` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `time` varchar(10) DEFAULT NULL,
  `title` varchar(55) DEFAULT NULL,
  `category` varchar(10) DEFAULT NULL,
  `clickANDcomment` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of page1
-- ----------------------------
