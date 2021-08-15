using System;
using System.Text;

namespace arrays
{
    //NxN.
    //Constatnt space
    static class RotatePhoto90
    {
        public static int[,] Transpose(int[,] tab)
        {
            int len = tab.GetLength(0);
            int v = -1;
            for (int i = 0; i < len; i++)
            {
                for (int j = 0; j < len; j++)
                {
                    if (i <= v || j <= v || i == 0 && j == 0) { continue; }
                    int temp = tab[i, j];
                    tab[i, j] = tab[j, i];
                    tab[j, i] = temp;
                }
                v++;
            }
            return tab;
        }
        public static int[,] Rotate(int[,] photo)
        {
            int len = photo.GetLength(0);
            photo = Transpose(photo);
            for (int i = 0; i < len; i++)
            {
                for (int j = 0; j < len; j++)
                {
                    int temp = photo[i, j];
                    photo[i, j] = photo[i, len - j - 1];
                    photo[i, len - j - 1] = temp;
                }
            }
            return photo;
        }
    }
}
