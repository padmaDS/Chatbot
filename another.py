import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo-0125"):
    messages = [{"role": "user", "content": prompt}]
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return completion.choices[0].message.content

query = """
Sir , 
        I  married my late husband Sh Mahendra Kumar  Jain (son of  Late Sh Bhura Mal Jain ) who was a permanent resident of 929, Kisan Marg, Barket Nagar , Tonk Phatak , Jaipur   on 16 April 1971, at Jaipur ( Raj ) , and subsequently our  3 sons were born .My husband was working as Police Inspector , (Post &amp; Telecommunication ) , Rajasthan Police .Subsequently , he left police job and started working in the computer science department , University of Rajasthan  and also used to work as homeopathic and biochemic medicine consultant. Around 20 years back ,  he left the Univ job and used to travel and work at various places outside Rajasthan  like Calcutta , Guwahati , Assam etc regarding Homeopathic , biochemic , naturopathy treatment and also work related to computer software  .  He was working for gain at Guwahati and as he had been living here at Guwahati in connection with his service , he had purchased a flat ( in the year 2014 )Flat No.2 D situated in the multistoried building Pink Arcade standing over a plot of land covered by Dag No.55 and 765 of K.P. Patta No.80 and 456 of revenue village- Sahar Sarania Part-I, Mouza- Ulubari, situated at K.C. Sen Road, Paltan Bazar, Guwahati   out of his family fund .    My husband Sh Mahendra Kumar Jain expired  at Jaipur, Rajasthan  on 15th March 2020 . Mahendra Jain , along with my 3 sons , are the legal heirs of my husband. 
After my husband expired , I applied for mutation of the land in his name vide Mission Basundhara Application id  XBXMXTX/X0X1X4X5X, and   XBXMXTX/X0X1X3X7X0X . However , both my applications have been rejected by the circle officer Guwahati Revenue circle without assigning any reason . Subsequently I filed an appeal against it with the Deputy Commissioner Kamrup (M ). A govt letter from the revenue &amp; DM  (LR )RLR.122/2012/134A  was also issued in this regard . However,  I am sorry to state that there has been little /  no progress  after registering my complaints and no resolution has been provided  .
Attached :
1 Death certificate of Sh M.K. Jain depicting my name as wife

Regards ,
Sudha Jain
( wife of Sh M. k . Jain )
929 , Barket Nagar , Kisan Marg ,
Jaipur (Raj ) 302015"""

details = f"""
You are helpful assistant, designed to suggest the respective department,
based on user query
provide output in JSON format

'''{query}'''

"""

department = get_completion(details)
print(department)