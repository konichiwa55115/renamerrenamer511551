#Thank you LazyDeveloper for helping me in this journey !
#Must Subscribe On YouTube @LazyDeveloperr
# Python Based Docker
# Python Based Docker
FROM python:latest

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

# Updating Pip Packages
RUN pip3 install -U pip

# Copying Requirements

# Installing Requirements
RUN pip3 install -U -r requirements.txt
WORKDIR renamerrenamer511551



# Running MessageSearchBot
CMD ["python3", "bot.py"]
