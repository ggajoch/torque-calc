from flask import Flask, render_template
import csv

app = Flask(__name__)

def read_csv(file_path):
    data = []
    materials = set()
    fasteners = set()
    engagements = set()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
            materials.add(row['Material'])
            fasteners.add(row['Fastener [Mx]'])
            engagements.add(row['Engagement [mm]'])

    sorted_materials = sorted(materials)
    sorted_fasteners = sorted(fasteners, key=float)  # Assuming fastener sizes are numeric
    sorted_engagements = sorted(engagements, key=float)  # Assuming engagements are numeric

    return data, sorted_materials, sorted_fasteners, sorted_engagements

@app.route('/')
def index():
    csv_data, materials, fasteners, engagements = read_csv('result.csv')
    return render_template('index.html', data=csv_data, materials=materials, fasteners=fasteners, engagements=engagements)

if __name__ == '__main__':
    app.run(debug=True)
