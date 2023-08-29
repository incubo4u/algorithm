class Solution:

    def bestClosingTime(self, customers: str) -> int:
        clients_till = []
        all_y, all_n = 0, 0
        N = len(customers)
        for j, c in enumerate(customers):
            all_y += int(c == "Y")
            all_n += int(c == "N")
            clients_till.append((all_y, all_n))

        min_penality = all_n
        close_time = 0
        for j in range(N):
            pen_close, pen_open = clients_till[j]
            penality = pen_open + all_n - pen_close
            if penality < min_penality:
                min_penality = penality
                close_time = j + int(customers[j] == "Y")
        return close_time
