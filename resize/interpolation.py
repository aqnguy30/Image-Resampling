class interpolation:

    #def linear_interpolation(self, pt1, pt2, unknown):
    def linear_interpolation(self, pt1, pt2, int1, int2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        if pt2 - pt1 != 0:

            term1 = int1 * (pt2 - unknown) / (pt2 - pt1)

            term2 = int2 * (unknown - pt1) / (pt2 - pt1)

            return term1 + term2

        else:

            return int1

        #Write your code for linear interpolation here

        #return

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
    #def BilinearInterpolationHelper(point11, point12, point21, point22, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        i1 = self.linear_interpolation(pt1['x'], pt3['x'], pt1['intensity'], pt3['intensity'], unknown['x'])

        i2 = self.linear_interpolation(pt2['x'], pt4['x'], pt2['intensity'], pt4['intensity'], unknown['x'])

        return self.linear_interpolation(pt1['y'], pt2['y'], i1, i2, unknown['y'])

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task


        #return

