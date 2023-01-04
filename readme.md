Alright, let me show you my implementation for this problem. I will try to keep it short and concise, so that it’s feasible to complete during the tech interview, which is about 45 to 60 minutes. I am sure that there are better solutions out there, but here is my approach.

First let’s identify the problem’s requirements. Usually, the basic requirements for this problem are:

The elevator can go up and down in a real-world fashion.
Users can send requests to the elevator from both outside and inside the elevator.
The first requirement is a bit vague, so let me break it down. A real-world elevator has the following behaviours:

When elevator is going up or down, it will stop at all the floors that the users requested.
If the elevator received a request of going down while it is going up, the elevator will go to the highest floor in the current requests, and then go down.
Users can send requests at anytime.
After understanding the requirement, we can start with our design. From the analysis above, we know that elevator needs to sort the requests by some kind of order. It’s not by timestamp, because if elevator is at floor 1, and customer A wants to go to floor 4, and B wants to go to floor 2, the elevator should not go to floor 4 first just because A sent the request first. Instead, the elevator should stop at floor 2 and let B out, then go to floor 4 to let A out. Thus, we know that the request should be sorted by the distance from the current floor and not by timestamp.

## Assumptions
Now, in real life, the elevator will finish all up requests before starting down requests. Let’s assume that going up has more priority than going down, which means that when the elevator is in IDLE state, and has both up and down requests, it will execute up requests first.

I used a max heap to store all down requests and sort them by their desired floor. Similarly, a min heap to store all up requests and sort them by their desired floor.

When, the requester is outside of the elevator, the elevator needs to stop at the currentFloor of the requester, before going to the desiredFloor of the requester.

Here is the elevator class implementation after keeping all the above in mind.