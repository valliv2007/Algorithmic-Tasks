"""Given the name of a US state or territory, return its postal abbreviation. All states, federal districts and inhabited territories will be tested, according to the linked wikipedia page.

Notes:

to spark your creativity, the size of your code is limited to 500 characters
the list of states and their respective abbreviations are listed below
import, exec, eval and "__" are forbidden
Examples
"Alabama"               -->  "AL"
"District of Columbia"  -->  "DC"
"U.S. Virgin Islands"   -->  "VI"
List of states and abbreviations
Alabama, AL
Alaska, AK
Arizona, AZ
Arkansas, AR
California, CA
Colorado, CO
Connecticut, CT
Delaware, DE
Florida, FL
Georgia, GA
Hawaii, HI
Idaho, ID
Illinois, IL
Indiana, IN
Iowa, IA
Kansas, KS
Kentucky, KY
Louisiana, LA
Maine, ME
Maryland, MD
Massachusetts, MA
Michigan, MI
Minnesota, MN
Mississippi, MS
Missouri, MO
Montana, MT
Nebraska, NE
Nevada, NV
New Hampshire, NH
New Jersey, NJ
New Mexico, NM
New York, NY
North Carolina, NC
North Dakota, ND
Ohio, OH
Oklahoma, OK
Oregon, OR
Pennsylvania, PA
Rhode Island, RI
South Carolina, SC
South Dakota, SD
Tennessee, TN
Texas, TX
Utah, UT
Vermont, VT
Virginia, VA
Washington, WA
West Virginia, WV
Wisconsin, WI
Wyoming, WY
District of Columbia, DC
American Samoa, AS
Guam, GU
Northern Mariana Islands, MP
Puerto Rico, PR
U.S. Virgin Islands, VI"""

def abbr(x):
    a=x.split()
    if len(a) > 1:
        if a[1][0:2]=='Ma':
            return 'MP'
        if a[1]=='of':
            a.pop(1)
        return a[-2][0]+a[-1][0]
    s=x.upper()
    b=s[0]
    if s[3:5] in ('SK','SO'):
        return b+s[4]
    if s[3:5] in ('ZO','TA'):
        return b+s[3]
    if s[-3:] in ('XAS','SEE','ADA','PPI','OTA'):
        return b+s[2]
    if s[1:3] in ('OW','ON','EO','EN','AW','AN','OU','IR','ER','AI','AR'):
        return b+s[-1]  
    return s[:2]

print(abbr('Louisiana'))