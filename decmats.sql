CREATE TABLE decmats(
type varchar,
n int,
d int,
blocklabels varchar,
blocks varchar,
condition varchar,
decmat varchar,
hc_series varchar,
ordinary varchar,
origin varchar,
recipe varchar);

/* import json to db */
CREATE TABLE tmp (c text);

DecMats=# \copy tmp from 'data.json'

INSERT INTO decmats 
SELECT q.* FROM tmp, json_populate_record(null::decmats, c::json) AS q;