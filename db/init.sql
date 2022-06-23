
CREATE DATABASE research_paper;
use research_paper;

CREATE TABLE `user` (
  `nrp` varchar(15) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`nrp`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `paper` (
    `owner` VARCHAR(15) NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `path` VARCHAR(255) NOT NULL,
    `abstract` TEXT NOT NULL,
    FOREIGN KEY (owner) REFERENCES user(nrp)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;;

insert  into `user`(`nrp`,`name`,`email`,`password`) values 
('C14190064','Baskara Bagus','baskara93@gmail.com','test'),
('C1419','user','user@gmail.com','user');