-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `books` ;

-- -----------------------------------------------------
-- Schema books
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books` DEFAULT CHARACTER SET utf8 ;
USE `books` ;

-- -----------------------------------------------------
-- Table `books`.`author`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books`.`author` ;

CREATE TABLE IF NOT EXISTS `books`.`author` (
  `author_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `author_fname` VARCHAR(45) NOT NULL,
  `author_mname` VARCHAR(45) NOT NULL,
  `author_lname` VARCHAR(45) NOT NULL,
  `author_dob` DATE NOT NULL,
  `author_dod` DATE NULL,
  PRIMARY KEY (`author_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books`.`book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books`.`book` ;

CREATE TABLE IF NOT EXISTS `books`.`book` (
  `book_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_name` VARCHAR(100) NOT NULL,
  `author_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`book_id`),
  INDEX `FK_1_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `FK_1`
    FOREIGN KEY (`author_id`)
    REFERENCES `books`.`author` (`author_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books`.`genre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books`.`genre` ;

CREATE TABLE IF NOT EXISTS `books`.`genre` (
  `genre_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `genre_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books`.`genre_book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books`.`genre_book` ;

CREATE TABLE IF NOT EXISTS `books`.`genre_book` (
  `genre_id` INT UNSIGNED NOT NULL,
  `book_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`genre_id`, `book_id`),
  INDEX `fk_genre_has_book_book1_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_genre_has_book_genre1_idx` (`genre_id` ASC) VISIBLE,
  CONSTRAINT `fk_genre_has_book_genre1`
    FOREIGN KEY (`genre_id`)
    REFERENCES `books`.`genre` (`genre_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_genre_has_book_book1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books`.`book` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books`.`format`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books`.`format` ;

CREATE TABLE IF NOT EXISTS `books`.`format` (
  `format_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `format_type` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`format_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books`.`book_format`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books`.`book_format` ;

CREATE TABLE IF NOT EXISTS `books`.`book_format` (
  `book_id` INT UNSIGNED NOT NULL,
  `format_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`book_id`, `format_id`),
  INDEX `fk_book_has_format_format1_idx` (`format_id` ASC) VISIBLE,
  INDEX `fk_book_has_format_book1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_book_has_format_book1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books`.`book` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_book_has_format_format1`
    FOREIGN KEY (`format_id`)
    REFERENCES `books`.`format` (`format_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
