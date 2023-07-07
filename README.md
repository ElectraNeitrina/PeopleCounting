# PeopleCounting
pre interview concept app

# The idea and what was done

1)The system design is working with interfaces: start, stop, registerCallback, and a hardware device for counting; those features have been tested during the beginning steps;
2)The system uses simple threshold method (differences between pictures). It requires to have a reference (gray) frame and every time do "||newFrame - refFrame|| > threshold => count a person (1)"
3) A value of normMatrix can help to understand the threshold value to tune the system; in the example of ref picture ("refFrame.png") the value of the normMatrix without a person (object) is around 57k and with a person around 80k. This difference used to detect a person (object). 
4) Python counting program interfaces web application through the POST method;
5) Web application runs Node.js inside the Docker container
6) Replies to user requests with GET and renders user-friendly GUI (table) on the website, listens to POST from python system to update the counter; a possibility to compare a data was implemented by a button, which is switching "simulated" and "live data".
7) Public transport operators are identified by ID, they have Name, they have Description, and they can have collection of Vehicles (fleet) - configured by many-2-many relation in fleetConfiguration
8) Vehicles are identified by ID, they have Name, they have PeopleCounter (subject to live changes), they Have description, and they can be associated with transport company (let's assume 2 transport companies can share a vehicle, because why not); so again many-2-many relation described in fleetConfiguration


 
