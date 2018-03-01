-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema twitter4pm
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema twitter4pm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `twitter4pm` DEFAULT CHARACTER SET utf8 ;
USE `twitter4pm` ;

-- -----------------------------------------------------
-- Table `twitter4pm`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter4pm`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter4pm`.`tweets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter4pm`.`tweets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tweet` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `likes` INT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tweets_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_tweets_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `twitter4pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter4pm`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter4pm`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `tweets_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_users_idx` (`users_id` ASC),
  INDEX `fk_likes_tweets1_idx` (`tweets_id` ASC),
  CONSTRAINT `fk_likes_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `twitter4pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_tweets1`
    FOREIGN KEY (`tweets_id`)
    REFERENCES `twitter4pm`.`tweets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter4pm`.`followers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter4pm`.`followers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `follower` INT NOT NULL,
  `leader` INT NOT NULL,
  PRIMARY KEY (`id`, `follower`, `leader`),
  INDEX `fk_users_has_users_users2_idx` (`leader` ASC),
  INDEX `fk_users_has_users_users1_idx` (`follower` ASC),
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`follower`)
    REFERENCES `twitter4pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2`
    FOREIGN KEY (`leader`)
    REFERENCES `twitter4pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
