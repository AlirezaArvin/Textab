import re
import csv

with open("Enter the path for your txt file here.") as f:
    content = f.readlines()
    content = list(map(lambda x: x.strip(), content))
    Numbers = []
    I2 = []
    R2 = []
    dataset_s = []
    count = 0
    for i in range(0, len(content)):
        exp = []
        if content[i][0:8] == 'estimate':
            exp = re.findall(r'(^\w+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+\d+\s+([^\s]+)\s+([^\s]+)\s+([^\s]+).*', content[i+2])
            count += 1
        if len(exp) != 0:
            dataset_s.append(exp[0])
        N = re.findall(r'Mixed-Effects Model \(k = (\d+); tau\^2 estimator: REML\)', content[i])
        R = re.findall(r'R\^2 \(amount of heterogeneity accounted for\):\s*(.+)%', content[i])
        I = re.findall(r'I\^2 \(residual heterogeneity / unaccounted variability\):\s*(.+)%', content[i])
        if len(N) != 0:
           Numbers.append(int(N[0]))
        if len(R) != 0:
            R2.append(float(R[0]))
        if len(I) != 0:
            I2.append(float(I[0]))

result = open("Enter the desired path to export and save the resulting CSV file.", 'w')
result.write('Variable, Number of Studies, R2 (%), Residual I2 (%), Estimate, SE, P-Value (95% CI)\n')
for i in range(0, len(Numbers)):
    result.write('%s,%i,%.2f,%.2f,%.3f,%.3f,%.3f (%.3f - %.3f)\n'% (dataset_s[i][0], Numbers[i], R2[i], I2[i], float(dataset_s[i][1]), float(dataset_s[i][2]), float(dataset_s[i][4]), \
                    float(dataset_s[i][5]), float(dataset_s[i][6])))
