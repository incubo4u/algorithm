using System;

namespace arrays
{
    public static class Cross
    {
        public static int[,] CreateCrossFromCenter(int[,] matrix){
            int lenY = matrix.GetLength(0);
            int lenX = matrix.GetLength(1);
            bool[] row = new bool[lenX];
            bool[] collumn = new bool[lenY];
            // find centers
            for (int m = 0; m < lenX; m++)
            {
                for (int n = 0; n < lenY; n++)
                {
                    if(matrix[m,n]==0){
                        row[m]=true;
                        collumn[n]=true;
                    }
                }
            }
            // nullify row
            for (int rowIndex = 0; rowIndex < lenX; rowIndex++)
            {
                if(row[rowIndex]){
                    for (int y = 0; y < lenY; y++)
                    {
                        matrix[rowIndex,y] = 0;
                    }
                }
            }
            // nullify collumn
            for (int collumnIndex = 0; collumnIndex < lenY; collumnIndex++)
            {
                if(collumn[collumnIndex]){
                    for (int x = 0; x < lenX; x++)
                    {
                        matrix[x,collumnIndex]=0;
                    }
                }
            }
            return matrix;
        }
    }
}