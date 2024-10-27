'''
पाइथोनमा AttributeError भनेको त्यस्तो त्रुटि हो जुन तपाईंले कुनै वस्तु (object)मा त्यस वस्तुमा नभएको एट्रिब्युट (attribute) 
वा मेथड (method) प्रयोग गर्दा आउँछ।

AttributeError को कारणहरू:

अपरिभाषित एट्रिब्युट: तपाईंले कुनै वस्तुमा त्यस वस्तुमा परिभाषित नगरिएको एट्रिब्युट प्रयोग गर्नुभयो।
अपरिभाषित मेथड: तपाईंले कुनै वस्तुमा त्यस वस्तुमा परिभाषित नगरिएको मेथड कल गर्नुभयो।
वस्तुको प्रकार गलत: तपाईंले एउटा वस्तुमा अर्को प्रकारको वस्तुको एट्रिब्युट वा मेथड प्रयोग गर्नुभयो।
टाइपो: तपाईंले एट्रिब्युट वा मेथडको नाम गलत लेख्नुभयो।
AttributeError को उदाहरण:

उदाहरण १: अपरिभाषित एट्रिब्युट
class Person:
    def __init__(self, name):
        self.name = name

person = Person("John")
print(person.age)  # AttributeError: 'Person' object has no attribute 'age'

उदाहरण २: अपरिभाषित मेथड
list = [1, 2, 3]
list.find(2)  # AttributeError: 'list' object has no attribute 'find'
'''