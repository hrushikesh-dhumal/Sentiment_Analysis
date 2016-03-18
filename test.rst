Detecting humans and faces in images or videos is a challenging task due the
variability of pose, appearance and lighting conditions. Also the algorithms
have to robust enough to occlusion and clutter present in the backgrounds.
Figure 1 and Figure 2, shows human and face detection examples.

.. figure:: ../images/projects/human_detection_mikel_rodriguez.png
  
.. figure:: ../images/projects/nist_project_human_detection_example.png

   Figure 1. Human detection
 
.. figure:: ../images/projects/nist_project_face_detection.jpg

.. figure:: ../images/projects/nist_project_face_detection2.jpg

.. figure:: ../images/projects/face-detection-people.jpg

   Figure 2. Face detection

Algorithms One of the most widely used methods for human detection is the HOG
(Histograms of oriented gradients) [1].  [1] Dalal, Navneet, and Bill Triggs.
"Histograms of oriented gradients for human detection." In Computer Vision and
Pattern Recognition, 2005. CVPR 2005. IEEE Computer Society Conference on, vol.
1, pp. 886-893. IEEE, 2005.

For face detection one popular method is based on Harr wavelet and SVM
classifier described in the paper [2].  [2] Viola, Paul, and Michael J. Jones.
"Robust real-time face detection." International journal of computer vision
57.2 (2004): 137-154.

We could use the OpenCV implementation of human and face detection for our
project [3].  Mahout and/or Spark’s MLlib library for machine learning
consisting of common learning algorithms could be used for classification for
human and face detection.
(http://spark.apache.org/docs/1.2.1/mllib-guide.html)
