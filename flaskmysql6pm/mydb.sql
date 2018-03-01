-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema twitter6pm
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema twitter6pm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `twitter6pm` DEFAULT CHARACTER SET utf8 ;
USE `twitter6pm` ;

-- -----------------------------------------------------
-- Table `twitter6pm`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter6pm`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter6pm`.`tweets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter6pm`.`tweets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tweets` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`),
  INDEX `fk_tweets_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_tweets_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `twitter6pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter6pm`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter6pm`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tweet_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `tweet_id`, `user_id`),
  INDEX `fk_tweets_has_users_users1_idx` (`user_id` ASC),
  INDEX `fk_tweets_has_users_tweets_idx` (`tweet_id` ASC),
  CONSTRAINT `fk_tweets_has_users_tweets`
    FOREIGN KEY (`tweet_id`)
    REFERENCES `twitter6pm`.`tweets` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tweets_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `twitter6pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter6pm`.`followers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter6pm`.`followers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `follower_id` INT NOT NULL,
  `leader_id` INT NOT NULL,
  PRIMARY KEY (`id`, `follower_id`, `leader_id`),
  INDEX `fk_users_has_users_users2_idx` (`leader_id` ASC),
  INDEX `fk_users_has_users_users1_idx` (`follower_id` ASC),
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`follower_id`)
    REFERENCES `twitter6pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2`
    FOREIGN KEY (`leader_id`)
    REFERENCES `twitter6pm`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
