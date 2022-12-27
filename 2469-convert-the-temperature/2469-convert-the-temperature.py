class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [] * 2
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        
        ans.append(kelvin)
        ans.append(Fahrenheit)
        
        return ans