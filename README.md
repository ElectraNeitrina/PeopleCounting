# PeopleCounting
pre interview concept app

# Article plan:

## State of the art - people counting

 - opencv people counting with raspberry pi: https://pyimagesearch.com/2018/08/13/opencv-people-counter/
 - Terabee industrialized solution: https://www.terabee.com/shop/people-counting/terabee-people-counting-l/
 - another approach - distance sensor based: https://www.terabee.com/shop/industrial-automation/terabee-ind-tof-1/
 - opencv theory, HOG algorithm, people detection: https://thedatafrog.com/en/articles/human-detection-video/

## Your approach to the problem

 - System design with interfaces: start, stop, registerCallback, and a hardware device for counting can be substituted
 - Python counting program interfaces web application through POST method
 - web application runs Node.js inside the Docker container
 - replies to user requests with GET and renders some user friendly data on the website, listens to POST from python system to update the counter
 - theory about contenerization: https://nodejs.org/en/docs/guides/nodejs-docker-webapp
 - another possible technologies: Java https://www.docker.com/blog/how-i-built-my-first-containerized-java-web-application/

## Further steps:

 - improve people counting algorithn: naive approach (frame diff), laser counting approach (square wave), machine learning approach (opencv stuff from the article)
 - improve python - web communication: possibly encrypted, binary protocol, redundant channels in case of medium loss
 - improve web: nice GUI, investigate user needs and implement REST API features


 