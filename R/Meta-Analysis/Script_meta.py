import re
import csv

with open("Enter the path for your output text file here.") as f:
    content = f.readlines()
    content = list(map(lambda x: x.strip(), content))
    titles = []
    numbers = []
    SMDs = []
    SMD_LCIs = []
    SMD_UCIs = []
    Ps = []
    I2 = []

    for i in range(0, len(content)):
        title = re.findall(r'^\w*:\s+(.+)', content[i])
        num = re.findall(r'Number of studies\: k \= (\d*)', content[i])
        SMD = re.findall(r'R.+ (.+) \[.+\; .+\] .+  .+$', content[i])
        SMD_LCI = re.findall(r'.+ .+ \[(.+)\; .+\] .+  .+$', content[i])
        SMD_UCI = re.findall(r'.+ .+ \[.+\; (.+)\] .+  .+$', content[i])
        P = re.findall(r'.+ .+ \[.+\; .+\] .+  (.+)$', content[i])
        I = re.findall(r'I\^2 = (.+%) \[.+\].+', content[i])
        if len(title) != 0:
            titles.append(title[0])
        if len(num) != 0:
            numbers.append(num[0])
        if len(SMD) != 0:
            SMDs.append(SMD[0])
        if len(SMD_LCI) != 0:
            SMD_LCIs.append(SMD_LCI[0])
        if len(SMD_UCI) != 0:
            SMD_UCIs.append(SMD_UCI[0])
        if len(P) != 0:
            Ps.append(P[0])
        if len(I) != 0:
            I2.append(I[0])
        
result = open("Enter the desired path to export and save the resulting CSV file.", 'w')
result.write('Title, Number of Studies, Pooled Effect Size (95% CI), P-Value, I2\n')
for i in range(0, len(titles)):
    result.write('%s,%s,%s (%s - %s),%s,%s\n'% (titles[i], numbers[i], SMDs[i], SMD_LCIs[i], SMD_UCIs[i], Ps[i], I2[i]))
