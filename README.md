Swag App v1


## Session

In addition to the request object there is also a second object called session which allows you to store information specific to a user from one request to the next. This is implemented on top of cookies for you and signs the cookies cryptographically. What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.


## GSAP

The GreenSock Animation Platform (GSAP) is an industry-celebrated suite of tools used on over 11 million sites, including a ton of award‑winning ones! You can use GSAP to animate pretty much anything JavaScript can touch, in any framework. Whether you want to animate UI, SVG, Three.js or React components - GSAP has you covered.

The core library contains everything you need to create blazing fast, cross-browser friendly animations.


## Alembic

Alembic provides for the creation, management, and invocation of change management scripts for a relational database, using SQLAlchemy as the underlying engine. 

```bash
source /path/to/yourproject/.venv/bin/activate
alembic init alembic
alembic revision --autogenerate -m "Update users table"
alembic upgrade head
```