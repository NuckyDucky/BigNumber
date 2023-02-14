class BigNumber:
    def __init__(self, value=0):
        self.digits = []
        if value == 0:
            self.digits.append(0)
        else:
            while value > 0:
                self.digits.append(value % 10)
                value //= 10

    def __str__(self):
        return "".join(str(d) for d in reversed(self.digits))

    def __add__(self, other):
        result = BigNumber()
        carry = 0
        i = 0
        while i < len(self.digits) or i < len(other.digits) or carry != 0:
            s = carry
            if i < len(self.digits):
                s += self.digits[i]
            if i < len(other.digits):
                s += other.digits[i]
            result.digits.append(s % 10)
            carry = s // 10
            i += 1
        return result

    def __mul__(self, other):
        result = BigNumber()
        for i in range(len(self.digits)):
            carry = 0
            for j in range(len(other.digits)):
                s = self.digits[i] * other.digits[j] + carry
                if i + j < len(result.digits):
                    s += result.digits[i + j]
                    result.digits[i + j] = s % 10
                else:
                    result.digits.append(s % 10)
                carry = s // 10
            if carry > 0:
                result.digits.append(carry)
        return result

    def __sub__(self, other):
        result = BigNumber()
        carry = 0
        i = 0
        while i < len(self.digits) or i < len(other.digits):
            s = carry
            if i < len(self.digits):
                s += self.digits[i]
            if i < len(other.digits):
                s -= other.digits[i]
            if s < 0:
                s += 10
                carry = -1
            else:
                carry = 0
            result.digits.append(s)
            i += 1
        while len(result.digits) > 1 and result.digits[-1] == 0:
            result.digits.pop()
        return result

    def __truediv__(self, other):
        quotient = BigNumber()
        remainder = BigNumber()
        for d in reversed(self.digits):
            remainder.digits.insert(0, d)
            q = 0
            while other <= remainder:
                remainder = remainder - other
                q += 1
            quotient.digits.insert(0, q)
        while len(quotient.digits) > 1 and quotient.digits[-1] == 0:
            quotient.digits.pop()
        return quotient

    def __lt__(self, other):
        if len(self.digits) < len(other.digits):
            return True
        elif len(self.digits) > len(other.digits):
            return False
        else:
            for i in range(len(self.digits) - 1, -1, -1):
                if self.digits[i] < other.digits[i]:
                    return True
                elif self.digits[i] > other.digits[i]:
                    return False
            return False

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.digits == other.digits

    def __ne__(self, other):
        return self.digits != other.digits

    def __gt__(self, other):
        return not (self < other or self == other)

    def __ge__(self, other):
        return not (self < other)

    def __bool__(self):
        return len(self.digits) > 1 or self.digits[0] != 0

    def __neg__(self):
        result = BigNumber()
        result.digits = self.digits.copy()
        result.digits[-1] = -result.digits[-1]
        i = 0
        while i < len(result.digits) - 1 and result.digits[i] < 0:
            result.digits[i] += 10
            result.digits[i + 1] -= 1
            i += 1
        while len(result.digits) > 1 and result.digits[-1] == 0:
            result.digits.pop()
        return result

    def __abs__(self):
        result = BigNumber()
        result.digits = self.digits.copy()
        return result

    def __int__(self):
        result = 0
        for d in reversed(self.digits):
            result = result * 10 + d
        return result

    def __float__(self):
        return float(str(self))

    def __trunc__(self):
        return int(str(self))

    def __mod__(self, other):
        return self - (self // other) * other

    def __pow__(self, other):
        result = BigNumber(1)
        for i in range(other):
            result = result * self
        return result


##a = BigNumber(12345678901234567890)
##b = BigNumber(98765432109876543210)
##c = a * b
##print(c)


