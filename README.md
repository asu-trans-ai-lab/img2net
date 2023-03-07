# img2net

![](media/1181c0d8c135e350bb363eb2c6667e9f.png)

Transportation networks are crucial for efficient traffic planning and
operation. However, obtaining accurate movement information at intersections is
often challenging and time-consuming. To address this issue, we propose a
machine learning-based approach that uses publicly accessible satellite images
from Google maps to automatically identify movement information for each
intersection.

Our approach involves developing a customized deep learning model to extract
movement information from satellite images. With this model, researchers can
easily generate movement information for all intersections in a given area
without relying on labor-intensive manual work.

To evaluate the effectiveness of our proposed method, we collected a large set
of intersection data in Arizona, US. Our results demonstrate that our approach
is highly accurate and efficient, making it an ideal solution for producing
movement information for intersection modeling and management tasks.

By leveraging the power of AI, our method offers a cost-effective and scalable
solution for improving transportation network data quality and efficiency. This
has the potential to significantly benefit traffic planning and operation tasks,
ultimately leading to better traffic management and improved traffic flow.

## Principle 1: Select gray pixels in the image and output the largest contour.

## ![Map Description automatically generated](media/dcafd2b81039dcfc0ecc2f68ee682001.PNG)![Icon Description automatically generated with medium confidence](media/4f216ee79908dec2161b45b166c7f9f9.jpeg)![A picture containing text Description automatically generated](media/1fdf27431c11cf33859db9d022e41048.png)

## Principle 2: Define the ROI area (excluding non-road areas), and then perform edge detection on the road

## ![A picture containing graphical user interface Description automatically generated](media/4bad053564563570ffed1cdd2fe4f2a9.png)
