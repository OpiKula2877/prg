-- -----------------------------------------------------
-- Schema rejstrik
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rejstrik
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rejstrik` DEFAULT CHARACTER SET utf8 ;
USE `rejstrik` ;

-- -----------------------------------------------------
-- Table `rejstrik`.`źaci`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rejstrik`.`źaci` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `jmeno` VARCHAR(45) NOT NULL,
  `primeni` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rejstrik`.`ciny`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rejstrik`.`ciny` (
  `id` INT NOT NULL,
  `nazev` VARCHAR(45) NOT NULL,
  `opatreni` VARCHAR(100) NULL,
  `źaci_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `źaci_id`),
  INDEX `fk_ciny_źaci_idx` (`źaci_id` ASC),
  CONSTRAINT `fk_ciny_źaci`
    FOREIGN KEY (`źaci_id`)
    REFERENCES `rejstrik`.`źaci` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;