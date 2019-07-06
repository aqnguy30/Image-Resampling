import numpy
from math import floor, ceil
from resize import interpolation

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using nearest neighbor approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        old_width, old_height = image.shape

        new_width = int(old_width * float(fx))

        new_height = int(old_height * float(fy))

        x_scale = new_width / old_width

        y_scale = new_height / old_height

        resizedImage = numpy.zeros((new_width, new_height))

        for row in range(new_width):

            for col in range(new_height):
                # i = round(row / x_scale)

                # j = round(col / y_scale)

                i = min(round(row / x_scale), old_width - 1)

                j = min(round(col / y_scale), old_height - 1)

                resizedImage[row, col] = image[i, j]

        return resizedImage

        # Write your code for nearest neighbor interpolation here

        #return image

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        
        Note: Do not write the code to perform interpolation between points in this file.
        There is a file named interpolation.py, and two function definitions are provided
        linear_interpolation: Write your code to perform linear interpolation between two in this function
        bilinear_interpolation: Write your code to perfrom bilinear interpolation using four points in this functions. 
                                As bilinear interpolation essentially does linear interpolation three times, you coould simply call the 
                                linear_interpolation function three times, with the correct parameters. 
        """

        old_width, old_height = image.shape

        new_width = int(old_width * float(fx))

        new_height = int(old_height * float(fy))

        x_scale = new_width / old_width

        y_scale = new_height / old_height

        resizedImage = numpy.zeros((new_width, new_height))

        for row in range(new_width):

            for col in range(new_height):

                i = row / x_scale

                j = col / y_scale

                # If it is a known point

                if not (row % x_scale) and not (col % y_scale):
                    resizedImage[row, col] = image[int(i), int(j)]

                    continue

                unk = {'x': i, 'y': j}

                p11 = {'x': min(floor(row / x_scale), old_width - 1),

                       'y': min(floor(col / y_scale), old_height - 1)}

                p12 = {'x': min(floor(row / x_scale), old_width - 1),

                       'y': min(floor(col / y_scale) + 1, old_height - 1)}

                p21 = {'x': min(floor(row / x_scale) + 1, old_width - 1),

                       'y': min(floor(col / y_scale), old_height - 1)}

                p22 = {'x': min(floor(row / x_scale) + 1, old_width - 1),

                       'y': min(floor(col / y_scale) + 1, old_height - 1)}

                p11['intensity'] = image[p11['x'], p11['y']]

                p12['intensity'] = image[p12['x'], p12['y']]

                p21['intensity'] = image[p21['x'], p21['y']]

                p22['intensity'] = image[p22['x'], p22['y']]

                interpolation_obj = interpolation.interpolation()
                resizedImage[row, col] = interpolation_obj.bilinear_interpolation(p11, p12, p21, p22, unk)

        return resizedImage

        # Write your code for bilinear interpolation here

        #return image
