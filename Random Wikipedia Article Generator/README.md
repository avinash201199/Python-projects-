## Random Wikipedia Article Generator

This python acript uses Beautiful Soup wo generate a random Wikipedia article and then if the user likes that article will open it in the web browser. 
Otherwise the program will continue to run and generate random articles. For this program I used this to generate a random article from wikipedia.
This link generates a random article everytime it is clicked. So after parsing this link the same link cannot be used twice for openning after getting the user's choice,
so the link had to be stored before showing the title. So I had to use a while true loop encompasing all of it. Then simply the openning of the url based on the user's choice
is left to the last if-else part.<br>
