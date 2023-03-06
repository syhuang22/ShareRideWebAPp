# Django Web-App: Ride Sharing Service
This web-app will let users
request, drive for, and join rides. <br>
To get started, run the below command in docker-deploy directory<br>
`sudo docker-compose up`
## Ride Owner

When a user requests a ride, he/she becomes the owner of that ride. Requesng
a ride should involve specifying a desnaon address, a required arrival (date & me), the
number of total passengers from the owner’s party, and oponally, a vehicle type and any other
special requests1
. A request will also indicate whether this ride can be shared or not – a shared
ride can be joined by other users (ride sharers). A ride owner would be able to modify a ride
request up unl it is confirmed (a ride becomes confirmed once a driver accepts the ride and is
in route). A ride is open from the me it is requested unl that point. A ride owner can also
view ride status unl the ride is complete (a ride becomes closed once a driver finishes the ride
and marks it as complete).


## Ride Driver
– A user can register as a driver, and in doing so will provide their name along with
their vehicle informaon. The vehicle informaon includes the type, license plate number,
maximum number of passengers, and oponally any other special vehicle info
1
. To simplify, a
driver can only have 1 vehicle. A driver can search for open ride requests based on the ride
request aributes. A driver can claim and start a ride service, thus confirming it. A driver can
also complete rides that they service aer reaching the desnaon to indicate that the ride is
finished.

## Ride Sharer
– A user can search for open ride requests by specifying a desnaon, arrival
window (the user’s earliest and latest acceptable arrival date & me) and number of passengers
in their party. The user can then become a ride sharer, by joining that ride. A ride sharer can
also view the ride status, similarly to a ride owner. Finally, a ride sharer can edit their ride status
as long as the ride is open.
Note that your system should support mulple rides, and the same user MAY hold different
roles in different rides. For example, a user may be an owner of a current ride, a ride sharer on
yet a later ride in the day, and a driver of 2 rides scheduled for the following day.

## Features

**Create Account** – A user should be able to create an account if they do not have one.<br><br>
**Login/Logout** – A user with an account should be able to login and logout.<br><br>
**Driver Registraon** – A logged-in user should be able to register as a driver and enter their
personal and vehicle info. They should also be able to access and edit their info.<br><br>
**Ride Selecon** – If a logged-in user is part of mulple rides, she should be able to select which
ride she wants to perform acons on. If a logged in user belongs to only one ride, you MAY
display your ride-selecon mechanism with the one ride, or you MAY omit it (not show it). Note
this should allow selecon of any open or confirmed rides for that user (but not complete rides).<br><br>
**Ride Requesng** – A logged-in user should be able to request a ride. Requesng a ride should
allow the owner to specify the desnaon address, a required arrival date / me, the number of
total passengers from their party, a vehicle type (oponally), whether the ride may be shared by
other users or not, and any other special requests.<br><br>
**Ride Request Eding (Owner)** – A ride owner should be able to edit the specific requested
aributes of the ride as long as the ride is not confirmed.<br><br>
**Ride Status Viewing (Owner / Sharer)** – A ride owner or sharer should be able to view the
status of their non-complete rides. For open ride requests, this should show the current ride
details (from the original request + any updates due to sharers joining the ride). For confirmed
ride requests, the driver and vehicle details should also be shown.<br><br>
**Ride Status Viewing (Driver)** – A ride driver should be able to view the status of their confirmed
rides, which should show the informaon for the owner and each sharer of the ride, including
the number of passengers in each party. A driver should also be able to edit a ride to mark it as
complete.<br><br>
**Ride Searching (Driver)** – A driver should be able to search for open ride requests. Only requests
which fit within the driver’s vehicle capacity and match the vehicle type and special request info
(if either of those were specified in the ride request) should be shown. A driver can claim and
start a ride service, thus confirming it. Once closed, the ride owner and each sharer should be
nofied by email that the ride has been confirmed (hence no further changes are allowed).<br><br>
**Ride Searching (Sharer)** – A user should be able to search for open ride requests by specifying a
desnaon, arrival window (the user’s earliest and latest acceptable arrival me) and number
of passengers in their party. A sharer should be able to join a selected ride, if any exist in the
resulng list of pending rides.
