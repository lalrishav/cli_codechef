import requests
from BeautifulSoup import BeautifulSoup

#print("");

while(1):
    user = raw_input("Enter the handle of the user:-")

    url = "https://www.codechef.com/users/"+str(user)
    print(url)
    try:
        response = requests.get(url)
        print "-------------------------------------------"
        
        print "connected"
    except:
        print('connectivity problem or no such handle found')
        continue
    html = response.content
    
    soup = BeautifulSoup(html)
    print soup

    try:
        table = soup.find('section',attrs={'class':'rating-data-section problems-solved'}).find('div',attrs={'class':'content'}).find('h5')
        s="";
        s=s+table.text[14]
        i=15
        while(table.text[i]!=')'):
            s=s+table.text[i]
            i=i+1
            
        print("The total problem solved is :- " + s)
        print("\n")
        rating = soup.find('div',attrs={'class':'rating-number'})
        print("Overall rating:- " + rating.text)
       
            
    except:
        print('No such user found')
        continue



