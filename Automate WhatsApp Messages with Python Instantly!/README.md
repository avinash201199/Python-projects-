### 1.Create a new project in code editor

After installation, create a new project in code editor, give it the desired name. The most crucial part is choosing Python as a file type. <br>

### 2. Install pywhatkit

open a terminal in the code editor window and paste the following code <br>
  `pip install pywhatkit`
  
## Some Features of pywhatkit
*Sending Message to a WhatsApp Group or Contact
*Sending Image to a WhatsApp Group or Contact
*Converting an Image to ASCII Art
*Converting a String to Handwriting
*Playing YouTube Videos
*Sending Mails with HTML Code


### 3. Type in the following code

` #import the downloaded library in python <br>
import pywhatkit <br>
#pywhatkit.sendwhatmsg():Runs a function from the imported library<br>
pywhatkit.sendwhatmsg("+9185000000", "avinash",23,5)<br>

#syntax: pywhatkit.sendwhatmsg("reciver no. with country code",<br>
# message, hours, minutes) `

Run the code, and you will find a message saying something like this: <br>
`In 50 seconds, web.WhatsApp.com will open, and after 20 seconds, a message will be delivered by Whatsapp.`

WhatsApp's web version will open and send a message to the given number at the specified time.
