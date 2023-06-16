import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
import joblib

app = Flask(__name__)
#open file
file = open("model.pkl","rb")
#load trained model
trained_model = joblib.load(file)

@app.route('/')
def diagnopets_home():
    return render_template('diagnopets.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    integer_features = [int(x) for x in request.form.values()]
    feature = [np.array(integer_features)]
    prediction = trained_model.predict(feature)
    prediction =  prediction.item()
    if prediction == 'Feline Panleukopenia':
        description = "Feline Panleukopenia adalah penyakit viral yang sangat menular pada kucing. Penyakit ini disebabkan oleh virus feline panleukopenia (FPV) dan dapat menyerang sel-sel yang membelah dengan cepat, seperti sumsum tulang, jaringan limfoid, usus, dan janin yang sedang berkembang. Penularannya terutama melalui kontak langsung dengan cairan tubuh kucing yang terinfeksi, serta melalui objek yang terkontaminasi. Gejala umum termasuk demam, kehilangan nafsu makan, muntah, diare (kadang-kadang berdarah), dehidrasi, dan penurunan jumlah sel darah putih. Feline Panleukopenia dapat sangat parah pada anak kucing, kucing hamil, dan kucing dengan sistem kekebalan yang lemah."
    elif prediction == 'Feline Immunodi ficiency Virus':
        description = "Feline Immunodeficiency Virus (FIV) adalah virus yang menyerang kucing dan melemahkan sistem kekebalan tubuh mereka. Penularannya melalui darah, air liur, atau cairan tubuh kucing yang terinfeksi. FIV merusak sel-sel kekebalan tubuh, membuat kucing rentan terhadap infeksi dan penyakit. Gejalanya bisa beragam, mulai dari tidak ada gejala hingga penurunan berat badan, masalah pencernaan, dan infeksi kulit. Tidak ada obat yang menyembuhkan FIV, namun perawatan yang baik dapat membantu kucing hidup nyaman. Pencegahan meliputi sterilisasi, menghindari pertarungan, dan tes darah rutin untuk deteksi FIV."
    elif prediction == 'Feline Chlamydiosis':
        description = "Feline Chlamydiosis adalah infeksi bakteri pada kucing yang menyerang mata, hidung, dan saluran pernapasan. Gejalanya termasuk konjungtivitis, bersin, batuk, keluarnya cairan dari hidung dan mata, serta penurunan nafsu makan. Diagnosanya melalui pemeriksaan klinis dan tes PCR. Penanganannya melibatkan pemberian antibiotik seperti tetrasiklin atau azitromisin. Pencegahan meliputi isolasi kucing terinfeksi, menjaga kebersihan lingkungan, menghindari kontak dengan kucing liar, dan vaksinasi jika tersedia. Penting untuk berkonsultasi dengan dokter hewan untuk diagnosis yang akurat dan perawatan yang tepat."
    elif prediction == 'Feline infectious peritonitis':
        description = "Feline Infectious Peritonitis (FIP) adalah penyakit mematikan pada kucing yang disebabkan oleh virus corona. Virus ini menyebabkan peradangan sistemik dan dapat mempengaruhi organ-organ dalam tubuh kucing. FIP memiliki dua bentuk, yaitu kering dan basah. Gejalanya termasuk penurunan berat badan, kehilangan nafsu makan, demam persisten, pembengkakan abdomen, dan gangguan neurologis. Tidak ada pengobatan yang efektif untuk FIP, dan penyakit ini umumnya fatal. Pencegahan melibatkan vaksinasi (meskipun tidak sepenuhnya efektif) dan menjaga kebersihan lingkungan untuk mengurangi paparan terhadap virus."
    elif prediction == 'Feline Leukumia Virus':
        description = "Feline Leukemia Virus (FeLV) adalah virus yang menyerang kucing dan dapat menyebabkan gangguan serius pada sistem kekebalan tubuh. Virus ini menyebar melalui kontak langsung dengan kucing yang terinfeksi, terutama melalui air liur, air mata, dan darah. Infeksi FeLV dapat menyebabkan penurunan berat badan, anemia, infeksi berulang, masalah kulit, dan bahkan kanker. Tidak ada pengobatan yang dapat menyembuhkan FeLV, oleh karena itu pencegahan melalui vaksinasi, menjaga kucing di dalam rumah, dan menghindari kontak dengan kucing liar atau tidak dikenal sangat penting. Tes darah rutin dapat mendeteksi infeksi FeLV pada kucing."
    return render_template('diagnopets.html', prediction_text = "{}".format(prediction), description = description)

if __name__ == "__main__":
    app.run(debug=true)
