class Student:
    def __str__(self):
        return f"Student, {self.name}, {len(self.grades)}, {self.average()}"
    def __gt__(self,other):
        if isinstance(other,Student):
            return self.average()>other.average()
        elif isinstance(other,(int,float)):
            return self.average()>other
        else:
            raise ValueError(f"can not compare Student and {other.__class__.__name__}")
        
    def __le__(self,other):
        return self.average() <= other.average()
    
s1 = Student("Diva")
s2 = Student("Leslie")

s1.add_course("math",90)
s1.add_course("programming",98)
s1.add_course("stats",100)

s2.add_course("geo",40)
s2.add_course("history",90)

print(s1)
print(s2)

if s1>s2:
    print(f"{s1.name} has higher grades than {s2.name}")

if s1<=s2:
    print(f"{s1.name} has lower grades than {s2.name}")

else:
    print(f"")

