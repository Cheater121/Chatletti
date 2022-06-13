# Chatletti
This application is planned as a simple messenger (prototype) in Python that can receive, process and send text messages. It plans to implement two functions - sending and receiving messages. The application will consist of two parts: server and client (client-server application). In development, it is planned to use the Flask framework (for the backend part), and PyQT6 (for the client / frontend). This is my first project after learning Python syntax, the purpose of which is to consolidate knowledge, as well as practice working with Git and running my application. Thanks for reading.
Api for app (later will be update):
 - to send message (/api/messenger) JSON must have 4 properties: 
     - "Username" (string, min length 1);
     - "Recipient" (string, min Length 1);
     - "Timestamp" (string, date-time format "YYYY-MM-DDTHH-MM-SS");
     - "Messagetext" (string, min Length 1).
 - to get message (/api/measenger/<username> from server you need to send Get-request to server. 
