#
# 아이템44
#
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print('이전:', r0.get_ohms())
r0.set_ohms(10e3)
print('이후:', r0.get_ohms())

r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3

#
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms += 5e3

#
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print(f'이전: {r2.current:.2f} 암페어')
r2.voltage = 10
print(f'이후: {r2.current:.2f} 암페어')

#
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'저항 > 0이어야 합니다. 실제 값: {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#r3.ohms = 0

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#BoundedResistance(-5)

#
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms는 불변객체입니다")
        self._ohms = ohms

r4 = FixedResistance(1e3)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#r4.ohms = 2e3

#
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print(f'이전: {r7.voltage:.2f}')
r7.ohms
print(f'이후: {r7.voltage:.2f}')

