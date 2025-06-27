class Solution:
    def multiply(self, num1, num2):
        def karatsuba(x, y):
            if len(x) == 1 or len(y) == 1:
                return str(int(x) * int(y))
            
            n = max(len(x), len(y))
            m = n // 2
            
            x = x.zfill(n)
            y = y.zfill(n)
            
            a, b = x[:n - m], x[n - m:]
            c, d = y[:n - m], y[n - m:]
            
            ac = karatsuba(a, c)
            bd = karatsuba(b, d)
            a_plus_b = str(int(a) + int(b))
            c_plus_d = str(int(c) + int(d))
            ad_plus_bc = karatsuba(a_plus_b, c_plus_d)
            
            ad_plus_bc_minus_ac_bd = str(int(ad_plus_bc) - int(ac) - int(bd))
            
            result = (
                int(ac) * 10 ** (2 * m) +
                int(ad_plus_bc_minus_ac_bd) * 10 ** m +
                int(bd)
            )
            return str(result)
        
        product = karatsuba(num1, num2)
        return product.lstrip('0') or '0'