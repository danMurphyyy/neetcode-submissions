class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if operation == "+":
                num1 = record[-1]
                num2 = record[-2]
                record.append(num1 + num2)

            elif operation == "D":
                num1 = record[-1] * 2
                record.append(num1)

            elif operation == "C":
                record.pop()

            else:
                record.append(int(operation))

        return sum(record)