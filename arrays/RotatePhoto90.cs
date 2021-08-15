using System;
using System.Text;

namespace arrays
{
    // I'm not sure if this is what was meant by "in place".
    static class RotatePhoto90
    {
        public static int[,] Rotate(int[,] photo){
            int len1D = photo.GetLength(0); 
            int len2D = photo.GetLength(1); 
            int[,] rotatedPhoto = new int[len2D,len1D];
            for (int i = 0; i < len1D; i++)
            {
                for (int j = 0; j < len2D; j++)
                {
                    int pixel = photo[i,j];
                    rotatedPhoto[j,i] = pixel;
                }
            }
            return rotatedPhoto;
        }
    }
}
