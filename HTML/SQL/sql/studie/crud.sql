USE company;

-- =====================================
-- SELECT
-- Výpis všech serverů a jejich
-- operačních systémů
-- =====================================
SELECT id, name, os, os_ver
FROM servers;


-- =====================================
-- INSERT
-- Vložení nového serveru do tabulky
-- servers
-- =====================================
INSERT INTO servers (name, os, os_ver)
VALUES ('srv-test-01', 'Ubuntu Server', '24.04 LTS');


-- =====================================
-- UPDATE
-- Změna verze operačního systému u
-- konkrétního serveru
-- =====================================
UPDATE servers
SET os_ver = '24.04.1 LTS'
WHERE name = 'srv-test-01';


-- =====================================
-- DELETE
-- Smazání testovacího serveru podle
-- názvu
-- =====================================
DELETE FROM servers
WHERE name = 'srv-test-01';
