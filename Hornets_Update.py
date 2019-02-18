
# coding: utf-8

# In[1]:


#import pandas
import pandas as pd
#define our URL we want to scrape from and create a dataframe in pandas 
url = 'https://www.cbssports.com/nba/standings/'
tables = pd.read_html(url)
df = tables[0]
df.columns = ['Rank','Team','Wins','Losses','Win Percentage','Games behind','Points scored average',
              'Points allowed average','Point-differential','Home record','Road record',
              'Record against division opponents','Record against conference opponents','Streak',
             'Previous 10-games record','Wins projection','Division winner projection','Postseason projection']
df
#manipulate the data to obtain the information we need. 
Hornets_rank = df.loc[df['Team'] == 'Charlotte']
Hornets_rank
new_standing = Hornets_rank.iat[0,0]
conversion = int(new_standing)
update = (f'The Charlotte Hornets are in {conversion}th place in the East.')

#twilio function that sends me the text message
def textme():
    from twilio.rest import Client
    from config import account_sid, auth_token

    client = Client(account_sid, auth_token)
    
    message = client.messages                 .create(
                     body= str(update),
                     from_='TWILIO PHONE NUMBER',
                     to='MY PHONE NUMBER '
                 )

    print(message.sid)

#call the function
textme()

