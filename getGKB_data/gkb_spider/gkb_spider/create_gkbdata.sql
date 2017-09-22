DROP TABLE IF EXISTS `pharmgkb`;
CREATE TABLE `pharmgkb`(
`auto_id` int(11) NOT NULL AUTO_INCREMENT,
`pa_id` varchar(25) DEFAULT NULL,
`num` varchar(25) DEFAULT NULL,
`genes` varchar(255) DEFAULT NULL,
`chemicals` varchar(255) DEFAULT NULL,
`pvalue` varchar(255) DEFAULT NULL,
`literature` varchar(255) DEFAULT NULL,
`significance` varchar(255) DEFAULT NULL,
`phenotypeCategories` varchar(500) DEFAULT NULL,
`variants` varchar(255) DEFAULT NULL,
`cases` varchar(255) DEFAULT NULL,
`race` varchar(255) DEFAULT NULL,
`characteristics` varchar(500) DEFAULT NULL,
`sentence` varchar(555) DEFAULT NULL,
`literatureUrl` varchar(255) DEFAULT NULL,
`id` varchar(255) DEFAULT NULL,
PRIMARY KEY (`auto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;