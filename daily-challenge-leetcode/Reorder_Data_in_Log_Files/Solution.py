class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def comparator(log):
            split = log.index(" ")
            log_id, content = log[:split], log[split + 1:]
            content_is_digits = int(content[-1].isdigit())
            content_is_letter = int(not content_is_digits)
            return (
                content_is_digits,
                content * content_is_letter,
                log_id * content_is_letter,
            )

        logs.sort(key=comparator)
        return logs
