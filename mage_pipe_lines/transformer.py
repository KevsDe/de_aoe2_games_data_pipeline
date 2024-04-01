import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data.dropna()

    month_dict = {
    "January": "01",
    "Jan.": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
    "Jan.": "01",
    "Feb.": "02",
    "Mar.": "03",
    "Apr.": "04",
    "May.": "05",
    "Jun.": "06",
    "Jul.": "07",
    "Aug.": "08",
    "Sept.": "09",
    "Oct.": "10",
    "Nov.": "11",
    "Dec.": "12"
    }


    def format_date(dt_string):
        d = dt_string
        
        d_s = d.replace(',','').strip().split()
        
        if d_s[0] in month_dict:
            d_s[0] = month_dict[d_s[0]]
        d_s = d_s[:3]    
        d_s = '-'.join(d_s)

        return d_s


    data['match_date'] = data['match_date'].apply(format_date)
    data['match_date'] = pd.to_datetime(data['match_date']).dt.strftime('%Y-%m-%d')
    data['extraction_date'] = pd.to_datetime(data['extraction_date'],format='%Y-%m-%d')

    ###

    def get_duration(duration):
    
        d = duration
        
        d = d.replace('m','').replace('s','').split()
        
        seconds = (int(d[0])*60) + int(d[1])
        minutes = round(seconds/60,1)
        
        return minutes

    data['match_length'] = data['match_length'].apply(get_duration)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
