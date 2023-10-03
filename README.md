# Problem E. Evil Forest
###### https://codeforces.com/gym/104207
###### https://codeforces.com/gym/104207/attachments/download/19250/statement.pdf
###### 2017 CCPC Final Contest Onsite Round, Sunday, December 3rd, 2017

###### others
* https://vjudge.net/problem/HDU-6247
* https://www.geeksforgeeks.org/difference-between-input-and-sys-stdin-readline/
* https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
* https://stackoverflow.com/questions/31099452/runtime-error-on-test-1-codeforces
* https://codeforces.com/blog/entry/46459

##### The Bear, king of the forest, loves painting very much. His masterpiece – “Back in time” is very famous around all over the forest. Recently he wants to hold a series painting competition to select those animals who are good at painting as well. So the Bear appoints his minister Tiger to help him prepare the painting competitions.  Tiger owns a stationery factory which produces sketchpad, so he wants to let all the competitions use the sketchpads produced by his factory privately. The Bear plans to hold N painting competitions, and informs Tiger of the number of competitors who are ready for each competition. One competitor needs only one sketchpad in one competition. For each competition, at least 10% extra sketchpads are required as backup just in case. The Tiger assigns you, his loyal subordinate to calculate the minimum number of sketchpads produced by his factory.

#### Input
* The first line of the input gives the number of test cases, T. T test cases follow.
* For each test case, the first line contains an integer N, where N is the number of competitions. The next line contains N integers a1, a2, . . . , aN representing the number of competitors in each competition.

#### Output
* For each test case, output one line containing “Case #x: y”, where x is the test case number (starting from 1) and y is the minimum number of sketchpads that should be produced by Tiger’s factory.

##### Limits
* 1≤T ≤100.
* 1 ≤ N ≤ 1000.
* 1≤ai ≤100.

##### Example Note
standard input

    1
    6
    13 11 11 11 13 11

standard output

    Case #1: 82

Note:
    For the first test case, two more sketchpads should be prepared for each painting competition.
