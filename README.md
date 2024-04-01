# Age Of Empires 2 ETL
![alt text](https://github.com/KevsDe/de_aoe2_games_data_pipeline/blob/main/screenshots/banner.jpg?raw=true)
## About the project:
As an AOE2 player I like to see my statistics and look how the top players are performing in ohter to keep learning and improving. Every player generates data with every single match about maps, civilizations and game modes.
The goal of the project is practice the skills learned during the DataTalks.Club Data Engineering Zoomcamp and get data ready to generate insights.

**This project was made for learning and fun purposes**

## About the ETL:
![alt text](https://github.com/KevsDe/de_aoe2_games_data_pipeline/blob/main/screenshots/mage_etl.png?raw=true)

- The data was obtained with a web scraping script from https://www.aoe2insights.com/
- Transformartion were made within the pipeline filtering out missing data, formating and casting.
- Finally the data was loaded into Google Big Query
- As an extra step, a new table is crated fixing a user_name error in the website, partitioning by match_date and clustering by player_profile 
![alt text](https://github.com/KevsDe/de_aoe2_games_data_pipeline/blob/main/screenshots/final_table.png?raw=true)
## About the execution:
- Mage is deployed on Google Cloud using Terraform
- Batch processing
![alt text](https://github.com/KevsDe/de_aoe2_games_data_pipeline/blob/main/screenshots/batch.png?raw=true)
![alt text](https://github.com/KevsDe/de_aoe2_games_data_pipeline/blob/main/screenshots/triggers.png?raw=true)

- In order to deploy Mage it is necessary to set up your cloud enviroment or running it locally
- The terraform templates are available in mage Github

## Viz and insights:
 - Finally big query table is connected to Looker data studio and prepared a simple dashbord for in game insights


![](https://github.com/KevsDe/de_aoe2_games_data_pipeline/blob/main/screenshots/dashboard.gif?raw=true)

**From Madrid (L)**
