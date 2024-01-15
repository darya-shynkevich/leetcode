# Design a call center
## Constraints and assumptions
1. What levels of employees are in the call center?
Operator, supervisor, director
2. Can we assume operators always get the initial calls?
Yes
3. If there is no available operators or the operator can't handle the call, does the call go to the supervisors?
Yes
4. If there is no available supervisors or the supervisor can't handle the call, does the call go to the directors?
Yes
5. Can we assume the directors can handle all calls?
Yes
6. What happens if nobody can answer the call?
It gets queued
7. Do we need to handle 'VIP' calls where we put someone to the front of the line?
No
8. Can we assume inputs are valid or do we have to validate them?
Assume they're valid

## Thoughts

Users make calls;
Operators, Supervisors, Directors will try to answer;
IF nobody is available => call is queued;