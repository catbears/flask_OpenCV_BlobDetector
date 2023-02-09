import cv2


class BlobDetectorParams:
    """Blob Detector Parameters

    We use the standard parameters and allow for printing. If there are use
    cases, they can be added after the demo_params() method."""

    def __init__(self):
        """Initialize standard parameters"""

        self.params = cv2.SimpleBlobDetector_Params()
        self.params.minThreshold = 50
        self.params.maxThreshold = 220
        self.params.filterByArea = True
        self.params.minArea = 25
        self.params.filterByCircularity = False
        self.params.minCircularity = 0.8
        self.params.filterByConvexity = True
        self.params.maxConvexity = 0.4
        self.params.filterByInertia = True
        self.params.minInertiaRatio = 0.1

    def __str__(self):
        """Allow easy printing of parameters at any time."""
        return f"minThreshold: {self.params.minThreshold}\n" \
               f"maxThreshold: {self.params.maxThreshold}\n" \
               f"filterByArea: {self.params.filterByArea}\n" \
               f"minArea: {self.params.minArea}\n" \
               f"filterByCircularity: {self.params.filterByCircularity}\n" \
               f"minCircularity: {self.params.minCircularity}\n" \
               f"filterByConvexity: {self.params.filterByConvexity}\n" \
               f"maxConvexity: {self.params.maxConvexity}\n" \
               f"filterByInertia: {self.params.filterByInertia}\n" \
               f"minInertiaRatio: {self.params.minInertiaRatio}\n"

    def demo_params(self):
        """Set parameters to demo values"""

        # Change thresholds
        self.params.minThreshold = 10
        self.params.maxThreshold = 200

        # Filter by Area.
        self.params.filterByArea = True
        self.params.minArea = 10

        # Filter by Circularity
        self.params.filterByCircularity = True
        self.params.minCircularity = 0.1

        # Filter by Convexity
        self.params.filterByConvexity = True
        self.params.maxConvexity = 0.2

        # Filter by Inertia
        self.params.filterByInertia = True
        self.params.minInertiaRatio = 0.04

        return self.params


def main():
    """Show parameters and demo parameters to test the class."""
    bdp = BlobDetectorParams()
    print(str(bdp))
    bdp.demo_params()
    print(str(bdp))


if __name__ == "__main__":
    main()
