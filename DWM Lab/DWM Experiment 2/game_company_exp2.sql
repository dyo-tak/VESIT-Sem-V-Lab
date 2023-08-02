SELECT *
FROM game_stat;

SELECT * FROM spectator
SELECT * FROM game
SELECT * from [location]

--
SELECT SUM(charge) AS ChargeSum, category
FROM spectator
GROUP BY CUBE(spectator.category);

select sum(spec.charge) as ChargeSum, spec.category, g.game_id
from game_stat gs, game g, spectator spec, [location] l
where 
    gs.game_id = g.game_id and
    gs.spec_id = spec.spec_id and 
    gs.loc_id = l.loc_id
group by cube (spec.category, g.game_id)

select sum(spec.charge) as ChargeSum, spec.category, g.game_id, l.stadium
from game_stat gs, game g, spectator spec, [location] l
where 
    gs.game_id = g.game_id and
    gs.spec_id = spec.spec_id and 
    gs.loc_id = l.loc_id
group by cube (spec.category, g.game_id, l.stadium)


--ROLLUP
SELECT SUM(spec.charge) as ChargeSum, spec.category, g.game_id, l.stadium
FROM game_stat gs
JOIN game g ON gs.game_id = g.game_id
JOIN spectator spec ON gs.spec_id = spec.spec_id
JOIN location l ON gs.loc_id = l.loc_id
GROUP BY rollup(spec.category, g.game_id, l.stadium);

SELECT SUM(spec.charge) as ChargeSum, spec.category, g.game_name
FROM game_stat gs
JOIN game g ON gs.game_id = g.game_id
JOIN spectator spec ON gs.spec_id = spec.spec_id
GROUP BY rollup(spec.category, g.game_name);

--slice
SELECT SUM(spec.charge) as ChargeSum, spec.category, g.game_id, l.stadium
FROM game_stat gs
JOIN game g ON gs.game_id = g.game_id
JOIN spectator spec ON gs.spec_id = spec.spec_id
JOIN location l ON gs.loc_id = l.loc_id
GROUP BY rollup(spec.category, g.game_id, l.stadium)
HAVING spec.category = 'student';

SELECT SUM(spec.charge) as ChargeSum, spec.category, g.game_id, l.stadium
FROM game_stat gs
JOIN game g ON gs.game_id = g.game_id
JOIN spectator spec ON gs.spec_id = spec.spec_id
JOIN location l ON gs.loc_id = l.loc_id
GROUP BY rollup(spec.category, g.game_id, l.stadium)
HAVING g.game_id = 3;

SELECT SUM(spec.charge) as ChargeSum, spec.category, g.game_id, l.stadium
FROM game_stat gs
JOIN game g ON gs.game_id = g.game_id
JOIN spectator spec ON gs.spec_id = spec.spec_id
JOIN location l ON gs.loc_id = l.loc_id
GROUP BY rollup(spec.category, g.game_id, l.stadium)
HAVING l.stadium = 'd y patil';

