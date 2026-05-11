USE company;

-- =====================================
-- 1) JOIN
-- Výpis serverů a jejich nasazených
-- služeb
-- =====================================
SELECT
    servers.name,
    services.name,
    services_running_on_servers.port
FROM services_running_on_servers
JOIN servers
    ON services_running_on_servers.servers_id = servers.id
JOIN services
    ON services_running_on_servers.services_id = services.id;


-- =====================================
-- 2) JOIN + agregační funkce (COUNT)
-- Počet nasazených služeb na
-- jednotlivých serverech
-- =====================================
SELECT
    servers.name,
    COUNT(services_running_on_servers.services_id) AS services_count
FROM servers
LEFT JOIN services_running_on_servers
    ON servers.id = services_running_on_servers.servers_id
GROUP BY servers.id, servers.name
ORDER BY services_count DESC;



-- ======================================
-- 3) Agregační funkce (COUNT + GROUP BY)
-- Počet serverů podle operačního systému
-- ======================================
SELECT
    os,
    COUNT(*) AS servers_count
FROM servers
GROUP BY os
ORDER BY servers_count DESC;



-- =====================================
-- 4) Vnořený dotaz (SUBQUERY)
-- Servery, na kterých běží služba s
-- konkrétním ID
-- =====================================
SELECT name
FROM servers
WHERE id IN (
    SELECT servers_id
    FROM services_running_on_servers
    WHERE services_id = (
        SELECT id
        FROM services
        WHERE name = 'Nginx'
    )
);



-- =====================================
-- 5) UNION
-- Spojení seznamu domén a IPv4 adres
-- =====================================
SELECT domain AS endpoint
FROM services_running_on_servers
WHERE domain IS NOT NULL

UNION

SELECT IPv4 AS endpoint
FROM services_running_on_servers
WHERE IPv4 IS NOT NULL;
