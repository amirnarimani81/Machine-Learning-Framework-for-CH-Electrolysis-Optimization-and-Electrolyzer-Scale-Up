# Creat dataset
create database Electrolyzer_db

# choose dataset
use Electrolyzer_db
GRANT ALL PRIVILEGES ON electrolyzer_db.* TO 'amir'@'localhost';
 FLUSH PRIVILEGES;

# Query
  select * from preprocessed ;

# solve null
SELECT * FROM preprocessed WHERE voltage IS NULL;

SELECT * FROM preprocessed WHERE voltage IS NOT NULL;

UPDATE preprocessed SET voltage = 0 WHERE voltage IS NULL;

# SHOW COLUMNS FROM preprocessed;


# Yield Efficiency (Yield per Reaction Time)
 SELECT cathod_catalyst, Methanol_Yield_micromol_ml_ / Reaction_Time_hr AS efficiency FROM preprocessed ;

# Catalyst Metal Composition Summary
SELECT
    process_type,
    AVG(Pt_atpercent_in_metal_element) AS avg_pt,
    AVG(Ni_atpercent_in_metal_element) AS avg_ni,
    AVG(Co_atpercent_in_metal_element) AS avg_pd
FROM preprocessed
GROUP BY process_type

# Detect Duplicate Experimental Conditions
SELECT 
    cathod_catalyst, anode_catalyst, Voltage_V, CH4_Flow_rate_sscm,
    COUNT(*) AS duplicates
FROM preprocessed
GROUP BY 
    cathod_catalyst, anode_catalyst, Voltage_V,
    CH4_Flow_rate_sscm
HAVING COUNT(*) > 1