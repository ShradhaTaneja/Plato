CREATE TABLE `restaurant` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `rname` varchar(50) NOT NULL,
  `raddress` varchar(200) NOT NULL,
  `rcity` varchar(20) NOT NULL,
  `rstate` varchar(20) NOT NULL,
  `rating` int(11) DEFAULT '0',
  `rcontact` varchar(20) NOT NULL,
  `rwebsite` varchar(30) DEFAULT NULL,
  `remail` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`rid`)
);

CREATE TABLE `menu_category` (
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`category`)
);

CREATE TABLE `menu_items` (
  `category` varchar(50) NOT NULL,
  `rid` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `price` varchar(20) DEFAULT NULL,
  `item_id` varchar(30) NOT NULL,
  PRIMARY KEY (`category`,`rid`,`item_id`),
  KEY `rid` (`rid`),
  CONSTRAINT `menu_items_ibfk_1` FOREIGN KEY (`category`) REFERENCES `menu_category` (`category`),
  CONSTRAINT `menu_items_ibfk_2` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`) ON DELETE CASCADE
);

CREATE TABLE `restaurant_menu` (
  `rid` int(11) NOT NULL,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`rid`,`category`),
  KEY `category` (`category`),
  CONSTRAINT `restaurant_menu_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`) ON DELETE CASCADE,
  CONSTRAINT `restaurant_menu_ibfk_2` FOREIGN KEY (`category`) REFERENCES `menu_category` (`category`)
);
