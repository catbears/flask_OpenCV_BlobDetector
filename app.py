import base64

import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import cv2
from blob_detector_params import BlobDetectorParams

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload_page():
    if request.method == "POST":
        # Get the uploaded image
        image = request.files["image"].read()

        # Convert the image to a numpy array
        image = cv2.imdecode(np.fromstring(image, np.uint8), cv2.IMREAD_COLOR)

        # Store unprocessed image in a global variable
        global unprocessed_image
        unprocessed_image = image

        # Process the image to detect blobs
        # params = BlobDetectorParams().params
        params = BlobDetectorParams().demo_params()
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(blurred_image)

        # Draw the keypoints on the image
        blob_image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Store the processed image in a global variable
        global processed_image
        processed_image = blob_image

        # Redirect to the results page
        return redirect(url_for("results_page"))
    else:
        return render_template("upload.html")


@app.route("/results")
def results_page():
    # Convert the processed image to a jpeg
    _, encoded_image = cv2.imencode(".jpg", processed_image)
    _, encoded_unprocessed_image = cv2.imencode(".jpg", unprocessed_image)

    # Convert the jpeg to a base64 string
    encoded_image = base64.b64encode(encoded_image).decode("utf-8")
    encoded_unprocessed_image = base64.b64encode(encoded_unprocessed_image).decode("utf-8")

    return render_template("results.html", image=encoded_image, unprocessed_image=encoded_unprocessed_image)


if __name__ == '__main__':
    app.run(debug=True)
