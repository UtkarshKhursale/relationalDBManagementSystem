Column Name |  Data Type| Is PII | Description
--- | --- | --- | ---
registrationId | VARCHAR | NO | PRIMARY-KEY, Unique Student Id e.g. E2Kxxx,I2Kxxx,C2Kxx
rollNumber     | INTEGER | NO | Roll Number of Student e.g.4059
firstName      | VARCHAR | YES| First Name of the Person
surName        | VARCHAR | YES| Last Name of the Person
email          | VARCHAR | YES| Email id of the Person
mobileNumber   | VARCHAR | YES| Mobile Number of the Person
aadhar         | VARCHAR | YES| Aadhar Card Number of the Parson
PAN            | VARCHAR | YES| PAN card Number of the Person
passport       | VARCHAR | YES| passport of the Person
nationality    | VARCHAR | NO | Nationality of the Person
isAadhar       | BOOLEAN | NO | Flag to Set if Person has aadhar Card or not
isPAN          | BOOLEAN | NO | Flag to Set if Person has PAN Card or not
isPassport     | BOOLEAN | NO | Flag to Set if Person has Passport or not
isIndian       | BOOLEAN | NO | Flag to Set if Person is Indian or not
fathersName    | VARCHAR | NO | Fathers Name of the Person
mothersName    | VARCHAR | NO | Mothers Name of the Person
permanantAddress   | VARCHAR | NO | permanent Address of the Person
residentialAddress | VARCHAR | NO | residential Address of the Person
tenthCGPA     | FLOAT | NO | tenth CGPA Score (On a Scale of 10)
twelfthCGPA    | FLOAT | NO | twelfth CGPA Score (On a Scale of 10)
tenthGrade    | FLOAT | NO | Tenth Grade (%)
twelfthGrade   | FLOAT | NO | twelfth Grade (%)
firstSemCGPA  | FLOAT | NO | 1 Sem CGPA Score (On a Scale of 10)
secondSemCGPA | FLOAT | NO | 2 Sem CGPA Score (On a Scale of 10)
thirdSemCGPA  | FLOAT | NO | 3 Sem CGPA Score (On a Scale of 10)
fourthSemCGPA | FLOAT | NO | 4 Sem CGPA Score (On a Scale of 10)
fifthSemCGPA  | FLOAT | NO | 5 Sem CGPA Score (On a Scale of 10)
sixthSemCGPA  | FLOAT | NO | 6 Sem CGPA Score (On a Scale of 10)
seventhSemCGPA| FLOAT | NO | 7 Sem CGPA Score (On a Scale of 10)
eightthSemGCPA| FLOAT | NO | 8 Sem CGPA Score (On a Scale of 10)
isDiploma     | BOOLEAN | NO | Flag to Set of Person is Diploma Student
diplomaMarks  | FLOAT | NO | Diploma Marks
isBacklog     | BOOLEAN | NO | Flag to Check if Person has Backlog
numberOfBacklogs | INTEGER | NO | Indicates number of Backlogs a Person has/had
activeBacklog    | INTEGER | NO | Indicates number of Backlogs a Person currently has
PassiveBacklog   | INTEGER | NO | Indicates number of Backlogs a Person had
isYD             | BOOLEAN | NO | Flag to set if Person has YD
YDYears          | INTEGER | NO | Number of YD
isEducationGap   | BOOLEAN | NO | Flag to Check if Person has taken Educational Gap
educationGapYears| INTEGER | NO | Number of Educational Year gap
isPICTStudent    | BOOLEAN | NO | Flat to Check if its PICT Student
currentBatch     | INTEGER | NO | Batch of the Student (Year when he/she will graduate)
