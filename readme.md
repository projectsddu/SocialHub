
# SocialHub 


<h3><b>Introduction</b></h3>

This project was developed under the Software Project-1 of the coursework by Jenil Gandhi
and Keval Gandevia under the guidance of Prof Pinkal Chauhan,Prof Brijesh Bhatt,Prof Jigar Pandya.We made the application transfer to the <b>ASGI(Asynchronus Gateway Interface)</b> application to support the Asynchronus calls.

<h3>The project involves following technology Stack:</h3>
<ul>
<li><b>Backend</b>:  Django</li>
<li><b>Frontend</b>: Django Templates</li>
<li><b>AJAX</b></li>
<li><b>JQuery</b></li>
<li><b>Chat server</b>: Django Channels</li>
<li><b>Django Humanize extension</b></li>
</ul>

## How to run the project:
---


### Step 1
requirement.txt  ----------------- pendin

### Step2
Go to https://download.docker.com/linux/ubuntu/dists/, choose your Ubuntu version, then browse to pool/stable/, choose amd64, armhf, or arm64, and download the .deb file for the Docker Engine version you want to install.

$ sudo dpkg -i /path/to/package.deb


### Step3
docker run -p 6379:6379 -d redis:5


### Step4 
python manage.py runserver


---
---
<h2><b>Why we used django channels</b></h2>
The reason we used django channels was on normal implementation of chat feature had certain
drawbacks like the new messages were only available on the reload of the page otherwise making
multiple ajax calls was not a good idea as it increased the load on server . So we searched
about realtime apps and we found that <b>WebSocket</b> was the thing we needed.
Channels provide with the real time connection with the frontend . It updated the frontend
as soon as 
---

## SocialHub - A Social Media Website
# SocialHub
## Our main project is in current resository itself.
### for lab experiment follow this link: https://github.com/projectsddu/Lab_Experiment

