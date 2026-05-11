-- --------------------------------------------------------
-- SQL skript pro evidenci potravin v mrazáku
-- Splňuje zadání:
--   - potraviny v mrazáku
--   - jejich kategorie
--   - fóch (šuplík), ve kterém se nachází
--   - množství a expirace
-- --------------------------------------------------------

    -- Vytvoření a použití databáze
    CREATE DATABASE IF NOT EXISTS mrazak_db CHARACTER SET utf8mb4 COLLATE utf8mb4_czech_ci;
    USE mrazak_db;

    -- Tabulka: Kategorie potravin
    CREATE TABLE kategorie (
        id_kategorie INT AUTO_INCREMENT PRIMARY KEY,
        nazev VARCHAR(100) NOT NULL UNIQUE
    ) ENGINE=InnoDB;

    -- Tabulka: Fóch (šuplík v mrazáku)
    CREATE TABLE foch (
        id_fochu INT AUTO_INCREMENT PRIMARY KEY,
        nazev VARCHAR(100) NOT NULL UNIQUE,
        popis TEXT
    ) ENGINE=InnoDB;

-- Tabulka: Potraviny
CREATE TABLE potravina (
    id_potraviny INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(150) NOT NULL,
    id_kategorie INT NOT NULL,
    id_fochu INT NOT NULL,
    mnozstvi DECIMAL(10, 2) NOT NULL CHECK (mnozstvi >= 0),
    jednotka_mnozstvi ENUM('ks', 'g', 'kg', 'l', 'ml') NOT NULL DEFAULT 'ks',
    datum_expirace DATE NOT NULL,
    poznamka TEXT,
    
    -- Cizí klíče
    FOREIGN KEY (id_kategorie) REFERENCES kategorie(id_kategorie) 
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_fochu) REFERENCES foch(id_fochu) 
        ON DELETE RESTRICT ON UPDATE CASCADE,
    
    -- Index pro efektivní vyhledávání podle expirace
    INDEX idx_expirace (datum_expirace)
) ENGINE=InnoDB;

-- Volitelné: Ukázková data
INSERT INTO kategorie (nazev) VALUES 
('Maso'), 
('Zelenina'), 
('Těstoviny'), 
('Pečivo');

INSERT INTO foch (nazev, popis) VALUES 
('Horní šuplík', 'Rychle mrazené nebo často používané položky'),
('Dolní šuplík', 'Dlouhodobé uskladnění, velké balení'),
('Dveře mrazáku', 'Malé krabičky a bylinky');

INSERT INTO potravina (nazev, id_kategorie, id_fochu, mnozstvi, jednotka_mnozstvi, datum_expirace, poznamka) VALUES
('Kuřecí prsa', 1, 1, 1.20, 'kg', '2026-05-10', 'Bio, vakuum'),
('Bramborové knedlíky', 3, 2, 6.00, 'ks', '2026-03-20', 'Domácí, z babičky'),
('Brokolice', 2, 1, 800.00, 'g', '2026-02-28', 'Zelenina na polévku'),
('Česnečky', 4, 3, 12.00, 'ks', '2026-07-15', 'Pečivo z pekárny'),
('Losos filety', 1, 2, 0.90, 'kg', '2026-01-30', 'Už brzy expirují!');