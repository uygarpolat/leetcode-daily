"""
3433. Count Mentions Per User

You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.

Each events[i] can be either of the following two types:

Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
This event indicates that a set of users was mentioned in a message at timestampi.
The mentions_stringi string can contain one of the following tokens:
id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
ALL: mentions all users.
HERE: mentions all online users.
Offline Event: ["OFFLINE", "timestampi", "idi"]
This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.

Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.

Example 1:

Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 71, id0 comes back online and "HERE" is mentioned. mentions = [2,2]

Example 2:

Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 12, "ALL" is mentioned. This includes offline users, so both id0 and id1 are mentioned. mentions = [2,2]

Example 3:

Input: numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]

Output: [0,1]

Explanation:

Initially, all users are online.

At timestamp 10, id0 goes offline.

At timestamp 12, "HERE" is mentioned. Because id0 is still offline, they will not be mentioned. mentions = [0,1]

Constraints:
1 <= numberOfUsers <= 100
1 <= events.length <= 100
events[i].length == 3
events[i][0] will be one of MESSAGE or OFFLINE.
1 <= int(events[i][1]) <= 105
The number of id<number> mentions in any "MESSAGE" event is between 1 and 100.
0 <= <number> <= numberOfUsers - 1
It is guaranteed that the user id referenced in the OFFLINE event is online at the time the event occurs.
"""

from typing import List
import heapq


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        result = [0] * numberOfUsers
        here = [1] * numberOfUsers
        ONLINE = "AA_ONLINE"
        OFFLINE = "A_OFFLINE"
        hq = []

        for event in events:
            time = int(event.pop(1))
            if event[0] == "OFFLINE":
                event[0] = OFFLINE
            payload = (time, event)
            hq.append(payload)
        heapq.heapify(hq)

        while hq:
            time, (message, recepient) = heapq.heappop(hq)
            if message == OFFLINE:
                here[int(recepient)] = 0
                payload = (time + 60, [ONLINE, recepient])
                heapq.heappush(hq, payload)
            elif message == ONLINE:
                here[int(recepient)] = 1
            else:
                if recepient == "HERE":
                    for i, b in enumerate(here):
                        result[i] += b
                elif recepient == "ALL":
                    for i in range(numberOfUsers):
                        result[i] += 1
                else:
                    for rec in recepient.split():
                        target = int(rec[2:])
                        result[target] += 1

        return result


def main():
    solution = Solution()
    events = [
        ["MESSAGE", "10", "id1 id0"],
        ["OFFLINE", "11", "0"],
        ["MESSAGE", "71", "HERE"],
    ]
    assert solution.countMentions(2, events) == [2, 2]
    events = [
        ["MESSAGE", "10", "id1 id0"],
        ["OFFLINE", "11", "0"],
        ["MESSAGE", "12", "ALL"],
    ]
    assert solution.countMentions(2, events) == [2, 2]
    events = [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]
    assert solution.countMentions(2, events) == [0, 1]
    events = [
        ["MESSAGE", "2", "HERE"],
        ["OFFLINE", "2", "1"],
        ["OFFLINE", "1", "0"],
        ["MESSAGE", "61", "HERE"],
    ]
    assert solution.countMentions(3, events) == [1, 0, 2]
    events = [
        ["OFFLINE", "44", "5"],
        ["MESSAGE", "98", "HERE"],
        ["OFFLINE", "78", "0"],
        ["OFFLINE", "88", "1"],
        ["OFFLINE", "44", "7"],
        ["MESSAGE", "94", "ALL"],
        ["MESSAGE", "66", "id7 id2 id1 id0 id5 id5"],
        ["MESSAGE", "10", "id9 id0 id7 id4"],
        ["OFFLINE", "61", "3"],
        ["MESSAGE", "37", "ALL"],
        ["MESSAGE", "40", "id5 id8 id9 id1 id4 id8 id7 id4 id8"],
        ["MESSAGE", "4", "ALL"],
        ["OFFLINE", "33", "8"],
        ["OFFLINE", "66", "6"],
        ["OFFLINE", "93", "8"],
        ["OFFLINE", "78", "4"],
        ["OFFLINE", "4", "1"],
        ["OFFLINE", "69", "2"],
    ]
    assert solution.countMentions(10, events) == [5, 5, 4, 3, 6, 6, 3, 6, 6, 6]
    print("✅ All tests passed!")


if __name__ == "__main__":
    main()
