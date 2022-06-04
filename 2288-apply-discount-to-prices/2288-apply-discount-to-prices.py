class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        helper = sentence.split(" ")
        ans = ""
        for i in helper:
            if i.count("$") == 1 and len(i) > 1 and i[0] == "$" and i[1:].isdigit():
                price = int(i[1:]) - (int(i[1:]) * discount/100)
                currans = str("%.2f"%price)
                ans += "$" + currans + " "
            else:
                ans += i + " "
        return ans[:-1]