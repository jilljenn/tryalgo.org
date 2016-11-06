---
layout: en
title:  "Rectangles stacking order"
category: geometry
excerpt_separator: <!--more-->
---

Given a picture of overlaying rectilinear rectangles, detect which rectangle is above which one.

![]({{ site.images }}rectangles-stacking-order.svg "stacked rectangles"){: width="300px"}

<!--more-->

The input is provided as a list of polygons describing the visible parts of each rectangle. It is assumed that the rectangles can be distinguished by their color.

### Idea

For every color i find the smallest rectangle  R containing all its visible parts.  This can be done in linear time.  Then for every polygon of color j which is intersects R we know that j is above i.

For a fixed polygon and fixed rectangle this test can be done in linear time, linear in the number of segments of the polygon. The test reduces to interval intersection tests.  For every horizontal segment of the polygone that lies between the bottom and the top of the rectangle we need to check whether the projections on the x-axis of this segment and the rectangle intersect.  The situation is similar for the vertical segments. The concerned segments are shown in blue below. Note that we do not need to deal with the case that the rectangle is completely included in the polygon in this problem, as polygons do not overlap.

![]({{ site.images }}rectangles-stacking-order-polygone-intersect-rectangle.svg){: width="300px"}
