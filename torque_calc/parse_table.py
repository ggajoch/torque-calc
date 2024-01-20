import csv
f = open('table.txt', 'r')
lines = f.readlines()
f.close()

material = None
engagement = None

doing_table = False

results = []

for line in lines:
    if line.find('(Fsu = ') != -1:
        material = line.split('(')[0].strip()
        # print(material)
    
    if line.find('Length of Thread Engagement (in) = ') != -1:
        engagement = float(line.split('=')[1])
        engagement *= 25.4
        engagement = round(engagement, 1)
    
    if line.split(' ')[0].startswith('M'):
        fastener, pullout_load, assembly_torque, full_torque = line.strip().split(' ')

        fastener = 10*float(fastener[1:])
        if fastener % 10 == 0:
            fastener = int(fastener)//10
        else:
            fastener = round(fastener/10, 1)

        pullout_load = float(pullout_load)
        assembly_torque = float(assembly_torque)
        full_torque = float(full_torque)

        # change barbarian units to metric ones
        pullout_load *= 4.448218916
        assembly_torque *= 0.112984829
        full_torque *= 0.112984829

        # round
        pullout_load = round(pullout_load, 2)
        assembly_torque = round(assembly_torque, 1)
        full_torque = round(full_torque, 1)


        # print(f'{material} {engagement} {fastener} {pullout_load} {assembly_torque} {full_torque}')
        results.append((material, engagement, fastener, pullout_load, assembly_torque, full_torque))

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Material', 'Engagement [mm]', 'Fastener [Mx]', 'Pullout Load [N]', 'Assembly Torque [Nm]', '100% Torque [Nm]'])
    for result in results:
        writer.writerow(result)
