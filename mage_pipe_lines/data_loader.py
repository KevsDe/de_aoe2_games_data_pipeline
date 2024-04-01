import requests 
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    # Getting players profiles 
    response = requests.get('https://www.aoe2insights.com/leaderboard/3/')
    soup = BeautifulSoup(response.content, 'html.parser')
    profiles = ['/user/272182/', '/user/234479/','/user/199325/', '/user/582058/','/user/197964/', '/user/666976/', '/user/208393/', '/user/347269/', \
    '/user/196240/', '/user/251265/', '/user/2783660/', '/user/9555704/', '/user/12298351/']
    players_profiles = ['https://www.aoe2insights.com' + x for x in profiles]


    # Getting matches info
    n = 1
    all_games = []
    for p in players_profiles:
        print('---Work started---')
        print(f'Working on profile {p}, {n} of {len(players_profiles)}')
        # Total pages in the profile
        player_matches = p + 'matches/?page=1'
        response = requests.get(player_matches)
        soup = BeautifulSoup(response.content, 'html.parser')
        total_pages = max([int(x.text.strip()) if x.text.strip().isdigit() else 0 for x in soup.find_all(class_='page-link')])
        user_name = soup.find(class_='text-center position-relative').text.split()[0]


        for m in range (1, total_pages+1):
            #print(f'page {m} of {total_pages}')
            player_matches_n = p + f'matches/?page={m}'
            response = requests.get(player_matches_n)
            soup = BeautifulSoup(response.content, 'html.parser')
            matches = soup.find_all(class_= 'match-tile')

            for idx in range(len(matches)):
                match_id = matches[idx].find(class_='stretched-link').get('href').replace('/match/', '').replace('/', '')
                w_team =  matches[idx].find(class_='team list-unstyled won')
                l_team =  matches[idx].find(class_='team list-unstyled')



                match_dict = {
                'extraction_date' : datetime.today().strftime('%Y-%m-%d'),
                'user_name' : user_name,
                'player_profile' : p.split('/')[-2],
                'match_id' : match_id,
                'game_mode' : matches[idx].find(class_='stretched-link').text.replace('\n', '').replace(' ', ''),
                'map' : matches[idx].find_all(class_='d-flex flex-column')[0].find_all('div')[1].text.strip(),
                'match_date' : matches[idx].find_all(class_='d-flex flex-column')[0].find(class_='mt-2').find('span').get('title'),
                'match_length' : matches[idx].find(class_='mt-2').find_all('div')[0].text.strip()}
                try:
                    if len(matches[idx].find(class_='team list-unstyled won').find_all('a')) >1:
                        
                        match_dict['w_p_user'] = [x.text.strip() for x in w_team.find_all('a')]
                        match_dict['w_p_civ'] = [x.get('title') for x in w_team.find_all(class_='image-icon')]
                        match_dict['w_p_id'] = [x.get('href').replace('user', '').replace('/', '') for x in w_team.find_all('a')]                  
                        match_dict['l_p_user'] = [x.text.strip() for x in l_team.find_all('a')]
                        match_dict['l_p_civ'] = [x.get('title') for x in l_team.find_all(class_='image-icon')]
                        match_dict['l_p_id'] = [x.get('href').replace('ser', '').replace('/', '') for x in l_team.find_all('a')]
                    else:
                        match_dict['w_p_user'] = [x.text.strip() for x in w_team.find_all('a')][0]
                        match_dict['w_p_civ'] = [x.get('title') for x in w_team.find_all(class_='image-icon')][0]
                        match_dict['w_p_id'] = [x.get('href').replace('user', '').replace('/', '') for x in w_team.find_all('a')][0]
                        match_dict['l_p_user'] = [x.text.strip() for x in l_team.find_all('a')][0]
                        match_dict['l_p_civ'] = [x.get('title') for x in l_team.find_all(class_='image-icon')][0]
                        match_dict['l_p_id'] = [x.get('href').replace('user', '').replace('/', '') for x in l_team.find_all('a')][0]
                except:
                    pass
                
                all_games.append(match_dict)
        n+=1

    print('---Work done---')

    df = pd.DataFrame(all_games)

    return df 


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
