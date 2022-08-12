import cv2
import os

"""
Functionalities
"""
class Service():

    def save_file_to_local( self,file ):
        folder       = 'uploads'

        # Save the image 
        file_path = os.path.join(folder, self.random_name_generator(file.filename) )
        file.save(file_path)

        # Rotate the file
        rotated_file = self.rotate_image( file.filename, file_path )

        # Return the path
        return {'rotated':rotated_file}


    def rotate_image( self, file_name, file_path ):

        # Reading an image in default mode
        src   = cv2.imread(file_path)
        image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

        # numpy to image
        rotate_name = 'rotate_90_'+file_name 
        cv2.imwrite('uploads/'+rotate_name,image)

        return 'uploads/'+rotate_name


    def random_name_generator( self, file_name ):
        return file_name 
