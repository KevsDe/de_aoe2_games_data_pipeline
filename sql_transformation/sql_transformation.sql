CREATE OR REPLACE TABLE `spry-device-413.aoe_insights.aoe_matches`
PARTITION BY match_date
CLUSTER BY player_profile
AS

SELECT
extraction_date,
CAST(match_date AS date) AS match_date,
CASE 
WHEN player_profile = '234479' THEN 'Locoser'
WHEN player_profile = '199325' THEN 'Hera'
WHEN player_profile = '666976' THEN 'Barles'
WHEN player_profile = '347269' THEN 'ACCM'
WHEN player_profile = '196240' THEN 'TheViper'
WHEN player_profile = '2783660' THEN 'Sebastian'
ELSE user_name
END AS user_name,
 *EXCEPT(user_name,extraction_date,match_date)
FROM `spry-device-413.aoe_insights.match_data` 