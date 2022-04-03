CREATE TABLE IF NOT EXISTS `tbl_sbb_data` (
	`id_profile` INT NOT NULL AUTO_INCREMENT,
  	`name` varchar(50) NOT NULL,
  	`gebdate` DATE NOT NULL,
    `gulstart` DATE NOT NULL,
  	`gulende` DATE NOT NULL,
	PRIMARY KEY (`id_profile`)
);