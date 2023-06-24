CREATE DATABASE IF NOT EXISTS `data_base` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `data_base`;

CREATE TABLE IF NOT EXISTS `user` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,    
  	`password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `user` (`id`, `username`, `password`) VALUES (1, 'admin', 'passwords@12345');
INSERT INTO `user` (`id`, `username`, `password`) VALUES (2, 'customer1', 'passwords@12345');
INSERT INTO `user` (`id`, `username`, `password`) VALUES (3, 'customer2', 'passwords@12345');

select * from user; 

CREATE TABLE IF NOT EXISTS `customer` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`ItemCustomer` varchar(255) NOT NULL,    
  	`Customer1` varchar(255) NOT NULL,
  	`Customer2` varchar(255) NOT NULL,
  	`Total` varchar(255) NOT NULL,    
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO customer (ItemCustomer)
VALUES ('Quantity'), ('Weight'), ('BoxCount');
select * from customer;
ALTER TABLE customer
DROP COLUMN id;




