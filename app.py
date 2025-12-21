from flask import Flask, render_template, request
import time

app = Flask(__name__)

# =====================
# ITERATIF
# =====================
def caesar_iterative(text, shift, mode):
    if mode == "decrypt":
        shift = -shift

    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


# =====================
# REKURSIF
# =====================
def caesar_recursive(text, shift, mode, index=0):
    if index == 0 and mode == "decrypt":
        shift = -shift

    if index == len(text):
        return ""

    char = text[index]
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        processed = chr((ord(char) - start + shift) % 26 + start)
    else:
        processed = char

    return processed + caesar_recursive(text, shift, mode, index + 1)


@app.route("/", methods=["GET", "POST"])
def index():
    data = {}

    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])
        mode = request.form["mode"]

        # ITERATIF
        start_i = time.perf_counter()
        result_iter = caesar_iterative(text, shift, mode)
        end_i = time.perf_counter()

        # REKURSIF
        start_r = time.perf_counter()
        result_rec = caesar_recursive(text, shift, mode)
        end_r = time.perf_counter()

        time_iter = (end_i - start_i) * 1000
        time_rec = (end_r - start_r) * 1000

        # KESIMPULAN
        if time_iter < time_rec:
            conclusion = "Algoritma Iteratif lebih cepat"
        elif time_rec < time_iter:
            conclusion = "Algoritma Rekursif lebih cepat"
        else:
            conclusion = "Keduanya memiliki waktu yang sama"

        data = {
            "iter_result": result_iter,
            "rec_result": result_rec,
            "time_iter": time_iter,
            "time_rec": time_rec,
            "conclusion": conclusion
        }

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
