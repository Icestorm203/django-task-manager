-- ============================================================
-- SQL Examples for Django Task Manager Project
-- Author: Мустафа Муратов
-- Description: Practical SQL queries including JOINs, filtering,
--              aggregation, and multi-table operations.
-- ============================================================


-- ============================================================
-- 1. BASIC SELECT
-- ============================================================

SELECT * 
FROM tasks_task
ORDER BY id ASC;


-- ============================================================
-- 2. INNER JOIN
--    Join tasks with content types (example of relational join)
-- ============================================================

SELECT t.id,
       t.title,
       t.description,
       ct.model AS content_type
FROM tasks_task AS t
INNER JOIN django_content_type AS ct
       ON ct.id = t.id
ORDER BY t.id;


-- ============================================================
-- 3. LEFT JOIN
--    Show all tasks even if no matching content type exists
-- ============================================================

SELECT t.id,
       t.title,
       ct.model AS content_type
FROM tasks_task AS t
LEFT JOIN django_content_type AS ct
       ON ct.id = t.id;


-- ============================================================
-- 4. JOIN WITH FILTERING
--    Show only open tasks + joined content type
-- ============================================================

SELECT t.id,
       t.title,
       t.is_closed,
       ct.model AS content_type
FROM tasks_task AS t
LEFT JOIN django_content_type AS ct
       ON ct.id = t.id
WHERE t.is_closed = FALSE;


-- ============================================================
-- 5. MULTI-TABLE JOIN
--    Users → User Groups → Groups
--    Demonstrates multi-level JOINs
-- ============================================================

SELECT u.id AS user_id,
       u.username,
       g.name AS group_name
FROM auth_user AS u
INNER JOIN auth_user_groups AS ug
       ON u.id = ug.user_id
INNER JOIN auth_group AS g
       ON ug.group_id = g.id
ORDER BY u.username;


-- ============================================================
-- 6. AGGREGATION (GROUP BY)
--    Count tasks by status
-- ============================================================

SELECT t.is_closed,
       COUNT(*) AS total_tasks
FROM tasks_task AS t
GROUP BY t.is_closed;


-- ============================================================
-- 7. FULL OUTER JOIN
--    Show all tasks + all content types (even without matches)
-- ============================================================

SELECT t.id,
       t.title,
       ct.model AS content_type
FROM tasks_task AS t
FULL OUTER JOIN django_content_type AS ct
       ON ct.id = t.id;


-- ============================================================
-- 8. CROSS JOIN
--    Cartesian product (use carefully)
-- ============================================================

SELECT t.title,
       ct.model
FROM tasks_task AS t
CROSS JOIN django_content_type AS ct;
