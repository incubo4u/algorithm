class Solution:

    def bestClosingTime(self, customers: str) -> int:
        clients_till = []
        N = len(customers)
        all_y = customers.count('Y')
        all_n = N - all_y
        min_penality = all_n
        curr_y = curr_n = close_time = 0
        for j, c in enumerate(customers):
            curr_y += (is_client := int(c == 'Y'))
            curr_n += int(c == 'N')
            penality = curr_n + all_n - curr_y
            if penality < min_penality:
                min_penality = penality
                close_time = j + is_client
        return close_time
