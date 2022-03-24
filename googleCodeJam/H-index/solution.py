from heapq import heappop, heappush


def h_index(n, citations):
    ans = []
    hq = []
    hindex = 0
    for i in range(n):
        if citations[i] > hindex:
            heappush(hq, citations[i])
        while hq and hq[0] <= hindex:
            heappop(hq)
        if len(hq) >= hindex+1:
            hindex += 1
        ans.append(hindex)
    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        paper_nr = int(input())
        citations = list(map(int, input().split()))
        h_index_scores = h_index(paper_nr, citations)
        print("Case #" + str(test_case) + ": " +
              ' '.join(map(str, h_index_scores)))
