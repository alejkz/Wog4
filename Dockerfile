#Create a ubuntu base image with python 3 installed.
FROM python:3

#Set the working directory
WORKDIR /home/alejkz/Desktop/WorldOfGames 

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 5001

#Run the command
CMD [“python3”, “./MainScore.py”]
