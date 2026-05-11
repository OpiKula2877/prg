USE company;

-- =====================================
-- INSERT: SERVERS
-- =====================================

INSERT INTO servers (name, os, os_ver) VALUES
('srv-web-01',  'Ubuntu Server', '22.04 LTS'),
('srv-web-02',  'Ubuntu Server', '22.04 LTS'),
('srv-db-01',   'Debian',        '12'),
('srv-mail-01', 'Rocky Linux',   '9.3'),
('srv-dev-01',  'Windows Server','2022');


-- =====================================
-- INSERT: SERVICES
-- =====================================

INSERT INTO services (name, s_type, s_ver) VALUES
('Nginx',        'síťová',     '1.24'),
('MariaDB',      'aplikační',  '10.11'),
('Postfix',      'síťová',     '3.8'),
('Docker',       'aplikační',  '26.1'),
('Node.js API',  'aplikační',  '20 LTS'),
('Prometheus',   'aplikační',  '2.52');


-- =====================================
-- INSERT: SERVICES RUNNING ON SERVERS
-- =====================================

INSERT INTO services_running_on_servers
(servers_id, services_id, domain, IPv4, IPv6, port, protocol, deploy_date, status)
VALUES

-- WEB SERVER 01
(
 (SELECT id FROM servers WHERE name='srv-web-01'),
 (SELECT id FROM services WHERE name='Nginx'),
 'www.company.local', '10.0.10.11', NULL, 80, 'HTTP', '2026-01-02', 'Running'
),
(
 (SELECT id FROM servers WHERE name='srv-web-01'),
 (SELECT id FROM services WHERE name='Node.js API'),
 'api.company.local', '10.0.10.11', NULL, 3000, 'HTTP', '2026-01-31', 'Stopped'
),
(
 (SELECT id FROM servers WHERE name='srv-web-01'),
 (SELECT id FROM services WHERE name='Docker'),
 NULL, '10.0.10.11', NULL, NULL, NULL, '2026-01-05', 'Installed'
),

-- WEB SERVER 02
(
 (SELECT id FROM servers WHERE name='srv-web-02'),
 (SELECT id FROM services WHERE name='Nginx'),
 'shop.company.local', '10.0.10.12', NULL, 443, 'HTTPS', '2026-01-02', 'Running'
),
(
 (SELECT id FROM servers WHERE name='srv-web-02'),
 (SELECT id FROM services WHERE name='Docker'),
 NULL, '10.0.10.12', NULL, NULL, NULL, '2026-01-02', 'Running'
),

-- DB SERVER
(
 (SELECT id FROM servers WHERE name='srv-db-01'),
 (SELECT id FROM services WHERE name='MariaDB'),
 NULL, '10.0.20.10', NULL, 3306, 'TCP', '2026-01-02', 'Running'
),
(
 (SELECT id FROM servers WHERE name='srv-db-01'),
 (SELECT id FROM services WHERE name='Prometheus'),
 NULL, '10.0.20.10', NULL, 9090, 'HTTP', '2026-01-02', 'Running'
),

-- MAIL SERVER
(
 (SELECT id FROM servers WHERE name='srv-mail-01'),
 (SELECT id FROM services WHERE name='Postfix'),
 'mail.company.local', '10.0.30.5', NULL, 25, 'SMTP', '2026-01-02', 'Running'
),

-- DEV SERVER
(
 (SELECT id FROM servers WHERE name='srv-dev-01'),
 (SELECT id FROM services WHERE name='Docker'),
 NULL, '10.0.40.15', NULL, NULL, NULL, '2026-01-02', 'Running'
),
(
 (SELECT id FROM servers WHERE name='srv-dev-01'),
 (SELECT id FROM services WHERE name='Node.js API'),
 'dev-api.company.local', '10.0.40.15', NULL, 3001, 'HTTP', '2026-01-02', 'Running'
);
