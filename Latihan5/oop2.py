class Student:
    def __init__(self,name,address):
        self.__name = name
        self.__address = address
        self.__numCourses = 0
        self.__courses = []
        self.__grades = []
        
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self,address):
        self.__address = address
        
    def addCourseGrade(self,course,grade):
        self.__courses.append(course)
        self.__grades.append(grade)
        self.__numCourses += 1
        
    def printGrades(self):
        for i in range(len(self.__courses)):
            print(self.__courses[i] +" : "+ str(self.__grades[i]))
            
    def getAverageGrade(self):
        sum = 0
        for n in self.__grades:
            sum += n
        return sum / len(self.__grades)
            

n_siswa = int(input("Masukkan Jumlah Siswa = "))
n_course = int(input("Masukkkan Jumlah Course = "))

siswa = []
for i in range(n_siswa):
    nama = input("Masukkan Nama Siswa = ")
    alamat = input("Masukkan Alamat Siswa = ")
    siswa.append(Student(nama,alamat))
    for j in range(n_course):
        mapel = input("Masukkan Nama Mapel Siswa "+nama+" = ")
        nilai = int(input("Masukkan Nilai Mapel Siswa "+nama+" = "))
        siswa[i].addCourseGrade(mapel,nilai)

print("Hasil")
for i in range(n_siswa):
    print(s1.getName(),s1.getAddress())
    siswa[i].printGrades()
    print("Rata-Rata : ", siswa[i].getAverageGrade())

# s1 = Student("Ani","Yogyakarta")
# print(s1.getName(),s1.getAddress())
# s1.addCourseGrade("Matematika",95)
# s1.addCourseGrade("IPA",90)
# s1.addCourseGrade("Bahasa Indonesia",85)
# s1.printGrades()
# print("Rata-Rata : ", s1.getAverageGrade())

# print()
# s2 = Student("Budi","Jakarta")
# print(s2.getName(),s2.getAddress())
# s2.addCourseGrade("Matematika",60)
# s2.addCourseGrade("IPA",70)
# s2.addCourseGrade("Bahasa Indonesia",100)
# s2.printGrades()
# print("Rata-Rata : ", s2.getAverageGrade())